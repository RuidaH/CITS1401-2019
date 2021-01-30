import graphics as gx

win = gx.GraphWin()
p1 = gx.Point(70,70)    # class, starting with a capital letter
p2 = gx.Point(140,40)
p1.draw(win)     # drawing point on the windows
p2.draw(win)     # starting from left top, p1, p2 is the object
print(p2.getX())


c = gx.Circle(p1, 40)  # 40 is the radian
c.setFill("blue")
c.draw(win)

r = gx.Rectangle(p1, p2)
r.setFill("Red")
r.draw(win)

t = gx.Text(p2, "CITS2401")
t.draw(win)

