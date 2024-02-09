#!/usr/bin/env python

# courtesy of https://github.com/fmash16/riscv_emulator (modified test.py file to automate tests compilation)

import subprocess
import sys
import re
import os

def make_tests(rv_tests_dir, dest_dir):
    result = subprocess.check_output("riscv64-unknown-elf-objcopy --help", stderr=subprocess.STDOUT)
    print("Existence of riscv64-unknown-elf-objcopy", result)
    files = [f for f in os.listdir(rv_tests_dir) 
            if (os.path.isfile(os.path.join(rv_tests_dir, f)) 
                & (".dump" not in f)
                & ("Make" not in f)
                & ("git" not in f)
                )]

    for f in files:
        f = os.path.join(rv_tests_dir, f)
        filename = f.split("/")[-1]
        print("------------------\n")
        print(filename, end="\n")
        cmd = "riscv64-unknown-elf-objcopy -O binary " + f + " " + dest_dir + "/" + filename + ".bin"
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        print(filename, result)
    print(os.listdir(dest_dir))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print ("Usage: ./test.py <riscv-tests-dir> <destination>")
        exit(1)
    rv_tests_dir = sys.argv[1] + "/isa"
    dest_dir = sys.argv[2]
    make_tests(rv_tests_dir, dest_dir)
