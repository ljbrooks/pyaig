class _truth_table(object):
    
    def __init__(self, m, d):
        self.m = m
        self.d = d

    def nvars(self):
        return self.m.N
    
    def __eq__(self, rhs):
        assert self.m == rhs.m
        return self.d == rhs.d
        
    def __hash__(self):
        return self.d
    
    def __and__(self, rhs):
        assert self.m == rhs.m
        d = self.d & rhs.d
        return _truth_table(self.m, d)
    
    def __or__(self, rhs):
        assert self.m == rhs.m
        d = self.d | rhs.d
        return _truth_table(self.m, d)
    
    def __xor__(self, rhs):
        
        if type(rhs) in (bool, int):
            if rhs:
                return ~self
            return self
        
        assert self.m == rhs.m
        d = self.d ^ rhs.d
        return _truth_table(self.m, d)
    
    def __invert__(self):
        d = self.m.mask & ~self.d
        return _truth_table(self.m, d)
    
    def implies(self, rhs):
        return ~self | rhs
    
    def iff(self, rhs):
        return ~(self ^ rhs)
    
    def cofactor(self, v, c):
        
        m = self.m.cofactor_masks[c][v]
        d = self.d & m

        nbits = 1 << v

        if c:
            d |= (d >> nbits)
        else:
            d |= (d << nbits)
        
        return _truth_table( self.m, d)
    
    def cofactors(self, v):
        return ( self.cofactor(v,True), self.cofactor(v, False) )
    
    def copy(self):
        return _truth_table(self.m, self.d)
    
    def permute(self, x, y):
        
        c_x = self.cofactors(x)
        c_xy = [ c.cofactors(y) for c in c_x ]
            
        vx = self.m.var(x, 1) 
        vy = self.m.var(y, 1) 
        
        return vy&( vx&c_xy[0][0] | ~vx&c_xy[0][1] ) | ~vy&( vx&c_xy[1][0] | ~vx&c_xy[1][1] )
    
    def negate(self, v):
        vv = self.m.var(v, 1) 
        cc = self.cofactors(v)
        return vv&cc[1] | ~vv&cc[0]
    
    def exists(self, v):
        c1, c0 = self.cofactors(v)
        return c1 | c0
    
    def forall(self, v):
        c1, c0 = self.cofactors(v)
        return c1 & c0
    
    def is_tautology(self):
        return self == self.m.const(1)
    
    def is_contradiction(self):
        return self == self.m.const(0)
    
    def is_satisfiable(self):
        return not self.is_contradiction()
    
    def depends(self, v):
        c1, c0 = self.cofactors(v)
        return c0.d != c1.d
    
    def min_variable(self, minv=0):        
        for v in xrange(minv, self.m.N):
            if self.depends(v):
                return v

        return None

    def permutations(self):
        "Generate all permutations of a _truth_table in lexicographical order"

        tt = self

        n = tt.nvars()
        a = range(n)
        
        while True:
            
            yield tt
            
            for j in xrange(1, n):
                if a[j] > a[j-1]:
                    break
            else:
                return

            for l in xrange(n):
                if a[j] > a[l]:
                    a[j], a[l] = a[l], a[j]
                    tt = tt.permute(l,j)
                    break
                    
            k = j-1
            l = 0

            while k>l:
                
                a[k], a[l] = a[l], a[k]
                tt = tt.permute(l,k)
                
                k -= 1
                l += 1

    def negations(self):
        "Generate all function derived by negating some of the inputs"
        
        n = self.nvars()

        for m in xrange( 0, 1<<n ):
            
            tt = self.copy()

            for v in xrange( n ):
                
                if m & ( 1 << v ):
                    tt = tt.negate(v)

            yield tt
            
    def all_npn(self):
        "Generate all NPN-equivalent functions"
        
        for p in self.permutations():
            for n in p.negations():
                yield n
                yield ~n

    def SOP(self):
        sop = self.isop()

        res = []
        
        N = self.nvars()
        
        for p in sop:
            pl = []
        
            for i in xrange(1, N+1):
                if i in p:
                    pl.append( '1' )
                elif (-i) in p:
                    pl.append( '0' )
                else:
                    pl.append( '-' )
                    
            pl.append(' 1')
            res.append( ''.join(pl) )
            
        return '\n'.join(sorted(res))

    def __str__(self):
        
        sop = self.isop()
        
        if len(sop) == 0:
            return '0'
            
        if len(sop) == 1 and len(sop[0]) == 0:
            return '1'
        
        res = []
        for p in sop:
            pl = []
            for l in sorted(p, key=abs):
                if l>0:
                    pl.append( self.m.name(l-1) )
                else:
                    pl.append( "!%s"%self.m.name(-(l+1)) )
            res.append( '&'.join(pl) )
        
        return ' + '.join(res)

    def __repr__(self):
        return "_truth_table(%d, %X)"%(self.m.N, self.d)

    def isop(self):
        (cres, fres) = self.m.isop(self,self, 0)
        assert fres == self
        return cres  
    
