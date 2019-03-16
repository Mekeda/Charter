# Charter
## Coding Assessment Problem 2: Find some MAC Addresses

### Project Requirements:
	**Language**: Any
	**Constraints**: N/A

	We have a directory of thousands of text files. Lines in these files may include a 48-bit MAC address in the format "AA:BB:CC:DD:EE:FF".
	Provide a solution that examines the files and outputs the filename, line number, and MAC address for every MAC address present.

### Project Description:
	**Language**: Written in Python 3.7
	**Libraries**: Python Native Libraries including: os and re
	**OS Environment**: Windows

	In order to parse through any text files and find MAC addresses in the format "AA:BB:CC:DD:EE:FF", the library usage of re for regex expressions was needed.
	For looping purposes, the os library needed to be used to step through each file in the subdirectory and each line within each file.
	The resulting solution will output the filename, line number, and the MAC address text line it was located on to a textfile labeled 'addresses.txt'.

	In order to run the MACparse.py program, it needs to be ran in a Python 3.x environment.

	Console command:
	- cd Desktop/Charter/src
	- python MACparse.py