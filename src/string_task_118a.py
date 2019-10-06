'''Petya started to attend programming lessons. 
On the first lesson his task was to write a simple 
program. The program was supposed to do the following:
 in the given string, consisting if uppercase and 
 lowercase Latin letters, it:

    1. deletes all the vowels,
    2. inserts a character "." before each consonant,
    3. replaces all uppercase consonants with 
        corresponding lowercase ones.

Vowels are letters "A", "O", "Y", "E", "U", "I", 
and the rest are consonants. 
The program's input is exactly one string, 
it should return the output as a single string, 
resulting after the program's processing the initial 
string.
'''
# ANSWER ACCEPTED 2019-09-14

import sys


VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def main():
    # gather the input string
    input_ = str( input() )

    # Make all lowercase
    str_ = input_.lower()
    
    # Delete all vowels
    for v in VOWELS:
        str_ = str_.replace( v, '' )
    
    # Inser . before each consonnant
    str_ = '.' + '.'.join(str_)
    
    print(str_) 

    return str_ 

if __name__ == "__main__": main()



