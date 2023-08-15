from fplib import *
import itertools


f_whole = lambda r : lambda a,b: r*a + b
f_fractional = lambda r: lambda a, b: a+ b/r
def fold_whole (r):
    f = lambda a,b: r*a + b
    f = f_whole(r)
    def fn(lx):
        return foldl(f,0)(lx)
    return fn

def fold_fractonal (r):
    f = lambda a,b: a + b/r
    f = f_fractional(r)
    def fn(lx, r = r):
        return foldr(f,0)(lx)/r
    return fn
    
class FixedRadix:
    def __init__(self, r, digitx):
        self.r = r
        if isinstance(digitx, tuple):
            self.whole, self.fraction = digitx
        else:
            self.whole, self.fraction = digitx, 0
            pass
        pass

    @property
    def value(self): return self.fold_to_double()
    
    def fold_to_double(self):
        w = foldl(lambda a,b: a*self.r+b,0 )(self.whole)
        w2 = fold_whole(self.r)(self.whole)
        assert w == w2
        l = foldr(lambda a,b: a + b*(1/self.r),0 )(self.fraction)/self.r
        l2 = fold_fractonal(self.r)(self.fraction) 
        assert l == l2
        ww = foldl(lambda a, b: a*self.r +b, 0) (self.whole+self.fraction) / (self.r**len(self.fraction))
        if ww != w+l: print(ww, w+l)
        assert ww== w+l
        if self.r < 0: return self.compute_neg_radix()
        return w + l
    @property
    def value2(self):
        w = fold_whole(self.r)(self.whole)
        l = fold_fractonal(self.r)(self.fraction)
        ww = foldl(lambda a, b: a*self.r +b, 0) (self.whole+self.fraction) / (self.r**len(self.fraction))
        if ww != w+l: print(ww, w+l)
        assert ww== w+l
        if self.r < 0: return self.compute_neg_radix()
        return w , l

    def convert(self, new_radix):
        
        pass
    
    def compute_neg_radix(self):
        mul = lambda i: i[0] * i[1]
        even_w = freversed(fmap(mul, zip(freversed(self.whole), zeros_ones(1))))
        even_l = fmap(mul, zip(self.fraction, zeros_ones(0)))

        odd_w = freversed(fmap(mul, zip(freversed(self.whole), zeros_ones(0))))
        odd_l = fmap(mul, zip(self.fraction, zeros_ones(1)))

        even = radix(-self.r)(even_w, even_l)
        odd = radix(-self.r)(odd_w, odd_l)

        print(even.value, odd.value)
        return even.value - odd.value

def zeros_ones(init=0):
    assert init == 1 or init == 0
    yield init
    for i in zeros_ones(init ^ 1) : yield i 
    pass

def take(n):
    def fn(f):
        return list(itertools. islice(f, n))
    return fn

def radix(r):
    def fn(*digitx):
        return FixedRadix(r, digitx)
    return fn



if __name__ == '__main__':
    # this is 123.456
    a = [3,-1,5], [-4]
    
    x = radix(10)(*a)
    print(x.value)
    x = radix(-10)(*a)
    print(x.value)
    print(take(10)(zeros_ones(0)))
    x = radix(0.1)(*a)
    print(x.value)
    a =[ [3,-1,5], [3,0, -5], [1, -7, 0, -5]]
    for i in a:
        print (radix(10)(i,[0]).value)
        pass
    pass
