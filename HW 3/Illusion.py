# This program will use DrawingPanel to draw a figure. I found a DrawingPanel
# python program given by the University of Arizona online, and I input it in
# my code as the foundation to do this lab.

# Import the drawingpanel packet, and build the window and pick the pen.
from DrawingPanel import *
panel  = DrawingPanel(500, 400)
panel.set_background('gray')
canvas = panel.canvas

# This function represents an individual subfigure in the graph. num represents
# the number if circles in each subfigure. This function will initially draw
# the circles and then draw the totated recrangle in the subfigure.
def circles(x, y, height, width, num):
    for i in range(1, num + 1):
        canvas.create_oval(x + (i-1)*width/(2*num), y + (i-1)*height/(2*num),
        x + (i-1)*width/(2*num) + width*(num-i+1)/num, y + (i-1)*height/(2*num)
        + height*(num-i+1)/num, fill = 'red')
    canvas.create_line(x, y + height/2, x + width/2, y)
    canvas.create_line(x + width/2, y, x + width, y + height/2)
    canvas.create_line(x + width, y + height/2, x + width/2, y + height)
    canvas.create_line(x + width/2, y + height, x, y + height/2)

# Height and width are the data for the largest circles, and num represent the
# number of circles for each subfigure.
def blanket(x, y, height, width, num, rows):
    canvas.create_rectangle(x, y, x + width*rows, y + height*rows, fill = 'light gray',
    outline = 'red')
    for i in range(rows):
        for j in range(rows):
            circles(x + i*width, y + j*height, height, width, num)


circles(0, 0, 90, 90, 3)
circles(120, 10, 90, 90, 3)
circles(250, 50, 80, 80, 5)
blanket(10, 120, 100, 100, 10, 2)
blanket(350, 20, 40, 40, 5, 3)
blanket(230, 160, 50, 50, 5, 4)
