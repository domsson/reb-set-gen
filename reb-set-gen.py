#!/usr/bin/env python3

# concept:
#
# read two files,
# - format
# - brands
#
# `format` contains a one-line format string with placeholders, $IMAGE and $BRAND (or somesuch)
# `brands` is a newline-separated list of brand names

import os
import sys
import argparse

#
# configuration
#

cfg_anykey_before_abort = (os.name == 'nt')
cfg_image_extension = "png"

#
# helper methods
#

def abort(message, code=0, anykey=False):
    print(message)
    if anykey: 
        input("Press any key to end")
    sys.exit(code)

#
# asciify
#

asciify_char_map = {
    "__": "_", # for second iteration, fix adjacent underscores
    " ": "_", # different to the other space, no idea, keep it!
    " ": "_", # different to the first space, keep this as well!
    ",": "_",
    ";": "_",
    "&": "",
    "+": "",
	"á": "a",
	"à": "a",
	"â": "a",
	"ǎ": "a",
	"ă": "a",
	"ä": "ae",
	"ã": "a",
	"é": "e",
	"è": "e",
	"ê": "e",
	"ě": "e",
	"ĕ": "e",
	"ë": "e",
	"í": "i",
	"ì": "i",
	"î": "i",
	"ǐ": "i",
	"ĭ": "i",
	"ï": "i",
	"ó": "o",
	"ò": "o",
	"ô": "o",
	"ǒ": "o",
	"ö": "oe",
	"õ": "o",
	"ø": "o",
	"ɵ": "o",
	"ú": "u",
	"ù": "u",
	"û": "u",
	"ǔ": "u",
	"ŭ": "u",
	"ü": "ue",
	"ñ": "n",
	"ý": "y",
	"ÿ": "y",
    "ẞ": "ss",
    "ß": "ss",
}

def make_lower_ascii(string):
        string = string.lower()
        for search, replace in asciify_char_map.items():
                string = string.replace(search, replace)
        return string

#
# argparse
#

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--format",  help = "Format file", default = "", required=True)
parser.add_argument("-b", "--brands",  help = "Brands file", default = "", required=True)
parser.add_argument("-o", "--output",  help = "Output file", default = "", required=True)

args = parser.parse_args()

format_file = args.format
brands_file = args.brands
output_file = args.output

if not os.path.isfile(format_file):
    abort("Not a file: " + format_file, 0, cfg_anykey_before_abort)

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

brands_handle    = open(brands_file, 'r') 
brands_lines     = brands_handle.readlines()
num_brands_lines = len(brands_lines)

output_handle = open(output_file, 'w')
num_output_lines = 0

for x in range(0, num_brands_lines):
    brand_name = brands_lines[x].strip()
    image_name = make_lower_ascii(brand_name)
    image_name = make_lower_ascii(image_name) # second iteration to get rid of double underscores etc
    image_file = image_name + "." + cfg_image_extension
    output_string = format_string.replace("$IMAGE", image_file)
    output_string = output_string.replace("$BRAND", brand_name)
    output_handle.write(output_string + "\n")
    num_output_lines += 1

brands_handle.close()
output_handle.close()

print("Done, wrote " + str(num_output_lines) + " lines to " + output_file)
