from __future__ import print_function
import math
import random

def print_matrix( matrix ):
    for c in range (len(matrix)):

        for r in range (len(matrix[c])):
            print(matrix[r][c], end=' ')        
        print("\n", end='')
    print("\n", end='')

    
    

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

def rand_matrix():
    m = []
    for c in range(4):
        point = []
        for r in range (4):
            point.append(random.randint(0,10))
        m.append(point)
    return m

#m1 * m2 -> m2
#change m2 in the end
def matrix_mult( m1, m2 ):
    retm = new_matrix()
    for c in range (4):
        for r in range(4):
            #needs a 3rd loop because 3 separate matrixes
            for x in range(4):
              retm[c][r] +=  m1[x][r] * m2[c][x]
    for c in range(4):
        for r in range(4):
            m2[c][r] = retm[c][r]
    return m2
 




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m


