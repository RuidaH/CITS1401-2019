# Name: Ruida He
# Student ID: 22762872


import os    

def main():
    
    
    file_name = input("Enter name of file containing World Happiness computation data : ")
    
    metric = input("Choose metric to be tested from (e.g. min, mean, median, harmonic_mean or their uppercase) : ")
    
    action = input("Choose action to be performed on the data using the specified metric.operation (e.g. list, correlation or their uppercase) : ")
    
    
    # Check whether the file you input exists or not
    if not os.path.isfile(file_name):
        
        print("The named input file does not exist, please try again!")
        
        return None

    
    # To turn the action and metric you input into lowercase
    action = action.lower()
    metric = metric.lower()
        
       
    mlst = Normalize(file_name)
    

    if action == "list":
        
        if metric == "min":
            
            mlst1 = Min(mlst)
            
            b = bubble_sort(mlst1)
            
            take_action(b, metric, action)     # print the results
            
        elif metric == "median":
            
            mlst1 = Median(mlst)
            
            b = bubble_sort(mlst1)
            
            take_action(b, metric, action)
            
        elif metric == "mean":
            
            mlst1 = Mean(mlst)
            
            b = bubble_sort(mlst1)
            
            take_action(b, metric, action)
            
        elif metric == "harmonic_mean":
            
            mlst1 = Harmonic_mean(mlst)
            
            b = bubble_sort(mlst1)
            
            take_action(b, metric, action)
            
        else:
            
            print("The metric you input doesn't match, please try again!")
            
            return None
        
        
  
    elif action == "correlation":
        
        if metric == "min":
            
            mlst1 = Min(mlst)
            
            p = Correlation(mlst, mlst1)
            
            take_action(p, metric, action)
            
        elif metric == "median":
            
            mlst1 = Median(mlst)
            
            p = Correlation(mlst, mlst1)
            
            take_action(p, metric, action)
            
        elif metric == "mean":
            
            mlst1 = Mean(mlst)
            
            p = Correlation(mlst, mlst1)
            
            take_action(p, metric, action)
            
        elif metric == "harmonic_mean":
            
            mlst1 = Harmonic_mean(mlst)
            
            p = Correlation(mlst, mlst1)
            
            take_action(p, metric, action)
            
        else:
            
            print("The metric you input doesn't match, please try again!")
            
            return None
    
    
    
    else:
        
        print("The action you input doesn't meet our requirement, please try again!")
        
        return None
    
    

     

        
def Normalize(file_name):
    
    lst = []
    
    file_read = open(file_name, "r")
    
    for line in file_read:       # How can i pass the first line, remove()
        
        fline = line.split(",")
        
        lst.append(fline)
    
    # fisrt we transfer empty elements to None and delete \n
    for k in range(1, len(lst)):
        
        lst[k][-1] = lst[k][-1].strip()
        
        for i in range(1, len(lst[0])):
            
            if lst[k][i] == "":
                
                lst[k][i] = None
            
            else:
            
                lst[k][i] = float(lst[k][i])
    
    # Normalize the list
    for i in range(2, len(lst[0])):
        
        lst_1 = []
            
        for k in range(1, len(lst)):
            
            if lst[k][i] != None:
            
                lst_1.append(lst[k][i])
            
        Max = max(lst_1)
        
        Min = min(lst_1)
        
        for k in range(1, len(lst)):
            
            if lst[k][i] != None:
            
                lst[k][i] = (lst[k][i] - Min) / (Max - Min)

    file_read.close()
    
    return lst






def bubble_sort(lst1):
    
    # sort by size by using bubble sort
    for x in range(len(lst1)):
        
        for y in range(len(lst1) - x - 1):
            
            if lst1[y][2] < lst1[y + 1][2]:
                
                lst1[y], lst1[y + 1] = lst1[y + 1], lst1[y]

    return lst1
    
    


# print the result
def take_action(lst1, metric, action):
    
    if action == "list":
    
        print("\n" + "Ranked list of countries' happiness scores based the", metric, "metric.\n")
    
        for x in range(len(lst1)):
        
            for y in range(len(lst1[x])):
            
                if y == 2:
                
                    print("{0:<0.4f}".format(lst1[x][y]), end = "")
            
                else:
                
                    print("{0:>12s}".format(lst1[x][y]), end = "")
        
    else:
           
        # for the result of correlation, lst1 is just a float number.
        print("\n" + "The correlation coefficient between the study ranking and the ranking using the", metric, "is", lst1)
        
        
        
    


