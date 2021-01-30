
# Q1

def Q1():
    
    print("Looks like {1} and {0} for breakfast".format("eggs", "spam"))
    print("There is {0} {1} {2} {3}".format(1,"spam", 4, "you"))
    print("Hello {0}".format("Susan", "Computewell"))
    print("{0:0.2f} {0:0.2f}".format(2.3, 2.3468))
    print("{0:7.5f} {1:7.5f}".format(2.3, 2.3468))
    print("Time left {0:02}:{1:05.2f}".format(1, 37.374))
    print("{0:3}".format("14"))
    
# Q2
# 1 is not a prime number
def Q2(N):
    
    lst = [] 
    for i in range(2, N):
        k = 2
        while(i % k != 0):
            k += 1
        if k == i:
            lst.append(i)
    return lst

# Q3
# This one also didn't skip the even numbers
def Q3(N):
    
    lst = []
    for i in range(2, N):
        k = 3
        flag = False 
        for k in range(3, i):
            if i % k == 0:
                flag = True
        if flag == False:
            lst.append(i)     
    return lst
                
def Q3_1(N):
    
    lst = [2] 
    for i in range(3, N):
        if i % 2 == 0:
            continue
        k = 3
        while(i % k != 0):
            k += 1
        if k == i:
            lst.append(i)
    return lst

# Q4
# There are more situation
def intersect(r1, x1, y1, r2, x2, y2):
    import math
    dis = ((x2 - x1)**2 + (y2 - y1)**2)
    if math.aqrt(dis) < math.abs(r1 - r2):
        return False
    if math.sqrt(dis) < r1 + r2:
        return True
    else:
        return False

# Q5

def Q5(lst):
    
    for i in range(len(lst)):
        if i % 2 == 0 and i != len(lst) - 1:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst;
        
# Q6

def Q6(file_name):
    
    file_read = open(file_name, "r")
    
    for line in file_read:
        
        line.split()
        
        for i in range(len(line)):
            
            if len(line[i]) == 4:
                
                print(line[4])
    
    file_read.close()
    
# Q6("f1.txt")
    
# Q7

def Q7(file_name1, file_name2):       
    
    fread = open(file_name1, "r")
    fwrite = open(file_name2, "w")
    
    for line in fread:
        
        fwrite.write(line)
    
    fread.close()
    fwrite.close()    
    return fread, fwrite
    
# Q8


"""
p = 5
q = 7
n = p*q = 35
e is between 3 and n-1 which is 34
"""
def encryptor(file_name,file_name1, n,e):
    
    fread = open(file_name, "r")
    
    fwrite = open(file_name1, "w")
    
    for line in fread:
        
        for cha in line:
            
            m = ord(cha)
            
            c = pow(m, e) % n
            
            fwrite.write(str(c))
            
            fwrite.write(" ")
            
    fread.close()
    
    fwrite.close()
            
            
def decyrtor(file_name1, file_name2, n, e):
    
    fread = open(file_name1, "r")
    
    fwrite = open(file_name2, "w")
    
    p = 17
    
    q = 19
    
    phi_n = (p - 1) * (q - 1)
    d = 1
    
    while True:        
        ed  = e*d
        rem = ed % phi_n
        if rem == 1:
            break
        else:
            d +=1
#    print(d)
    for line in fread:
        list1 = line.split()
    for m in list1:        
        print(m)
        cha = int(m)        
        c = pow(cha, d) % n
        char_c = chr(c)
        fwrite.write(char_c)
            
    fread.close()
    
    fwrite.close()
    
            
    
    

    
            
