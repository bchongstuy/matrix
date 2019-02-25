"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for list in range(len(matrix[0])):
      line = ''
      for j in range(len(matrix)):
         line += str(matrix[j][list]) + ' '
      print(line[:-1])


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    n = len(matrix)
    for i in range(n):
      for j in range(n):
        matrix[i][j] = 0
    x = 0
    while x < n:
      matrix[x][x] = 1
      x += 1
    print (matrix)

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for i in range(len(m2)):
      cpy = [e for e in m2[i]]
      for j in range(len(m2[i])):
          v = 0
          for k in range(4):
              v += m1[k][j] * cpy[k]
          m2[i][j] = v



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m