def Min(lst):
    
    lst1 = []
    
    for k in range(1, len(lst)):
        
        lst2 = []                 # get the list without the none type
        lst3 = []                 # store the country name and the mininum
        lst3.append(lst[k][0])
        lst3.append(" ")
        
        # Use a loop to avoid the None
        for i in range(2, len(lst[0])):
            
            if lst[k][i] != None:
                
                lst2.append(lst[k][i])
        
        Min = min(lst2)
        
        lst3.append(Min)
        
        lst3.append("\n")
        
        lst1.append(lst3)
        
    return lst1



def Median(lst):
    
    lst1 = []

    for k in range(1, len(lst)):
        
        lst2 = []                 # get the median number of every row
        
        lst3 = []                 # store the counrty name and the median number correspondingly
        
        lst3.append(lst[k][0])
        
        lst3.append(" ")          # offer a blankspaces between the country name and the median value
        
        for i in range(2, len(lst[0])):
            
            if lst[k][i] != None:
                
                lst2.append(lst[k][i])
                
        lst2.sort()
        
        if len(lst2) % 2 == 0:
        
            Median = (lst2[int((len(lst2) - 2) / 2)] + lst2[int(len(lst2) / 2)]) / 2
        
        else:
            
            Median = lst2[int((len(lst2) - 1) / 2)]
        
        lst3.append(Median)
        
        lst3.append("\n")
        
        lst1.append(lst3)

    return lst1   
    




def Mean(lst):
    
    lst1 = []
    
    for k in range(1, len(lst)):
        
        lst2 = []                     # store the country name and the mean number correspondingly
        
        s = 0
        count = 0
        
        lst2.append(lst[k][0])     
        lst2.append(" ")              # offer a blankspaces between the country name and the median value
        
        for i in range(2, len(lst[0])):
            
            if lst[k][i] != None:
                
                s += lst[k][i]
                
                count += 1
        
        lst2.append(s/count)
        
        lst2.append("\n")
        
        lst1.append(lst2)
        
    return lst1





def Harmonic_mean(lst):
    
    lst1 = []
    
    
    for k in range(1, len(lst)):
        
        lst2 = []
        
        s = 0
        count = 0
        
        lst2.append(lst[k][0])
        lst2.append(" ")
        
        for i in range(2, len(lst[0])):
            
            if lst[k][i] != None and lst[k][i] != 0:     # Avoid the zero and None type
                
                s += 1 / lst[k][i]
                
                count += 1
                
        lst2.append(count/s)
        
        lst2.append("\n")
        
        lst1.append(lst2)
        
    return lst1






def Correlation(lst, lst1):
    
    # The study ranking is lst[k][1]
    # The other ranking is lst1[k][2]
    
    rlst = []                             # Store the study ranking, sort and reverse
    
    rlst1 = []                            # store the sorted ranking
    
    for k in range(1, len(lst)):
        
        rlst.append(lst[k][1])
        
        rlst1.append(lst[k][1])
    
    rlst1.sort()
    
    rlst1.reverse()
    
    # Get the d
    
    for i in range(len(rlst)):
        
        for x in range(len(rlst1)):
            
            if rlst[i] == rlst1[x]:
                
                rlst[i] = x + 1           # The study ranks are in the rlst
                
                break
            
    # execute the same operation for the other ranking
    
    rlst2 = []
    
    rlst3 = []                            # store the lsit after the sorting and reversing
    
    for k in range(len(lst1)):
        
        rlst2.append(lst1[k][2])
        
        rlst3.append(lst1[k][2])
    
    rlst3.sort()
    
    rlst3.reverse() 
        
    for i in range(len(rlst2)):
        
        for x in range(len(rlst3)):
            
            if rlst2[i] == rlst3[x]:
                
                rlst2[i] = x + 1           # The study ranks are in the rlst2
                
                break
    
    # Obtain the correlation
    
    n = len(rlst)
    
    dsum = 0
    
    for x in range(n):
        
        square_d = (rlst[x] - rlst2[x]) ** 2
        
        dsum += square_d
        
    p = 1 - ((6 * dsum) / (n * (n ** 2 - 1)))
    
    return round(p, 4)
        

    