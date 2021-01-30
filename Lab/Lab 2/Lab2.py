def factorial():
    a = int(input("Please input the factorial number: "))
    f = 1
    for i in range(a, 1, -1):
        f = f * i
    print("The result is: ", f)
    

# factorial()


"""
import math as m

q = float(input("Please input a float number: "))
s = m.sqrt(q)
print("The root of", q, "is:", s)
"""


"""
# A program to compute the value of an investment
# carried 10 years into the future
# Author: Michael J Wise.
def main():
    investment = int(input("The future years of an investment:"))
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    for i in range(1, investment+1):
        principal *= (1 + apr)
    print ("The value in 10 years is:", principal)
    
main()
"""

print("hidh",end='')
print("jjjj")

def he(N) :
    if(type(N).__name__ == "int") :
        for i in range(1, N+1):
            if(i % 5 != 0 and i % 2 != 0) :
                print("The result:", i)
    else:
        print("The input must be an integer.")

he(10)

def float_checker(N):
    try:
        for i in range(1, N+1):
            if(i % 5 != 0 and i % 2 != 0) :
                print("The result:", i)
    except:
        print("The input must be an integer.")
        
#float_checker(10)