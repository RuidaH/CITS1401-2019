
# Get the abbreviation of the name
def Q1(name):
    
    name = name.split()
    firstName = name[0]
    lastName = name[1]
    abbrev = firstName[:1] + lastName[:]
    
    return abbrev

print(Q1("Ruida He"))


# Turn the string into number
# Pay attention to the str(num)
def encode(msg):
    
    encode_msg = ""
    for i in msg:
        num = ord(i)
        encode_msg = encode_msg + str(num) + " "
    
    return encode_msg

test_String = "Found the beauty of life and improve yourself"
print(encode(test_String))


# Turn the number back to the string
# Pay attention to the chr(int(i))
def decode(msg_num):
    
    decoded_msg = ""
    msg_num = msg_num.split()
    for i in msg_num:
        string = chr(int(i))
        decoded_msg += string
        
    return decoded_msg

test1 = encode(test_String)
print(decode(test1))


# Another way to solve with decode
def decode1(msg_num):
    
    lst = []
    decode = msg_num.split()
    for i in decode:
        char = chr(int(i))
        lst.append(char)
        
    decoded_msg = "".join(lst)
    
    return decoded_msg

print(decode1(test1))


# Test the new line
# Why are there one more empty line in the last line
#   According my observation, when you write something into the file,
#   the cursor will stop at the nest line of the the last line of the file
def try1():
    
    with open("test of the overview.txt","w") as tf:
        print("hello \n to \n CITS2401", file = tf)
        
    i = 0
    
    with open("test of the overview.txt","r") as inputf:
        for line in inputf:
            i += 1
            print("line no.", i, ":", line)
            
def try2():
    
    f = open("test of the overview.txt","r")
    
    i = 0
    
    for line in f:
        
        i += 1
        print("line no.", i, ":", line)
        
    f.close()
    

def multable(num):
    
    print("*******************************")
    
    for i in range(21):
        
        print("{0:0d} x {1:2d} = {2:4d}".format(num, i, num*i))
        
    print("*******************************")
    

# Interactive loop
# Guess the number until you get it right
def guessGame(n):
    attempt = 1
    guessNum = int(input("Try the guess the right number: "))
    while n != guessNum:
        guessNum = int(input("Wrong! Try the guess the right number again: "))
        attempt += 1
    print("Congrate! You guess the right number in", attempt, "times")


# Sentinel loop
# The sentinle value is ""
def ave():
    print("The program will ask user to input number and find the sum of that numbers as well as their average")
    s = 0
    count = 0
    num = input("Input a number: ")   # you cannot use float here because "" cannot be converted into float numer
    while num:     # mean num != "":
        s += float(num)
        count += 1
        num = input("Input a number: ")
    print("the sum of these numbers is", s, "and their average is", s / count)
    
    
# For this time, you input a string containing num seperated by comma every time
def nested():
    
    s = 0
    count = 0
    
    line_of_input = input("Please input some number seperated by comma: ")
    
    while line_of_input:

        nums = line_of_input.split(",")
        
        for num in nums:    # make it become list and delete the comma
            s += float(num)
            count += 1
            
        line_of_input = input("Please input some number seperated by comma: ")
            
    print("The sum of these numbers is", s, "and their average is", s / count)
    

# Check if the number is a prime number
# Go up to half of the value
def isprime(n):
    if n < 2:
        return False
    elif n < 4:
        return True     # 2, and 3 are prime number
    else:
        for i in range(2, n//2+1):    # start from 2, note n //2 +1
            if n % i == 0:
                return False
    return True

# Find a list of number up to n
def primeList(n):
    if n < 2:
        return []
    elif n < 3:
        return [2]
    else:
        lst = [2]
        for i in range(3, n, 2):
            flag = True
            for k in range(2, i//2+1):
                if i % k == 0:
                    flag = False
                    break
            if flag:     # it means that flag == True
                lst.append(i)
    return lst
            

# Find n prime number
def Nprimes(n):
    if n == 0:
        return []
    elif n < 2:    # n = 1
        return [2]
    else:
        count = 1
        lst = [2]
        num = 3
        while count < n:
            flag = True
            for k in range(2, num//2+1):
                if num % k == 0:
                    flag = False
                    break
            if flag == True:
                lst.append(num)
                count += 1
            num += 1
    return lst

# Another method
def Nprimes1(n):
    plist = [2,3]
    if n == 0:
        return []
    elif n < 3:
        return plist[:n]
    else:
        num = 5      # the next prime number and it is odd number
        while len(plist) < n:
            status = True
            for i in range(2, num//2+1):
                if num % i == 0:
                    status = False
                    break
            if status == True:
                plist.append(num)
            num += 2     # since even number is never the prime number
    return plist
            

# Word frequency
def wordCut():
    
    file = open("test_of_word_frequency.txt", "r")
    filetxt = file.read()
    filetxt = filetxt.lower()
    
    chlist = list(range(128))
    del chlist[97:123]
    
    for i in chlist:
        filetxt.replace(chr(i), " ")
    
    filetxt = filetxt.split()    # Turn the string into the list
    
    dic = {}
    for word in filetxt:
        
        dic[word] = dic.get(word, 0) + 1
        
    # If we want descending sort as a list
    
    dlist = list(dic.items())
    dlist.sort(key = bycount, reverse = True)
    
    # print(dlist)
    
    return dic
       
def bycount(t):
    return t[1]


# Binary search
# Premise: the data is sorted
def bSearch(n, lst):
    
    low = 0
    high = len(lst) - 1
    
    while high >= low:
        
        mid = (high + low) // 2
        
        if lst[mid] == n:
            return mid    # Return the position
        elif lst[mid] < n:
            low = mid + 1
        elif lst[mid] > n:
            high = mid - 1
    
    return None   # Finally you cannot find the num in the list


# Rursion of binary search
def recBSearch(n, lst, low, high):
    
    mid = (high + low) // 2
    
    if high < low:
        return None    # one of the base case
    elif lst[mid] == n:
        return mid     # another base case
    elif lst[mid] < n:
        return recBSearch(n, lst, mid+1, high)
    elif lst[mid] > n:
        return recBSearch(n, lst, low, mid-1)
 

def Search(n,lst):
    return recBSearch(n, lst, 0, len(lst)-1)
    

# Recursion of fast exponentiation (better than iteration)
# when n is even, a ** n  = a ** (n//2) * a ** (n//2)
# when n is odd, a ** n  = a ** (n//2) * a ** (n//2) * a
def recPower(a, n):
    
    if n == 1:
        return a
    
    factor = recPower(a, n//2)
    if n % 2 == 0:
        return factor * factor
    elif n % 2 != 0:
        return factor * factor * a
    

# Fibonacci sequence,  1,1,2,3,5,8,... (n terms)
# Recursion
# 与iteration相比，Recursion是倒着过来从最大到1（base case）
def recFibo(n):
    
    if n <= 2:
        return 1
    
    return recFibo(n-1) + recFibo(n-2)
    
    
    

# Iteration for the sum of Fibonacci sequence
# The value at the n term
def iteraFibo(n):
    
    pre = 1
    cur = 1
    
    if n >= 3:
        for i in range(2, n):   # or range(n-2), range(3, n+1)
            cur, pre = cur + pre, cur
    
    return cur
        
    
        
    
    
            
            