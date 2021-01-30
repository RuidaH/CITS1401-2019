import math as m

def material_cost(r):
    Sphere = 4 * m.pi * (r**2)
    return Sphere

def sum(N) :
    sum = 0
    for i in range(1, N+1) :
        if i % 2 == 0 or i % 3 == 0 :
            sum += i
    return(sum)

def population_growth(ininum, rate, hours_to_achieve, total_hours):
    total_population = ininum * rate ** (total_hours / hours_to_achieve)
    return total_population

def investment(amount, rate):
    double_amount = amount
    year = 0
    while( double_amount / amount < 2):
        year += 1
        double_amount = amount * (1 + rate)**year
    return year
        
def GCD(a, b):
    gcd = 0
    if(a > b):
        while(b != 0):
            c = a % b
            a = b
            b = c
        gcd = a
    else:
        while(a != 0):
            c = b % a
            b = a
            a = c
        gcd = b
    return gcd

# turning a binary number into a decimal number
def decimal(b):
    lens = len(b)
    decimal_num = 0
    for i in range(0,lens):
        decimal_num += int(b[i]) * 2**(lens-i-1)
    return decimal_num
        

#Reduction and Analogy
# to print half an n*n square
def code_segment1(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print("#", end = "")
        print()
        #n -= 1        # it didnt change the first range of range(0, n)


# to print a sideways triangle
# focus on the connection
def code_segment2(n):
    for i in range(0,n+1):
        for j in range(0,i):
            print('#', end = "")
        print()
    for i in range(0,n+1):
        for j in range(0,n-i-1):
            print('#', end = "")
        print()

def rice_figure():
    b = []
    print("1 for YES, 0 for NO\n")
    b.append(input("Did you use extra nitrogen-based fertiliser? (y/n): ")) 
    b.append(input("Did you use extra phosphate-based fertiliser? (y/n): "))
    b.append(input("Did you allow early flooding of the field? (y/n): "))
    b.append(input("Was the field left fallow (empty) the previous season? (y/n): "))
    b.append(input("Did you harvest early? (y/n): "))
    b.append(input("Did you drain the field before harvest? (y/n): "))
    b.append(input("Were the grains dried in the sun before delivery? (y/n): "))
    b.append(input("Did you use the more expensive new variety? (y/n): "))
    lens = len(b)
    decimal_num = 0
    for i in range(0,lens):
        decimal_num += int(b[i]) * 2**(i)
    return decimal_num
    
