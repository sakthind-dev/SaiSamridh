# -copy_file.py *- coding: utf-8 -*-
"""
Exercise: Convert this function to a standalone program or script that
takes two file names from the command line and copies one to the other.

Steps:
1. Delete "Def" line. You don't need it.
2. Use Edit menu of Spyder to Unindent all the lines.
3. import the system library sys
4. sys.argv is a list of the filenames following the program name.
   sys.argv[0] is the program name, sys.argv[1] is first argument, etc.
   Get the infilename and outfilename from this list.
5. Save the program as copy_file.py
6. Run the program from a terminal window (Mac), a cmd.exe window (PC,) or
   a command prompt within Spyder (use Tools>Open command prompt)

Here is how running it should look:
>python copy_file.py humptydumpty.txt newhumpty.txt
"""

""" Opens two files and copies one into the other line by line. """
import sys

if len(sys.argv) < 3:
    print("Usage: python copy_file_worked.py <input_file> <output_file>")
    sys.exit(1)
with open(infilename) as infile, open(outfilename, 'w') as outfile:
    for line in infile:
        outfile.write(line)    
infile.close()
outfile.close()
