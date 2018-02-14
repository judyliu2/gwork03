import math


def print_matrix( matrix ):
    r = 0
    c = 0
    for r in range (4):
        for c in range (4):
            print matrix[c][r] + " "
        print "\n"

    
    

def ident( matrix ):
    m = [];
    for c in range (4):
        for r in range (4):
            if (r == c):
                m.append(1)
            else:
                m.append(0)
    return m

#m1 * m2 -> m2
#change m2 in the end
def matrix_mult( m1, m2 ):
    if (len(m1) == len(m2[0])):
        for c in range (4):
            for r in range(4):




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
            return m
