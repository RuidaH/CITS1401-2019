
""""
C = 1
while C > -999:
    
    C = input("Please inout the temperature in Celsius:")
    C = float(C)

    F = 9 / 5 * C + 32
    
    if C < -999 or F < -999:   # A loop and a half, at least run one time of the loop
        print("Kindly do not provide ridiculous values")
        break
    
    print("The converted temperature in Farenheit is ", F)
    
print("END OF THE WHILE LOOP")
"""

# 1. Find whather a number is prime or not
def isprime(N):      # Go up to half of the value
    if N < 2:
        return False   # Not a prime number
    elif N < 4:
        return True    # 2, 3 are prime number
    else:
        for i in range(2, N//2+1):   # 7 // 2 = 3, you noly need half of the number
            if N % i == 0:
                return False
        return True
    
    
# 2. Find the list of prime number up to N
def primelist(N):
    if N < 2:
        return []
    elif N == 2:
        return [2]
    else:
        pl = [2,3]
        for num in range(4, N+1):
            if isprime(num):
                pl.append(num)
    return pl

def primelist2(N):
    if N < 2:
        return []
    elif N == 2:
        return [2]
    else:
        pl = [2]
        for num in range(3, N+1, 2):       # all the even numbers are not the prime number
            status = True
            for i in range(2, num//2+1):
                if num % i == 0:
                    status = False
                    break                  # Once you found it is divisible, just break and check the flag and append the list
            if status:
                pl.append(num)
        return pl
    
    
# Find N prime numbers
def Nprimes(N):
    plist = [2,3]
    if N < 1:
        return []
    elif N < 3:
        return plist[:N]
    else:
        num = 5
        while len(plist) < N:
            status = True
            for i in range(2, num//2 + 1):
                if num % i == 0:
                    status = False
                    break       
            if status:
                plist.append(num)
            num += 2    # increment the number by 2
        return plist