class truth_tables(object):

    def __init__(self, N):
        
        self.N = N
        self.nbits = 1 << self.N
        self.mask = ~( ~0L << self.nbits )
        self.names = {}
        
        self.cofactor_masks = [[],[]]
        
        for v in xrange(N):

            bits = 1<<v
            res = ~( ~0L << bits ) 
            
            mask_bits = bits << 1
            
            for _ in xrange( self.N-(v+1) ):
                
                res |= res << mask_bits
                mask_bits <<= 1
                
            self.cofactor_masks[0].append( res )
            self.cofactor_masks[1].append( res << bits )
        
    def name(self, i):
        if i in self.names:
            return self.names[i]
        return 'x%d'%i
        
    def const(self, v):
        return _truth_table(self, self.mask*v)
        
    def var(self, i, c=1):
        assert 0<=i< self.N
        assert c==0 or c==1
        return _truth_table(self, self.cofactor_masks[c][i])
    
    def all_functions(self):
        
        nfuncs = ( 1<<self.nbits )
        
        for i in xrange(nfuncs):
            yield _truth_table(self, i)

    def canonize(self):
    
        canonized = {}
        
        for f in self.all_functions():
    
            if f in canonized:
                continue
                
            for g in f.all_npn():
                canonized[ g ] = f

        return canonized

    def isop(self, L, U, i):

        if L.is_contradiction():
            return ([], L)
        
        if U.is_tautology():
            return ([set([])], U)
        
        x = min( L.min_variable(i), U.min_variable(i) )
        fx = self.var(x, 1)
        
        (L0,L1) = L.cofactors(x)
        (U0,U1) = U.cofactors(x)
        
        (c0, f0) = self.isop(L0 & ~U1, U0, x+1)
        (c1, f1) = self.isop(L1 & ~U0, U1, x+1)
        
        Lnew = L0 & ~f0 | L1 & ~f1
        (cstar, fstar) = self.isop(Lnew, U0&U1, x+1 )

        cres =  [ c.union(set([x+1])) for c in c0] + [ c.union(set([-(x+1)])) for c in c1] + cstar
        fres = f0&fx | f1&~fx | fstar

        return ( cres, fres )

    def conjunction(self, fs):
        return reduce( lambda f,g: f&g, fs, self.const(1) )
        
    def disjunction(self, fs):
        return reduce( lambda f,g: f|g, fs, self.const(0) )
        
    def xor(self, fs):
        return reduce( lambda f,g: f^g, fs, self.const(0) )
        
def cube(n):
    return reduce( lambda f,g: f&g, [ _truth_table.var(n, i, 1) for i in range(n) ], _truth_table.const(n,1) )

if __name__=="__main__":
    
    N = 10
    m = truth_tables(N)
    
    import string
    m.names.update( zip(range(N), string.uppercase ) )
    
    x = [ m.var(v,1) for v in xrange(N) ]
    
    print "XOR:"
    print m.xor(x[:4]).SOP()
    
    print "AND:"
    print m.conjunction(x).SOP()
    
    print "OR:"
    print m.disjunction(x).SOP()

    res = m.const(0)
    
    for i in xrange(1, N-2):
        res |= x[i]

    for i in xrange(N-2, N):
        res &= ~x[i]
        
    print "Equations:"
    print res
    print
    
    print "SOP:"
    print res.SOP()
    print
    
    res = res.permute(N/2,N-1)
    
    print "Equations, permuted:"
    print res
    print

    print "SOP, permuted:"
    print res.SOP()