def listchange(lst, val):
    # lst = lst + ["been through the function"]
    lst.append("been through the function")
    val = val + 100
    
def main():
    lst2 = [1,2,3,4,5,"hello","just created teh list"]
    i = 222
    listchange(lst2, i)
    print(lst2)
    print(i)

# single value hasn't been changed

# when you want to use list, l = l.copy

# that should not be the list of the list, inside the list no copy, the list would change