import math


def print_matrix( matrix ):
    row = 0
    col = 0
    for c in range (len(matrix)):
        for r in range (4):
            print matrix[c][r] + " "
            c = 0
        print "\n"

    
    

def ident( matrix ):
    m = []
    for c in range (4):
        point = []
        for r in range (4):
            if (r == c):
                point.append(1)
            else:
                point.append(0)

        m.append(point)
    return m

#m1 * m2 -> m2
#change m2 in the end
def matrix_mult( m1, m2 ):
    retm = []
    if (len(m1) == len(m2[0])):
        for c in range (4):
            for r in range(4):
                retm[c][r] = retm[c][r] + m1[c][r] * m2[r][c]
            
        m2 = retm




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
            return m
