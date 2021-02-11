# Super Python Optimizer
Super Python Optimizer -- Scripts / Framework for increasing the speed of "Python" by way of implementing the program in a compiled language (Rust by default) and wrapping it, selectively unwrapping it by platform.

## Workflow (because it might work)
1. Write program.
2. Compile static release binaries for whichever necessary platforms.
3. Place binaries in the 'pack' folder, with a common \<binaryname\> root. As far as extensions, .exe is Windows (64-bit), .32exe is Windows (32-bit), .macos is MacOS (64-bit), and no filename is Linux (64-bit).
4. Run 'python3 spo.py \<binaryname\> \<outname\> [templatefile.py]' to create the final python script \<outname\>.py from the selected template. Running without the last parameter uses 'spotemplate.py'. Modify the user block near the bottom as necessary; this is either after running SPO, or by copying the template and editing in advance.

