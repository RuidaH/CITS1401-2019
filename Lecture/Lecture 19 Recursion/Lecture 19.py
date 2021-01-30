def fact(n):
    if n == 1:     # the base case
        return 1
    else:
        return n * fact(n-1)
    

# Binary search
def bsearch(n, lst):
    low = 0
    high = len(lst) - 1
    
    while high >= low:
        mid = (high + low) // 2    # mid need to be integer
        if lst[mid] == n:
            return mid
        elif lst[mid] > n:
            high = mid - 1
        elif lst[mid] < n:
            low = mid + 1
    return None

# recusion for binary search
def recBiSearch(n, lst, low, high):
    
    mid = (high + low) // 2
    
    if high < low:
        return None
    elif lst[mid] == n:
        return mid
    elif lst[mid] < n:
        return recBiSearch(n, lst, mid + 1, high)
    else:
        return recBiSearch(n, lst, low, high - 1)
    
# we can then call the binary search with a generic search wrapping function
def search(n, lst):
    return recBiSearch(n, lst, 0, len(lst) - 1)


def recPower(a, n):
    
    if n == 0:
        return 1
    
    factor = recPower(a, n//2)
    
    if n % 2 == 0:       # n is eve number
        return factor * factor 
    else:                # n is odd number
        return factor * factor * a
        
        
# get the value in the position n
# recursion
def recfibo(n):
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)
    
# iteration
def iterfibo(n):
    pre = 1
    cur = 1
    if n >= 3:
        for i in range(2, n):   # or range(n-2)
            cur, pre = pre + cur, cur
    return cur
    
    
    