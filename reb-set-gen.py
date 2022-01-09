#!/usr/bin/env python3

# concept:
#
# read three files,
# - format
# - images
# - brands
#
# `format` contains a one-line format string with placeholders, $IMAGE and $BRAND (or somesuch)
# `images` is a newline-separated list of image file names
# `brands` is a newline-separated list of brand names
#
# The numer of liens in `images` and `brands` needs to match, and the order of 
# entries in both files is assumed to match each other
#
# We read all three files, then generate a new file that contains one line for 
# each line of the `images`/`brands` files, where the line is based on the 
# `format` string, but with the placeholders replaced with the respective 
# entries from the `images` and `brands` files.

import os
import sys
import argparse

cfg_anykey_before_abort = (os.name == 'nt')

def abort(message, code=0, anykey=False):
    print(message)
    if anykey: 
        input("Press any key to end")
    sys.exit(code)

#
# argparse
#

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--format",  help = "Format file", default = "", required=True)
parser.add_argument("-i", "--images",  help = "Images file", default = "", required=True)
parser.add_argument("-b", "--brands",  help = "Brands file", default = "", required=True)
parser.add_argument("-o", "--output",  help = "Output file", default = "", required=True)

args = parser.parse_args()

#format_file = os.path.abspath(args.format)
#images_file = os.path.abspath(args.images)
#brands_file = os.path.abspath(args.brands)

format_file = args.format
images_file = args.images
brands_file = args.brands
output_file = args.output

if not os.path.isfile(format_file):
    abort("Not a file: " + format_file, 0, cfg_anykey_before_abort)

if not os.path.isfile(images_file):
    abort("Not a file: " + images_file, 0, cfg_anykey_before_abort)

if not os.path.isfile(brands_file):
    abort("Not a file: " + brands_file, 0, cfg_anykey_before_abort)

format_handle = open(format_file, 'r') 
format_lines  = format_handle.readlines()
format_string = format_lines[0].strip()
format_handle.close()

if format_string.find("$IMAGE") == -1:
    abort("Format string is missing '$IMAGE' placeholder", 0, cfg_anykey_before_abort)

if format_string.find("$BRAND") == -1:
    abort("Format string is missing '$BRAND' placeholder", 0, cfg_anykey_before_abort)

images_handle = open(images_file, 'r') 
brands_handle = open(brands_file, 'r') 

images_lines = images_handle.readlines() 
brands_lines = brands_handle.readlines()

num_images_lines = len(images_lines)
num_brands_lines = len(brands_lines)

if num_images_lines != num_brands_lines:
    images_handle.close()
    brands_handle.close()
    abort("File line number mismatch: images " + str(num_images_lines) + ", brands " + str(num_brands_lines), 0, cfg_anykey_before_abort)

output_handle = open(output_file, 'w')
num_output_lines = 0

for x in range(0, num_images_lines):
    output_string = format_string.replace("$IMAGE", images_lines[x].strip())
    output_string = output_string.replace("$BRAND", brands_lines[x].strip())
    output_handle.write(output_string + "\n")
    num_output_lines += 1

images_handle.close()
brands_handle.close()
output_handle.close()

print("Done, wrote " + str(num_output_lines) + " lines to " + output_file)
