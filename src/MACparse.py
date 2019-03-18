from __future__ import print_function
from io import open
 
import os
import re
 
MAC_REGEX = r'\b[a-f0-9]{2}(?:([:-]?)[a-f0-9]{2}(?:\1[a-f0-9]{2}){4}|(?:\.?[a-f0-9]{2}){5})\b'
 
 
def main():
    solution = open("addresses.txt", "w")
 
    # Nested for loops to parse through every file in the directory that ends with .txt
    for subdir, dirs, files in os.walk('address_files'):
        for in_file in files:
            if in_file.endswith('.txt'):
                line_num = 1   # Counter for line matches
                matches = []  # Matches array to keep track of present pattern on line number
                pattern = re.compile(MAC_REGEX, re.IGNORECASE)  # regex expression for finding MAC 48-bit addresses
                with open(os.path.join(subdir, in_file), 'r', encoding='utf8') as in_file_obj:
                    for line in in_file_obj:
                        if re.search(pattern, line):
                            line_str = u", MAC Address Found @ Line {}: ".format(line_num)
                            try:  # Python 2 Exception
                                f_name = unicode(in_file_obj.name)
                            except NameError:  # Python 3 Exception
                                f_name = in_file_obj.name
                            # Output solutions to a textfile in the same directory
                            print(u"In file path:", f_name, line_str, line, file=solution)
                            matches.append(line_num)
                        line_num += 1
                if not len(matches):
                    raise Exception
        print(u"\n\n", file=solution)
    solution.close()
 
 
if __name__ == "__main__":
    main()