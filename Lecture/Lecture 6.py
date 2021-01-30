# Lecture 6 : Decisions



# objectives of this lecture
"""
1. conditional statement/decision
2. comparison operators
3. logical operators
"""



# Concepts
# Truth table(T,F...)
# Pattern / Software Design Pattern : A recurring and reusable generalised set of instructions
# Nesting : put one compound statement inside of another.
# Math domain error : the domain of the number is bigger or smaller.
# Run-time error : errors happened during the process(运行时错误）
# Anti-bugging : before process some data have tests to ensure procedures will be safe(bying using decision structure for now)
# Decision structure : if / elif / else


"""
The condition of " if " is a boolean expression,i.e.evaluates to the values TRUE or FALSE.
"""



# Comparison operators
"""
< less than
<= less than or equal to
== equal to                # You need to pay attention to this common mistake with the =(indicate assignment)
>= greater than or equal to
> greater than
!= not equal to
"""



# Forming comparisons
"""
When comparing strings, the ordering is lexicographic, meaning that the strings are sorted based on the underlying unicode.
1. ASCII / Unicode is a way of representing characters as integers
2. Because of this, all upper-case latin latters come before lower-case letters.
"""

print("The example of forming comparisons")
print("Adam" < "Zill","because A < Z")
print("Adam" < "adam","because A < a")
print("Adam" > "Abba","because d > b, it just keep comparing until the last letter when the first letters are the same")
print("A" == 65)    #you cannot do this.



# Logical/boolean operators
"""
not : an unary operator, meaning that it operates on a single operation
or
and
"""
a = 1
b = 3
print("\nThe example of the logical operators")
print(a > 0 and a < 4)
print(b > 2 or b < 5)
print(not(a > 0 and a < 4))


# The means of the "if","elif","else"
# "\n" is entering to the next row
print("\nThe example of how to use if/elif/else")
import math    # Make the math library available

a = float(input("Please enter coefficient a: "))
b = float(input("Please enter coefficient b: "))
c = float(input("Please enter coefficient c: "))

# 1. The first methos is to check if the "check" is 0
# 2. The second methods is to check if root1 equals to roots2

check = b*b - 4*a*c       # it is better use a check to represent b*b - 4*a*c because you can more eassier change the error when this is wrong.
if check < 0 :
    print("The roots are complex.")

#if check >= 0 :
elif check == 0 :
    root = -b / (2*a)
    print("There are repeated two roots at: ", root)
    
else :                    # The final else is optional, you can use elif to replace this else
    root1 = (-b + math.sqrt(check)) / (2*a)
    root2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
    print("The roots are:\n",root1, "and", root2)

