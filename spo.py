import base64
import sys
import os

fileexts = ['.exe', '.32exe', '.macos', '']
filereps = []
program_name = sys.argv[1]
out_name = sys.argv[2]
template_filename = 'spotemplate.py'
if len(sys.argv) > 3:
    template_filename = sys.argv[3]

for ext in fileexts:
    fname = os.path.join(os.path.curdir, 'pack', program_name + ext)
    if os.path.exists(fname):
        f = open(fname, 'rb')
        frep = base64.b64encode(f.read())
        filereps.append(frep)
    else:
        filereps.append(b'')

template = open(template_filename, 'r').readlines()
outfile = open(out_name + '.py', 'w')
file_reconstr = []
for line in template:
    if line == 'win64code = ""\n':
        file_reconstr.append(f"win64code = {filereps[0]}\n")
    elif line == 'win32code = ""\n':
        file_reconstr.append(f"win32code = {filereps[1]}\n")
    elif line == 'maccode = ""\n':
        file_reconstr.append(f"maccode = {filereps[2]}\n")
    elif line == 'linuxcode = ""\n':
        file_reconstr.append(f"linuxcode = {filereps[3]}\n")
    elif line == 'name = ""\n':
        file_reconstr.append(f"name = '{out_name}'\n")
    else:
        file_reconstr.append(line)

outfile.writelines(file_reconstr)
