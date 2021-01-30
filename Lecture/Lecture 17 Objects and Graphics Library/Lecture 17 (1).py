# Class contains abstract feature

# Normally, when we creat a function, we used to have small letter to start.
# when you have the class, you start with the capital letter

import graphics as gx

win = gx.GraphWin()

# drawing point
# point is class in it, it requires 2 inputs, creating an instance of point. and we call them p1, p2
# p1, p2 are all the objects of the class
p1 = gx.Point(70, 70)
p2 = gx.Point(140, 40)
p1.draw(win)      # p1 draw on window
p2.draw(win)

print(p2.getX())   # get the position in x coordinate (140)

# draw the circle
c = gx.Circle(p1, 40)    # p1 is the center of the circle, 40 is the radian
c.draw(win)

# draw the rectangle
# p1 is the left corner of the rectangle, p2 is the right corner of the rectangle
r = gx.Rectangle(p1, p2)    
r.draw(win)

# draw the text
t = gx.Text(p2, "CITS2401")
t.setFill("red")
t.draw(win)

# draw the line
l = gx.Line(p1, p2)
l.draw(win)

# draw the oval（椭圆形)
o = gx.Oval(p1, p2)
o.draw(win)



