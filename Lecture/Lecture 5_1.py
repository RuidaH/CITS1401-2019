# Lecture 5 Math Module



# Concept
# Control Structure : for loops alter the flow of program execution
# A library : a module with some definitions or functions



# The software development process (Sofeware life cycle)
"""
1. Analyse the problem
2. Determine the specification
3. Create a design
4. Implement the design i.e. write the program
5. Test / Debug the program
6. Maintain the program
"""



#if you import the module, all the function in the module is avialable for you.
#math.(+tab) -> you can see the the function in the math library
#you need to import again after the %Reset (it means stops)

import math             # not maths
# import math as m       So you can use the m.sqrt(9), which is more convenient

def quadratic(a, b, c):
    
    

    """
    a = float(input("Please enter coefficient a: "))
    b = float(input("Please enter coefficient b: "))
    c = float(input("Please enter coefficient c: "))
    """

    check = b*b - 4*a*c
    if check < 0 :
        res = "The roots are complex."
        print("The roots are complex.")
        return None, None       # nothing to return 

#if check >= 0 :
    elif check == 0 :
        root = -b / (2*a)
        res = "There are repeated roots"
        print("There are repeated two roots at: ", root)
        return root, root
    
    else :
        root1 = (-b + math.sqrt(check)) / (2*a)
        root2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
        res = "There are two different roots"
        print("The roots are:\n",root1, "and", root2)
        return root1, root2
    # return res


a = 1
b = 2
c = 1
r1, r2 = quadratic(a,b,c)
print("the root are:",r1, r2)