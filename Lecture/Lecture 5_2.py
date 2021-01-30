def fact():
    n = int(input("Please enter a positive number: "))
    f = 1 
    for i in range(n, 1, -1):
        f = f * i
    print("The factorial of", n, "is : ", f)
    
fact()

"""for i in range(n):
        f = f * (i + 1)"""
"""for i in range(1, n + 1):
        f = f * i      """



"""
range(start, n) returns start, start + 1,...,n-1
"""
print("\nThe example of range1")
a = list(range(1, 11))
print(a)



"""
range(start, n, step) returns that start, start + step,...,stopping before n
"""
print("\nThe example of range2")
b = list(range(1, 11, 2))
print(b)

print("\nThe example of range3")
c = list(range(11, 1, -1))        #the number would never reach 1
print(c)
