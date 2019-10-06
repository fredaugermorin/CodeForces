'''You've got a 5 × 5 matrix, consisting of 24 zeroes 
and a single number one. Let's index the matrix rows 
by numbers from 1 to 5 from top to bottom, let's index
 the matrix columns by numbers from 1 to 5 from left 
 to right. In one move, you are allowed to apply one of 
 the two following transformations to the matrix:

Swap two neighboring matrix rows, that is, rows with 
indexes i and i + 1 for some integer i (1 ≤ i < 5).
Swap two neighboring matrix columns, that is, columns 
with indexes j and j + 1 for some integer j (1 ≤ j < 5).
You think that a matrix looks beautiful, if the single 
number one of the matrix is located in its middle 
(in the cell that is on the intersection of the third 
row and the third column). Count the minimum number of 
moves needed to make the matrix beautiful.

Input
The input consists of five lines, each line contains five 
integers: the j-th integer in the i-th line of the input 
represents the element of the matrix that is located on the 
intersection of the i-th row and the j-th column. It is 
guaranteed that the matrix consists of 24 zeroes and a single 
number one.

Output
Print a single integer — the minimum number of moves 
needed to make the matrix beautiful.
'''

# Accepted on 2019-09-14

NUMLINES = 5
NUMCOLS = 5

def main():
    middlerow = NUMLINES // 2 + 1
    middlecol = NUMCOLS // 2 + 1

    # fetch the input row by row
    for line in range(NUMLINES):
        input_ = input().replace(' ', '')
        if '1' in input_:
            row = line
            col = input_.find('1')
    
    # +1 since lists are 0 indexed
    numop = abs( row + 1 - middlerow ) \
            + abs( col + 1 - middlecol )

    print( numop )
    
    return numop

if __name__ == "__main__": main()
            