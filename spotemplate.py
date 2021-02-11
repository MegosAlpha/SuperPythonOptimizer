import os
import platform
import sys
import base64
import subprocess

osid = platform.system()

# Base-64 Platform Dependent Code (Filled by SPO)
# Easy to extend, just handling the major cases basically
win64code = ""
win32code = ""
maccode = ""
linuxcode = ""

# Name of program, from outfile cmdline parameter.
name = ""

is_64bits = sys.maxsize > 2**32

# Universal .exe just because the other OS's shouldn't care about extensions here
# Less with statements necessary
with open(name + ".exe", 'wb') as f:
    if osid == "Windows":
        if is_64bits or win32code == "":
            f.write(base64.b64decode(win64code))
        else:
            f.write(base64.b64decode(win32code))
    elif osid == "Darwin":
        f.write(base64.b64decode(maccode))
        os.chmod(name + ".exe", 0o744)
    elif osid == "Linux":
        f.write(base64.b64decode(linuxcode))
        os.chmod(name + ".exe", 0o744)

# Execution step
# Note that this is somewhat geared towards unit testing
# To handle such a case, impl in the program robust cmdline parameter support for its functions.

def run_with_params(params):
    actual_program = subprocess.run([os.path.join(os.path.curdir, name+".exe")] + params, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    return actual_program.stdout

def run_normal():
    if len(sys.argv) > 1:
        return run_with_params(sys.argv[1:])
    return run_with_params([])

# User
# Your code goes here! Implement passthrough translation functions as much as necessary.
print(run_normal(), end='')

# End user block

if os.path.exists(name + ".exe"):
    os.remove(name + ".exe")
