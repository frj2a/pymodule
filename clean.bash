#! /bin/bash
sudo cmake --build build --target uninstall 2>/dev/null
rm -f pymodule.so
rm -fR build
