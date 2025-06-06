#! /bin/bash
rm -fR build
mkdir build
mkdir cmake 2>/dev/null
cmake . -B build && cmake --build build && sudo cmake --install build
# ln -s build/pymodule*.so ./pymodule.so 
python3 test.py
