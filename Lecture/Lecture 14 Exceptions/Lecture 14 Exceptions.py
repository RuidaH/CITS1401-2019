

def quadratic(a, b, c):
    
    import math
    

    """
    a = float(input("Please enter coefficient a: "))
    b = float(input("Please enter coefficient b: "))
    c = float(input("Please enter coefficient c: "))
    """
    
    try:
        check = b*b - 4*a*c
    except TypeError:
        print("Please check the inputs. there are not numerical", a,b,c)
        return None, None
        # return     it only return one value, which is None

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
        
        try:
            root1 = (-b + math.sqrt(check)) / (2*a)
            root2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
        except ZeroDivisionError:
            print("Please check the inputs, one of them zero and causing zero division", a,b,c)
            return None, None

        res = "There are two different roots"
        print("The roots are:\n",root1, "and", root2)
        return root1, root2
    # return res


# When you try to inlcude all the function as the body of try
def quadratic1(a, b, c):
    
    import math

    try:
        check = b*b - 4*a*c
        if check < 0 :
            res = "The roots are complex."
            print("The roots are complex.")
            return None, None       # nothing to return 

        elif check == 0 :
            root = -b / (2*a)
            res = "There are repeated roots"
            print("There are repeated two roots at: ", root)
            return root, root
    
        else:
            root1 = (-b + math.sqrt(check)) / (2*a)
            root2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
            res = "There are two different roots"
            print("The roots are:\n",root1, "and", root2)
            return root1, root2
                
    except TypeError:
        print("Please check the inputs. there are not numerical", a,b,c)
        # return None, None
        # return     it only return one value, which is None, but for this function, it would report error.

    except ZeroDivisionError:
        print("Please check the inputs, one of them zero and causing zero division", a,b,c)
        return None, None

    print("This is theedn of the function")

"""
1. Once you have an error, the body of try would stop executing and go into the except, doing the execution inside the except.
2. Even if you do not use return in the except, there is a return which is None for the function
"""
    
    
"""
  There is a real main program in python, and thta is the code thta exists
in the module outside any function or object. and it is called __main__
"""

# if i want to have my own main program and i want to use it
# but you can not import this program to some other softwares, only the functions in this program can be reported, not the content of these
if __name__ == "__main__":
    r1,r2 = quadratic(1,2,1)
    print("this is the way you write your own program. Whatever you run this file, this stuff will be executed")
    
    
# Exceptions handling for the file opening
def test_fileIO(name, mode):
    mode_list = ["r","w","a"]
    if mode not in mode_list:
        print("Unknown file access mode", mode)
        return None
    
    try:
        f = open(name, mode)
    except IOError:
        print("Cannot open the file {0:s}".format(name))
        return None
    
    return f