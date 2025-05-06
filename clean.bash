#! /bin/bash
sudo cmake --build build --target uninstall
rm pymodule.so
rm -fR build
