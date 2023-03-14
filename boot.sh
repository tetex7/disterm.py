#!/usr/bin/env bash

YELLOW="\033[0;33m"
NO_COL="\033[0m"

if [ -r "./boot/init.boot" ]; then
    printf "${YELLOW}BOOTING${NO_COL}\n"
    ./boot/init.boot $@
else
    printf "BOOT ERR:\n\t\"init.boot\"\n\t\tIS NOT FOUND\n"
fi
