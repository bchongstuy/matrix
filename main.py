from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = new_matrix(4,4)

add_edge(edges, 0, 0, 0, 0, 30, 0)
add_edge(edges, 0, 0, 0, 30, 0, 0)
add_edge(edges, 30, 30, 0, 30, 0, 0)
add_edge(edges, 30, 30, 0, 0, 30, 0)

for i in range(100):
    for j in range(100):
        add_edge(edges, 0, 0, 0, 0, 0, 0)
        add_edge(edges, 0, 0, 0, i, j, 0)
        add_edge(edges, 0, 0, 0, j, i, 0)


draw_lines(edges, screen, [255, 0, 0])




#ident(matrix)
#print_matrix(matrix)
#draw_lines( matrix, screen, color )
display(screen)