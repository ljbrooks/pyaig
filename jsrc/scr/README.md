

# design of the rewriting package


The expression is in the form of s/c tree, together with logic
operators. The expression is generated from 

```
python -i AGenSCTerms.py examples/WT_USP_KS_8x8_noX_multgen.sv.aig_out_4.aig 
```

which first rewrite the logic in to MAJ/XOR3 chains (AND and XOR) is
also identifies and represended using the function `s` and function
`c`, stands form sum and carry.

Then, we will follow the paper

> Sound and Automated Verification of Real-World RTL Multipliers

to implement the rewriting. The original paper using ACL2 's rewriting
package, but for our purpose, I will write a dedicated pythone package
for this.

1. First, the sc-tree is generated in `s.py`

2. A run.py is run to produce the rewriten adder tree.

## TODO

Currently, we are facing a problem that in order to do the rewriting,
I have to write a package such that same expression are identified as
being the same, and possibly ordered as well, then, further rewriting
can be carried out.

I can possibly write a dedicated rewriter which might be enough to
rewrite 90% of the sc-tree, which may or may not be enough. So wait to see.

Current status, as of 

```
commit 3696b244ec9ea782087234905818e68017602830
```

we are able to rewrite the Unsigned multiplier to remove all the
invertions.

To further handle it, I need to write a more dedicated package to
handle the expressions and later the rewrites. I have to identify
`s(x)` with `c(y)` in the case that `x` is the same as `y` which are
lists of arbitrary sc-terms.

## Objectives

I am hoping this sc-tree package can be evolved to handle future any
arithmetic logic for rewriting and verification.



## 二 7月 04 23:04:09 CST 2023

`scr/TermReduce.py` is able reduce the sc-term with the same
signature.

A signature is the uid and termx is replaced with TermList construct
which also has an uid. This is pretty cool

Now, I can apply the rewriting

``` python
c(  c(s(x), c(y), 
    c(x)))
    --> 
```

``` python
m(s((mx) + y) , m(s(x)+z) )

=  m (y + m (x + mz)) - m ( y+mx)

```
<!-- this is a fold, and needs be recognized -->
