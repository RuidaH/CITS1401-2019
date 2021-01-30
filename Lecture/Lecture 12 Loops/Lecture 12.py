def forloop(lst):
    s = 0
    for element in lst:
        print(element)
        s += element
        print("Sum till this element is", s)
    print("The grand total of all elements of the list is",s)
    
    
def whileloop(lst):
    s = 0
    l = len(lst)
    i = 0
    while i < l:
        print(lst[i])
        s += lst[i]
        print("Sum till this element is", s)
        i += 1
    print("The grand total of all elements of the list is",s)
    
    
# Interactive loop
def guessgame():
# This user will guess a secret number
# The program would not stop until you guess the right number
    s = 7
    attempt = 1
    n = int(input("Please guess this secret number between 0 and 10: "))
    while n != s:
        n = int(input("Wrong,please guess this secret number again: "))
        attempt += 1
    print("well done, you guessd it coreectly in", attempt, "tries")



"""
  The first ave is ask whether user want to input a number,
and then to input a number. after executing, the program would ask if user want to input again.
"""
def ave():
    print("This program will require user to enter numbers and find the average.")
    count = 0
    s = 0
    n = input("Do you want to enter a number: ")
    while n[0] == "y" or n[0] == "Y":
        num = float(input("Please enter the number: "))
        count += 1
        s += num
        n = input("Do you want to enter a number: ")
    print("The total of number you enter is", s, "and average is", s/count)


# sentinel loop
# sentinel loop save a step to check whether user want to input or not
def ave1():
    print("This program will require user to enter numbers and find the average.")
    count = 0
    s = 0
    num = float(input("Please enter the number: "))
    while num >= 0:
        count += 1
        s += num
        num = float(input("Please enter the number: "))
    print("The total of number you enter is", s, "and average is", s/count)
    
# the sentinel value is ""
def ave2():
    print("This program will require user to enter numbers and find the average.")
    count = 0
    s = 0
    num = input("Please enter the number: ")
    while num :     # it means num != ""
        count += 1
        s += float(num)
        num = input("Please enter the number: ")
    print("The total of number you enter is", s, "and average is", s/count)

# This one would  cuase the error when you want to end the program and input an empty string,
# it would go into the inner loop and float the empty string
def nested():
    count = 0
    s = 0
    line_of_input = " "
    
    while line_of_input != "":
        line_of_input = input("Please enter list of numbers seperated by comma(,): ")
        print(line_of_input)
        # inner loop will come here
        nums = line_of_input.split(",")
        for num in nums:
            s += float(num)
            count += 1
        
    print("the total of all the value is:",s, "and their average is", s/count)


# So the way to deal with that is put the input to the end of the outer loop, and the outer while loop would help us to check the empty string
def nested1():
    count = 0
    s = 0
    line_of_input = input("Please enter list of numbers seperated by comma(,): ")
    
    while line_of_input != "":
        print(line_of_input)
        # inner loop will come here
        nums = line_of_input.split(",")
        for num in nums:
            s += float(num)
            count += 1
        line_of_input = input("Please enter list of numbers seperated by comma(,): ")
        
    print("the total of all the value is:",s, "and their average is", s/count)
    
    
# Rather than having 1 number per input line, have multiple, comma-separated numbers per line
# just tell you you can get the elements in the string in every line
def nested_loop(file_name):
    
    file_read = open(file_name,"r")
    
    s = 0
    
    count = 0
    
    for line in file_read:
        
        for xStr in line.split():
            
            sum += float(xStr)
            
            count += 1
    
    print("just some operation, i just want to try to print the elements in every line, you don't have to execute it")
    