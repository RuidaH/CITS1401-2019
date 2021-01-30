# Q1

def e1_1():
    string_a = "myprogram.exe"
    string_b = string_a.strip(".exe")
    return string_a[5:9], string_b

def e1_2():
    string_a = "myprogram.exe"
    lens = len(string_a)
    if lens % 2 == 0:
        return string_a[int(lens/2)-1]
    else:
        return string_a[int((lens+1)/2)-1]

# Q2

def e2_1(code, n):
    decode = ""
    for i in range(0,len(code)):
        trans = ord(code[i]) - ord("a")
        code_a = chr((trans + n) % 26 + ord("a"))
        decode += code_a      
    return decode                         

e2_1("xyz",5)

# Q3

def octalToDecimal(octal_num):
    octal_num = str(octal_num)
    decimal_num = 0
    lens = len(octal_num)
    for i in range(0,lens):
        decimal_num += int(octal_num[i])*(8**(lens-i-1))
    return decimal_num

"""
def decimalToOctal(decimal_num):
    octal_num = []
    trans = decimal_num
    remainder = 1
    while remainder != 0:
        remainder = trans % 8
        print(remainder)
        octal_num.append(remainder)
        trans = int((trans - remainder) / 8)
    octal_num.reverse()
    return octal_num
"""

def d2o(dec):
    l = len(str(dec))
    tot = dec
    s = ""
    for i in range(l*2):
        div = int(tot/(8**(l-i)))
        tot = tot%(8**(l-i))
        s += str(div)
    print(s)

# Q4

def py():
    st = "Python rules!"
    st1 = st.split()
    st2 = st.upper()
    st3 = st.find("rules")
    return st1, st2, st3

# Q5






# Q6

# it wiil turn all the oldsubstring into the newsubstring, not only the first one.
def change2(strs):
    strs1 = strs.replace("ten", "ten(10)")
    return strs1

# Q7

# other methods?
def prime1(n):
    list1 = [1]
    for i in range(2, n):
        j = 2
        while (i % j != 0):
            j += 1
        if(j == i):
            list1.append(j)
    return list1
            
# Q8

import os
import os.path

print(os.name)

# return the current working directory (CWD) of the file to execute the code
print(os.getcwd())

path = os.getcwd()

print(os.listdir(path))


# if i only want to print file not including the folders
for f in os.listdir(path):
    if os.path.isfile(os.path.join(path, f)):
        print(f)
# isfile and join belongs to the os.path library
# isfile return true if something inside the parenthesis is an existing regular file.
