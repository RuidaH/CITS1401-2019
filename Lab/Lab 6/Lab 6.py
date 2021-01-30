
# Q1

def all_different(S, E, N, D, M, O, R, Y) :
  digitlist = [S, E, N, D, M, O, R, Y]
  digitlist.sort()
  for i in range(len(digitlist) - 1) :
    if digitlist[i] == digitlist[i+1] :
      return False
  return True

# Q2

def readm(file_name):
    
    file_read = open(file_name, "r")
    
    lsts = []
    
    lst = []
    
    for line in file_read:
        
        lsts = line.split()
        
        lst.append(lsts)
    
    for i in range(2, len(lst[1])):   # Since the first row has the fisrt name and the last name, so there are different elements in the lst
        
        lst1 = []
        
        for k in range(1, len(lst)):
            
            lst1.append(int(lst[k][i]))
            
        a = max(lst1)
        
        for x in range(len(lst1)):
            
            if a == lst1[x]:
                
                break
        
        print(lst[x+1][0] + " " + lst[x+1][1] + " got the highest marks of ", a , " in " + lst[0][i+2])

    file_read.close()       
            

# Q3

def avg(file_name):
    
    file_read = open(file_name, "r")
    
    lsts = []
    
    lst = []
    
    for line in file_read:
        
        lsts = line.split()
        
        lst.append(lsts)
        
    for i in range(2, len(lst[1])):
        
        lst1 = []
        
        for k in range(1, len(lst)):
            
            lst1.append(int(lst[k][i]))
            
        a = sum(lst1) / len(lst1)
        
        print("The average mark of " + lst[0][i+2] + " is " , a)
        
    file_read.close()

# Q4

def passe(file_name):
    
    file_read = open(file_name, "r")
    
    lsts = []
    
    lst = []
    
    for line in file_read:
        
        lsts = line.split()
        
        lst.append(lsts)
        
    for i in range(2, len(lst[1])):
        
        count = 0
        
        lst1 = []
        
        for k in range(1, len(lst)):
            
            if int(lst[k][i]) >= 50:
                
                count += 1
                
        print("There are", count, "students passing the " + lst[0][i+2])
        
    file_read.close()
    
# Q5

def totalm(file_name):
    
    file_read = open(file_name, "r")
    
    lsts = []
    
    lst = []
    
    for line in file_read:
        
        lsts = line.split()
        
        lst.append(lsts)
        
    for k in range(1, len(lst)):
        
        count = 0
        
        lst1 = []
        
        for i in range(2, len(lst[1])):
                
            count += int(lst[k][i])
                
        print("The total mark of " + lst[k][0] + " " + lst[k][1] + " is ", count)
        
    file_read.close()

# Q6

def digit(N):
    
    n = int(N)
    
    # Use the length of string to get the number of decimal places
    string1 = str(N)
    string2 = str(n)
    
    floatdp = len(string1) - len(string2) - 1
    
    f = round(N - n, floatdp)   # use round function to simplify 0.3200000003
    
    count = 0

    while n != 0:
        
        count += n % 10
        
        n = n // 10
    
    i = 1
    
    while f != 0:
            
        k = 0
            
        f = f * 10
        
        k = int(f)
            
        count += k
            
        f = round(f - k, floatdp - i)
        
        i += 1
            
    return count
            
digit(32.32)           
        
    
def decimal_place(n):
    
    n = str(n)
    n = n.split(".")
    length = len(n[-1])
    
    return length


    
        

            
            
        