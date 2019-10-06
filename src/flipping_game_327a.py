'''Iahub got bored, so he invented a game 
to be played on paper.

He writes n integers a1, a2, ..., an. 
Each of those integers can be either 0 or 1. 
He's allowed to do exactly one move: he chooses 
two indices i and j (1 ≤ i ≤ j ≤ n) and flips
all values ak for which their positions are in 
range [i, j] (that is i ≤ k ≤ j). Flip the value 
of x means to apply operation x = 1 - x.

The goal of the game is that after exactly one 
move to obtain the maximum number of ones. 
Write a program to solve the little game of Iahub.

Input
The first line of the input contains an integer 
n (1 ≤ n ≤ 100). In the second line of the 
input there are n integers: a1, a2, ..., an. 
It is guaranteed that each of those n values 
is either 0 or 1.

Output
Print an integer — the maximal number of 1s 
that can be obtained after exactly one move.
'''

def main():
    #retreive length of sequence
    numInt = int( input() )

    # retreive the actual 0-1 sequence
    seq_ = [int(x) for x in input().split(' ')]


    '''algo
        1. find longest 0's seq
        2. look left if more 1's than left 0's seq
            if not, add left seq
            if yes dont add left seq, stop left search
        3. look right if more 1's than right 0's seq
            if not, add right seq
            if yes dont add right seq, stop right search
        4. retreive left start index, right end index
        5. maximum number of ones is number of 1's outside
            the range + all 0's in range minus all 1's in range
    '''
    # 1. find longest 0's seq
    seqLen = 0
    maxSeqLen = 0
    s,e = 0,0 # start and end indexes of longest 0's seq
    prev = 1
    for i, el in enumerate(seq_) : 
        if not el:
            seqLen +=1
            if seqLen > maxSeqLen:
                maxSeqLen = seqLen
                e=  i
            if prev:
                s = i 
        else:
            seqLen = 0
        prev = el
        
    print('start: %s, end: %s, length: %s' 
            % ( s, e, maxSeqLen )
            )
    
    # 2. look left and right recursively
    def recursive_search( seq ):
        pass

    left_ = seq_[:s]
    right_ = seq_[e+1:]
    return 0

if __name__ == "__main__": main()

'''
    #find all zeros first
    zeros_ = [i for i in range( len( seq_ ) ) 
                if not seq_[i] 
                ]
    dist_ = [0] 
            + [zeros_[i] 
                - zeros_[i-1] 
                for i in range(len(zeros_))
                ]
    
    # spot 0's sequences length and split
    seqLen = 0
    seqSummary = []
    for i, el in zeros_ :
        if not el and el-el[i-1] == 1:


        
        

    # try finding all 0's sequences,
    #   their start and end index,
    #   their length
    #   and the number of 1's between them

    s,e = 0,0 # the start and end indexes of a 0's seq
    zeroSeq = [] # a list to contain all info
    inSeq = False # wether we are in a sequence or not

    prevSeqEnd = 0
    for i, el in enumerate( seq_ ):
        if not el and not inSeq:
            s = i #we just started a 0's seq
            inSeq = True 
        elif not el and inSeq:
            pass #0's sequence continues
        elif el and inSeq:
            e = i - 1 # just ended a seq
            inSeq = False
            zeroSeq.append( [s, 
                            e, 
                            e-s+1, 
                            e-prevSeqEnd] 
                        )
            
            prevSeqEnd = e

    print( zeroSeq )

    return None 
'''
