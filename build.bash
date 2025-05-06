#! /bin/bash
rm -fR build
mkdir build
cd build
cmake ..
make
cd ..
ln -s build/pymodule*.so ./pymodule.so 
