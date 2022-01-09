# reb-set-gen

A little tool that reads in two text files. One contains a format string which 
is expected to have two placeholders, `$BRAND` and `$IMAGE`. The other text 
file is supposed to contain multiple lines, each being one "brand". The tool 
then produces a new file, which has the same amounts of lines as the "brands" 
input file, but with each line being formatted according to the "formats" file.

## Dependencies

 - Python 3


## Installation

 - Install all dependencies
 - Download this tool and place it wherever you want

## Running

Open up a terminal (for example, "Windows Power Shell"), then navigate to the 
directory where you've put this tool into. Then run the tool with either of 
these commands (try both and see which one works):

    python ./reb-set-gen.py

    ./reb-set-gen.py

This should show you some more information as to how to actually run the tool 
(and have it do something more useful than just to show the help text).

## Command line arguments

To make the tool do something useful, you need to provide it with three 
command line options:

   | option | description |
   |--------|-------------|
   | -f     | Path to the format text file |
   | -b     | Path to the brands text file |
   | -o     | Path for the generated output file |

Example:

    ./reb-set-gen.py -f ./format.txt -b C:\Users\Gurt\Documents\IREM.txt -o C:\Users\Gurt\Documents\IREM-markenset.txt


