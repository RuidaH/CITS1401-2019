#import C2F   it's not using .py
#C2F.c2f()

#只要有除法都是float
#cint = int(float(c)) if c is string due to the input

print("this is the program to find interest for 10 years")
p = float(input("Please enter the amount you deposit:"))
apr = float(input("please enter annual interest rate:"))

for am in range(10):
    p = p * (1 + apr)
    print("your amount after",am+1,"years is :",p)


print("you have $", p, "in your account")