from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0,0,0 ]
matrix = new_matrix()

print("Testing new_matrix")
print_matrix(matrix)
print(" ")

print("Testing ident")
identity = ident(matrix)

print_matrix(identity)

test_matrix = rand_matrix()
print("test_matrix")
print_matrix(test_matrix)

print("Testing matrix_mult with identity")
matrix_mult(identity, test_matrix)
print_matrix(test_matrix)

print("test_matrix")
print_matrix(test_matrix)

test_matrix2 = rand_matrix()
print("test_matrix2")
print_matrix(test_matrix2)

print("multiplying test_matrix with test_matrix2")
matrix_mult(test_matrix, test_matrix2)
print_matrix(test_matrix2)


def square(matrix,x,y):
    for h in range(25):
        add_edge(matrix,x+25,y+h,0,x+50,y+h,0)
        
mid = 250

lines = new_matrix(4,0)
square(lines,100,100)
square(lines,125,75)
square(lines,150,75)
square(lines,175,100)
square(lines,200,100)
square(lines,225,100)
square(lines,250,100)
square(lines,275,75)
square(lines,300,75)
square(lines,325,100)
square(lines,350,125)
square(lines,350,150)
square(lines,350,175)
square(lines,350,200)
square(lines,350,225)
square(lines,325,250)
square(lines,325,275)
square(lines,275,275)
square(lines,325,300)
square(lines,350,325)
square(lines,375,350)
square(lines,375,375)
square(lines,350,375)
square(lines,325,375)
square(lines,300,350)
square(lines,275,325)
square(lines,250,325)
square(lines,225,350)
square(lines,225,375)
square(lines,200,350)
square(lines,200,375)
square(lines,225,325)
square(lines,200,325)
square(lines,175,325)
square(lines,150,325)
square(lines,125,350)
square(lines,100,375)
square(lines,75,375)
square(lines,50,375)
square(lines,50,350)
square(lines,75,325)
square(lines,100,300)
square(lines,100,275)
#left eye
square(lines,150,275)
square(lines,200,250)
#nose and mouth
square(lines,125,225)
square(lines,225,250)
square(lines,100,250)
square(lines,175,225)
square(lines,200,225)
square(lines,225,225)
square(lines,250,225)
square(lines,300,225)

#arms
square(lines,150,175)
square(lines,150,150)
square(lines,125,150)

square(lines,275,175)
square(lines,275,150)
square(lines,300,150)

square(lines,75,225)
square(lines,75,200)
square(lines,75,175)
square(lines,75,150)
square(lines,75,125)




draw_lines( lines, screen, color )
display(screen)
