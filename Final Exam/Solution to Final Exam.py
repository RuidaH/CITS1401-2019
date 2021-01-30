import os

# Q1

def splitAddress(address):
    
    address = address.replace("@", ".")
    addlst = address.split(".")
    return addlst

# Q2

def baseName(p):
    
    p = p.split("/")
    finalp = p[-1]
    finalp = finalp.split(".")
    return finalp[0]

# Q3

def manhat(x, y):
    
    length = len(x)     # assigning the length into a variable can reduce the calculation
    
    total = 0
    
    for i in range(length):
        
        total += abs(x[i] - y[i])
        
    return total

# Q4

def try4(f):
    
    if os.path.exists(f):
        return [c for c in open(f,'r').read().split('\n') if c != ""]

def SameSol(f):
    
    if os.path.exists(f):
        
        k = open(f, "r").read()
        k = k.split("\n")
        lst = []
        
        for c in k: 
            if c != "":
                lst.append(c)
                
        return lst
    return []
            
def sampleAnswer(f):
    
    if os.path.exists(f):
        infile = open(f, "r")
        non_blanks = []
        
        for line in infile:
            line = line.strip()   # to remove "\n"
            # line = line[:-1]      This one is also great
            if line != "":
                non_blanks.append(line)
        return non_blanks
    return []
        
# Q5

def ft6b():
    numberGames = {}
    numberGames[(1,2,4)] = 5
    numberGames[(4,2,1)] = 10
    numberGames[(1,2)] = 12
    
    try:
        sum = 1
        for k in numberGames:
            sum *= numberGames[k]    # The sum is 600 because it go through all the loop
        numberGames.append(sum)      # You cann't just append only one value(dic is with key-value pairs)
        print('Try block executed.')    
    except:
        print('Exception occured')
    print(numberGames, 'Sum=',sum)
    
# Q6

# I have three ways to do these

# list1 and list2 are sorted in ascending order

def merge1(list1, list2):
    
    lst = []
    l1 = 0
    l2 = 0
    
    while l1 < len(list1) and l2 < len(list2):
    # Or while len(list1)  == 0 or len(list2) == 0:
        
        if list1[l1] < list2[l2]:   # keep l1 and l2 0 because we are always deleting the elements in the list
            lst.append(list1[l1])   # it is awful to change the index
            del list1[l1]                 
        else:
            lst.append(list2[l2])
            del list2[l2]
    
    lst += list1
    lst += list2    # no matter which list has remain elements, just add them up
    
    return lst
            
# If you don't delete the elements in the list..
def merge2(list1, list2):
    
    lst = []
    l1 = 0
    l2 = 0
    
    while l1 < len(list1) and l2 < len(list2):
        
        if list1[l1] < list2[l2]:   
            lst.append(list1[l1])  
            l1 += 1                 
        else:
            lst.append(list2[l2])
            l2 += 1
    
    lst += list1[l1:]
    lst += list2[l2:]
    
    return lst

# Insert the elements of the list1 into the list2
def merge3(list1, list2):
    
    for i in range(len(list1)):
        
        for k in range(len(list2)):
            
            if list1[i] >= max(list2):
                list2.append(list1[i])
                break
            
            if list1[i] <= list2[k]:
                list2.insert(k, list1[i])
                break
    
    return list2

# Q7

def marksDistribution(D):
    
    grades = {}
    
    for mark in D:
        
        if D[mark] >= 80:
            grades["HD"] = grades.get("HD", 0) + 1
            
        elif D[mark] >= 70:
            grades["D"] = grades.get("D", 0) + 1
            
        elif D[mark] >= 60:
            grades["Cr"] = grades.get("Cr", 0) + 1
        
        elif D[mark] >= 50:
            grades["P"] = grades.get("P", 0) + 1
            
        else:
            grades["N"] = grades.get("N", 0) + 1
            
    return grades

# Q8

def Pow(x, N):
    
    if N == 0:
        return 1
    
    fac = Pow(x, N//2)
    
    if N % 2 == 0:
        
        return fac * fac
    
    else:
        
        return fac * fac * x
    
