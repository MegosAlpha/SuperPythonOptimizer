# Super Python Optimizer
Super Python Optimizer -- Scripts / Framework for increasing the speed of "Python" by way of implementing the program in a compiled language (Rust by default) and wrapping it by platform.

## Planned workflow
1. Write program (in Rust).
2. Compile static release binaries (in Rust) for whichever necessary platforms.
3. Place binaries in the 'pack' folder. By default, .exe is Windows (64-bit), .32exe is Windows (32-bit), .macos is MacOS (64-bit), and no filename is Linux (64-bit).
4. Run 'python3 spo.py \<outname\>.py' to create the final script.
