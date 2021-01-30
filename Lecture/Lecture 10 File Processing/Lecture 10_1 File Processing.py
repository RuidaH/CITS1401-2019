
"""
# print the odd num
inlist = []
for i in range(6):
    if i%2 == 0:
        inlist.append(i)
    else:
        inlist[-1]+=1
print(inlist)

# it change the type of num
def multable(num):
    print("*******************************")
    for i in range(21):
        print("{0:0d} x {1:2d} = {2:4d}".format(num, i, num*i))
    print("*******************************")
"""   


f = open("readName.txt","r")    # just open the file
print("file opened")
lno = 1
for line in f:
    print(line,end = "line " + str(lno) + ":")       # the \n in the file and the print,so it got 2 new lines
    lno += 1                                        
f.close()                            # [:-1] you can ignore the last character every line, end = "\t"
print("file closed")
    
"""   
print(f.readlines())            # when you use readline, use a loop ,you need to read it again and again,which is inefficient
f.close()                       # the list of the string<-readlines
"""
"""
f2 = open("readName.txt","w")
msg = "this is the python \n this lecture is freaking good!"   # delete all the original file and start again
f2.write(msg)
f2.close()
"""
"""
f2 = open("readName.txt","a")
msg = "this is the python \n this lecture is freaking killing me!"    # appending
f2.write(msg)
f2.close()
"""
"""
f3 = open("name.xlsx","a")
msg = "bob"
#msg1 = "zac"
f3.write(msg)
#f3.write(msg1)
f3.close()
"""

filename = "names.csv"

fread = open(filename,"r")
fwrite = open(login.csv,"w")

for name in fread:
    #print(name)
    flname = name.split(",")
    fname = flname[0]
    lname = flname[1]
    uname = fname[0] + lname
    fwrite.write(uname)

fread.close()
fwrite.close()


