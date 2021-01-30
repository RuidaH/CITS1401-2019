"""this program is demostrating choatic function
it is wriiten during the week 2"""
 
def choatic():
    print("this is choatic fuction")
    x = float(input("please enter a value between 0 and 1:"))
    for i in range(0,10,2):  #not to 10
        x = 3.9 * x * (1-x)    #assignment
        print("the value of i variable is ",i)
        print("the value :", x)

choatic()    #you do not have to type the function in the statement shell again


#Another Note
print("hello")      #The content inside the "" is not gonna changed
print("sleepy")
print("4+5")
print(4+5)
print("3+4=",3+4)   #it is quite normal that there is a space bar due to the comma
print(3, 4, 3 + 4)