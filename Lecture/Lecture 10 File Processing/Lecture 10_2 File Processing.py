
def read1():
    # just an operation to open the file, set a variable to link the file
    f = open("readName.txt","r")

    print(f.read())
    print(type(f.read()))

    # you need to close the file after you have used it.
    f.close()


def readline2():
    
    f = open("readName.txt","r")
    
    print("File opened")
    
    for line in f:
        
        print(line)    # The reason why there are extra lines between two line in the file is because print means next line
                       # (接上一行)and plus "\n", so it will get 2 new line
    
    f.close()
    
    # print("File closed")
    
    
def readline3():
    
    f = open("readName.txt","r")
    
    print("File opened")
    
    for line in f:
        
        print(line, end = "")    # This can sovle the "new line" problem in f2()
    
    f.close()
    
    print("File closed")
    
    
def readline4():
    
    f = open("readName.txt","r")
    
    print("File opened")
    
    lno = 1
    
    for line in f:
        
        # print(line[:-1])       this is the first method
        print(line, end = "Line" + str(lno) + ":")     # this is the second method
        
        lno += 1
    
    f.close()
    
    print("File closed")
    
    
def readlines5():
    
    f = open("readName.txt","r")
    
    print(f.readlines())
    # This would print a list, every elements in the list is a line in the file
    # (接上一行/take the previous line)and "\n" is literrally showed in the elements
    
    f.close()


def write1():
    
    f = open("readName.txt", "w")
    
    msg = "This is the new content of the file\nWhen you use w operation, all the original content would be deleted"
    
    f.write(msg)
    
    f.close()
    
def append1():
    
    f = open("readName.txt", "a")
    
    msg1 = "\nwhen you use append operation, the original text would not be lost"
    
    f.write(msg1)
    
    f.close()
    
# 引用一个表格以另外的形式填充另一个表格
def quote():
    
    fileName = "names.txt"
    
    fread = open("names.txt", "r")     # You got information in this file
    
    fwrite = open("names1.txt","a")
    
    for name in fread:                 # the name in the loop is the line of the file
        
        flname = name.split()          # You need to seperate the name
        
        uname = flname[0][0] + flname[1] + "\n"
        
        fwrite.write(uname)
        
    fread.close()
    
    fwrite.close()
        
def read11():
    
    f = open("names1.txt", "r")
    
    print(f.read())
    
    f.close()


    