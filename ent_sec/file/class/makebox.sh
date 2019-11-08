#! /bin/bash
mkdir box
mkdir box/bin
cp -v /bin/bash /home/class/box/bin
cp -v /bin/ls /home/class/box/bin
mkdir box/lib
mkdir box/lib64
cp /lib/x86_64-linux-gnu/libselinux.so.1 box/lib
cp /lib/x86_64-linux-gnu/libc.so.6 box/lib
cp /lib/x86_64-linux-gnu/libpcre.so.3 box/lib
cp /lib/x86_64-linux-gnu/libdl.so.2 box/lib
cp /lib64/ld-linux-x86-64.so.2 box/lib64
cp /lib/x86_64-linux-gnu/libpthread.so.0 box/lib
cp /lib/x86_64-linux-gnu/libtinfo.so.6 box/lib
cp /lib/x86_64-linux-gnu/libtinfo.so.6 box/lib
