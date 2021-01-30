def hi():    #: is vital
    print("welcome!")    #indented block
    print("fun")   #indentation means belonging to the function(缩进） 
    
print("the end")    #it is one the part of the function

def c2f():     #can be used many times
    
    hi()
    hello("kao")      #don't have import
    C = int(input("Please input the temperature in Celsius:"))
    Cint = float(C)

    F = ( 9 / 5 ) * Cint + 32
    if F < 80 and F > 40 :
        print("It is a great weather")
    else :
        print("It is too hot or too cold")
    print("The temperature in Farenheit is:",F)
    
def hello(course):      #hello expect to a value(eg:"cit1401")
    print("welcome to", course)
    print("fun")
    
#the benefit: it is convenient to debug
#the model can not be import entirely???
    
c2f() #we can use it directly