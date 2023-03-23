## Read Pride & Prejudice
# Author: Anthony Mc Garry


"""This code first checks whether the number of command line arguments is equal to 2. If it's not, the code prints an error message and exits.
If there are 2 command line arguments, the code assumes that the second argument is the filename of the text file to be processed."""

import sys

if len(sys.argv) != 2:
    print("Usage: python Pride.py <filename>")
    sys.exit(1)

filename = sys.argv[1]



"""Next, the code iterates over every character in the text using a for loop. For each character, 
the code checks whether it is equal to the letter "e". If it is, the code increases the counter variable by 1."""

try:
    with open(filename, "r") as f:
        text = f.read()
        count = 0
        for letter in text:
            if letter == "e":
                count += 1

    print("The letter 'e' appears", count, "times in the text file.")
except FileNotFoundError:
    print("File not found:", filename)
    sys.exit(1)