# Q1

def sldic(slist):
    
    dic = {}
    for i in range(len(slist)):
        dic[i] = slist[i]
    return dic

# Q2

def edic(keys, names, ages):
    
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = [names[i], ages[i]]
    return dic


# Q3

def Q3(dic):
    
    lst = list(dic.values())
    keys = list(dic.keys())
    return max(lst), keys[lst.index(max(lst))]

    """
    Max = max(lst)
    Min = min(lst)
    items = list(dic.items())   # dic.items() doesn't support indexing
    for i in range(len(items)):
        if items[i][1] == Max:
            print("The key of the maximum is", items[i][1])
        if items[i][1] == Min:
            print("The key of the minimum is", items[i][1])
    return Max, Min
    """


import graphics as gx
import math as m
import time


# Q1

def Q1(x, y, radius):
    
    win = gx.GraphWin()
    p = gx.Point(x, y)         # like 70, 70
    p.draw(win)
    circle = gx.Circle(p, radius)
    circle.draw(win)

# Q2

def Q2(x, y, radius):
    
    win = gx.GraphWin()
    p = gx.Point(x, y)
    c = gx.Circle(p, radius)
    c.draw(win)
    
    area = m.pi * (radius ** 2)
    gx.Text(p, area).draw(win)       #gx.Text(gx.Point(x, y),"sth you want to print").draw(win)
    
    cir = 2 * m.pi * radius
    p1 = gx.Point(x+50, y+50)
    gx.Text(p1, cir).draw(win)        
    
# Q3

def Q3_1():
    
    win = gx.GraphWin()
    
    p1 = gx.Point(70, 10)
    p2 = gx.Point(10, 70)
    p1.draw(win)
    p2.draw(win)
    
    r = gx.Rectangle(p1, p2)
    r.draw(win)
    i = 0
    while i < 10:
        r.move(15, 0)
        time.sleep(2)
        i += 1

# Q5

def Q5(x, y):
    
    win = gx.GraphWin()
    
    p = gx.Point(x, y)
    r = 1
    for i in range(20):
        r = r*2
        c = gx.Circle(p, r)
        c.draw(win)
    
# Q6

def Q6():
    
    Option = input("Please enter the option (square, cicle or exit):")
    times = 0
    
    
    while Option != "exit" :
        
        if Option == "circle":    
            
            x = int(input("Please input x:"))
            y = int(input("Please input y:"))
            radius = int(input("Please input radius"))
            p = gx.Point(x, y)
            r = gx.Circle(p, radius)
            win = gx.GraphWin()
            r.draw(win)
            time.sleep(5)
            win.close()
            
        elif Option == "square":
            
            x1 = int(input("Please input x for the first location:"))
            y1 = int(input("Please input y for the first location:"))
            p1 = gx.Point(x1, y1)
            
#            x2 = int(input("Please input x for the second location:"))
#            y2 = int(input("Please input y for thr second location:"))
#            p2 = gx.Point(x2, y2)
#            
#            length = m.sqrt((x1 - x2) ** 2 + (y1 - y2) **2)
#            length1 = abs(x1 - x2)
#            length2 = abs(y1 - y2)
#            if length**2 != length1**2 + length2**2:
#                print("The location you input can not make a square, please try again!")
#                continue       # why does the program continue to ask user to input x and y for square rather than the asking the option
            
            # The second method
            length = int(input("Please input the side length of the square"))
            x2 = x1 + length
            y2 = y1 + length
            p2 = gx.Point(x2, y2)
            
            s = gx.Rectangle(p1, p2)
            win = gx.GraphWin()
            s.draw(win)
            time.sleep(5)
            win.close()
        
        else:
            
            print("what you input doesn't match, please try again1")
            
        times += 1
        if time == 10:
            print("You have entered 10 times, please exit now")
            break
        
        Option = input("Please enter the option (square, cicle or exit):")
        
    print("The end of the function")
    
    

# Q7

def Q7(x, y, z):
    
    # x, y, z cna be list or item
    
    m = (x[1] - y[1]) / (x[0] - y[0])
    n = x[1] - m * x[0]
    
    if z[1] == z[0] * m + n:
        
        print("These three points would form one line, please try other points!")
        
    else:

        p1 = gx.Point(x[0], x[1])
        p2 = gx.Point(y[0], y[1])
        p3 = gx.Point(z[0], z[1])
    
        l1 = gx.Line(p1, p2)
        l2 = gx.Line(p1, p3)
        l3 = gx.Line(p2, p3)
    
        win = gx.GraphWin()
        l1.draw(win)
        l2.draw(win)
        l3.draw(win)
        
# Q8

import random as rnd

def square(x1, y1, num, win):
    
    p1 = gx.Point(x1, y1)
    length = int(200 / num)
    x2 = x1 + num
    y2 = y1 + num
    p2 = gx.Point(x2, y2)
            
    s = gx.Rectangle(p1, p2)
    
    colors = ["red", "blue", "yellow", "black", "white"]
    s.setFill(colors[rnd.randrange(0, len(colors))])
    
    s.draw(win)
    
    

def Q8():
    
    num = int(input("Please input number of squares: "))
    
    if int(m.sqrt(num)) ** 2 != num :
        
        print("The number you input can not form the squares in the 200 * 200 windows")
        
    else:
        
        sqrtNum = int(m.sqrt(num))
        
        length = 200 / sqrtNum
        
        win = gx.GraphWin()

        for rows in range(sqrtNum):
            
            x = rows * length
            
            for columns in range(sqrtNum):
                
                y = columns * length
                
                square(x, y, length, win)

        
        
        
    
    
    
    