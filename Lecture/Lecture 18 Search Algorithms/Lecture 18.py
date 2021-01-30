# Linear search
def search(n, lst):
    for i in range(len(lst)):
        if lst[i] == n:
            return i
    return None

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
