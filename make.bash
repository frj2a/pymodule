#! /bin/bash
rm -fR build
mkdir build
mkdir cmake
cmake . -B build && cmake --build build && sudo cmake --install build
ln -s build/pymodule*.so ./pymodule.so 
python3 test.py
