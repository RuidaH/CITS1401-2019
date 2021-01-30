"""
Example: Word Frequency
This is a multi-accumulator problems --- we will likely need hundreds, perhaps thousands of these accumulators
"""



def wordcount():
    
    file = open("test.txt", "r")
    filetxt = file.read()
    
    # get rid of special acculators first
    
    filetxt = filetxt.lower()
    chlist = list(range(128))
    del chlist[97:123]
    
    for c in chlist:
        filetxt = filetxt.replace(chr(c), " ")
    
    # make it list by spliting with the empty space
    flist = filetxt.split()
    
    dic = {}                         # create an empty dictionary
    for word in flist:
        dic[word] = dic.get(word, 0) + 1
        
    for item in dic:
        print(item, dic[item])
    
    return dic
        
    # if you want to sort them as descending sort
    dlist = list(dic.items())      # make it the list containing the tuples
    dlist.sort(key = bycount, reverse = True)
    
    print(dlist)



# to sort the items by frequency, we need a function that will take a tuple (here, 2-tuple) and return the second item, i.e. count
def bycount(t):
    return t[1]

"""
To sort the list by frequency:
    t.sort(key = bycount, reverse = True)
"""

# take second element for sort
def takesecond(elem):
    return elem[1]

# random list
random = [(1,2), (3,4), (5,1),(6,3)]

# sort list with the key
random.sort(key = takesecond)

print("The result is:", random)
    

