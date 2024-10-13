

```
cd cudd-
./configure --shared
make -j 4
cd ../
```

# on mac m1 pro worked as following
```
python3 setup.py build --cudd
python3 setup.py install
```

# on linux 24.04

```
python3 setup.py build --cudd
python3 setup.py install
cp cudd/.libs/libcudd-so* ~/miniconda/lib


# helpful but no enough
conda install libstdcxx-ng 

# need to do the following
cd ~/minicond/lib
ln -sf ln -sf /usr/lib/gcc/aarch64-linux-gnu/13/libstdc++.so libstdc++.so.6
ln -sf ln -sf /usr/lib/gcc/aarch64-linux-gnu/13/libstdc++.so libstdc++.so
```
