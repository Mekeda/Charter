import os #os module imported here for file navigation
import re #reg expression imported here for finding MAC Addresses

solution = open("addresses.txt","w")
for subdir, dirs, files in os.walk('address_files'): #nested for loops to parse through every file in the directory that ends with .txt
    for file in files:
        if file.endswith('.txt'):
            i = 1   #counter for line matches
            matches = []    #matches array to keep track of present pattern on line number
            pattern = re.compile(r'\b[a-f0-9]{2}(?:([:-]?)[a-f0-9]{2}(?:\1[a-f0-9]{2}){4}|(?:\.?[a-f0-9]{2}){5})\b', re.IGNORECASE) #regex expression for finding MAC 48-bit addresses
            with open(os.path.join(subdir, file), 'r', encoding='utf8') as file:
                for line in file:
                    if re.search(pattern, line):
                        print("In file path:", file.name, ", MAC Address Found @ Line {}: ".format(i), line, file=solution)   #output solutions to a textfile in the same directory
                        matches.append(i)
                    i = i +1
            if not len(matches):
                raise Exception 
solution.close()