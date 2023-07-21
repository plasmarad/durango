"""
Compiles DHC to your system using clang
This script is mostly for users who wish to install dhc into their system (end-users)
This script is not for developers, if you wish to compile dhc , please use CMake
"""

import subprocess
import platform
import os
import argparse
from colorama import Fore

# pylint: disable=C0116 W0106 C0301

def clang_verify():
    # Determine the command to check for Clang based on the platform
    if platform.system() == "Windows":
        command = "where clang++"
    else:
        command = "which clang++"

    # Run the command and capture the output
    try:
        output = subprocess.check_output( command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return False

    # Check if the output contains "clang"
    return b"clang" in output

def run_dhc ():
    binary_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build", "dhc")
    if os.path.isfile(binary_path):
        try:
            dhc_args = input("Pass dhc arguments:\t")
        except EOFError:
            print("\nexiting...")
            exit()
        print(Fore.YELLOW + "RUNNING: " + Fore.RESET + binary_path+" "+dhc_args)
        subprocess.run(binary_path+" "+dhc_args, shell=True,stderr=subprocess.STDOUT,check=False).stdout
    else:
        print(Fore.RED +
            "Binary not found, source may not have been compiled or compilation may have failed."+
            Fore.RESET)
        exit()

def compile_dhc():
    if clang_verify() is False:
        print(Fore.RED + "ERROR: CLANG IS NOT INSTALLED ON YOUR SYSTEM!" + Fore.RESET)
        exit()
    compile_command = "clang++ ../**.cpp -I../../libraries -std=c++20 -o dhc"
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build"))
    # print command output
    print(Fore.YELLOW + "!: compilation is about to start"+Fore.RESET)
    subprocess.run(compile_command,shell=True,stderr=subprocess.STDOUT, check=False).stdout
    print(Fore.GREEN + "!: compilation finished"+Fore.RESET)

def lint_dhc():
    try:
        subprocess.run(["cpplint", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError:
        print("cpplint is not installed.")

    subprocess.run("cpplint ./**.cpp",shell=True, stderr=subprocess.STDOUT, check=False).stdout


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-r", action="store_true",help="runs dhc binary")
    parse.add_argument("-c", action="store_true",help="compile & run")
    parse.add_argument("-l", action="store_true",help="runs cpplint")
    args=parse.parse_args()

    if not any(vars(args).values()):
        print("No arguments passed, would you like to compile and run dhc? (y/n)")
    if args.c:
        compile_dhc()
    if args.r:
        run_dhc()
    if args.l:
        lint_dhc()