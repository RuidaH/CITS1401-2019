# student Name: Ruida He
# student ID: 22762872

import math as m
import os


def main(text_file1, text_file2, feature):
    
    
    # check if the file 1 and the file 2 exist or not
    
    if not os.path.isfile(text_file1):
        
        print("The first file you input does not exist, please try again!")
        
        return None, None, None
    
    if not os.path.isfile(text_file2):
        
        print("The second file you input does not exist, please try again!")
        
        return None, None, None
    
    
    
    feature.lower()
    
    
    
    if feature == "composite":
        
        profile_1 = Composite(text_file1)
        
        profile_2 = Composite(text_file2)
        
        dis = Distance(text_file1, text_file2, feature)
        
        return dis, profile_1, profile_2
        
    elif feature == "punctuation":
        
        profile_1 = Punctuation(text_file1)
        
        profile_2 = Punctuation(text_file2)
        
        dis = Distance(text_file1, text_file2, feature)
        
        return dis, profile_1, profile_2
        
    elif feature == "conjunction":
        
        profile_1 = Conjunction(text_file1)
        
        profile_2 = Conjunction(text_file2)
        
        dis = Distance(text_file1, text_file2, feature)
        
        return dis, profile_1, profile_2
    
    elif feature == "unigrams":
        
        profile_1 = Unigrams(text_file1)
        
        profile_2 = Unigrams(text_file2)
        
        dis = Distance(text_file1, text_file2, feature)
        
        return dis, profile_1, profile_2
    
    else:
        
        print("The feature you input is not meeting our need, please try again!")
        
        return None, None, None
        
        

# read the file and make all the letter in the file lowercase 
def Read_file(text_file):
    
    file_text = open(text_file)
    
    file_read = file_text.read()
    file_read = file_read.lower()
    
    # file_read is a string
    return file_read     




# Get the list only containing the words of the file （eliminating the punctuations or identifiers)
def Only_words(text_file):
    
    file_read = Read_file(text_file)
    
    file_read = file_read.replace("--", " ")
    
    chlist = list(range(128))
    del chlist[97:123]
    del chlist[39]
    del chlist[44]
    # I want to delete ASCII code of aingle quote, since I have already deleted 39 ("'"), I just use 44 (45 - 1)
    
    changed_file = ""
    
    # replace all the special character which are not lowercase letters, dash and single quote with emptyspace
    for k in chlist:
        file_read = file_read.replace(chr(k), " ")
    
    for i in range(len(file_read)):
        
        flag = False
        
        if file_read[i] == "'":
            
            check_1 = ord(file_read[i+1])
            check_2 = ord(file_read[i-1])
            
            if  check_1 <= 96 or check_1 >= 123 or check_2 <= 96 or check_2 >= 123:
                flag = True
                
            if flag == False:
                changed_file += file_read[i]
                
        else:
            
            changed_file += file_read[i]
    
    flist = changed_file.split()
    
    return flist   
    




def Conjunction(text_file):
    
    dic = {"also":0, "although":0, "and":0, "as":0, "because":0,
           "before":0, "but":0, "for":0, "if":0, "nor":0, "of":0,
           "or":0,"since":0, "that":0, "though":0, "until":0,
           "when":0, "whenever":0, "whereas":0, "which":0, "while":0,
           "yet":0,}
    
    flist = Only_words(text_file)
    
    for word in flist:
        
        if word in dic:
            
            dic[word] += 1

    return dic





def Punctuation(text_file):
    
    dic = {",":0, ";":0, "-":0, "'":0}
    
    file_read = Read_file(text_file)
    
    # Avoid the situation of counting "--"
    
    if "--" in file_read:
        file_read = file_read.replace("--", " ")
    
    apostrophe_Num = 0
    
    # you don't need to consider the situation of file_read[1] and file_read[-1] (' in the letter)
    # since you just need to calculate the number of single quote between the letters.
    for i in range(1, len(file_read)-1):    
        
        if file_read[i] == "'":
            
            check_1 = ord(file_read[i-1])
            check_2 = ord(file_read[i+1])
            
            if check_1 > 96 and check_1 < 123 and check_2 > 96 and check_2 < 123:
                
                apostrophe_Num += 1
                
    dic["'"] = apostrophe_Num

    comma_Num = file_read.count(",")
    dic[","] = comma_Num
    
    semicolon_Num = file_read.count(";")
    dic[";"] = semicolon_Num
    
    dash_Num = file_read.count("-")
    dic["-"] = dash_Num
    
    return dic
  
  
  
  
# just use Only_words function directly
def Unigrams(text_file):
    
    dic = {}
    
    flist = Only_words(text_file)
    
    for word in flist:
        
        dic[word] = dic.get(word, 0) + 1

    return dic



def Composite(text_file):
    
    dic = Conjunction(text_file)
    dic1 = Punctuation(text_file)
    dic.update(dic1)
    
    fread = Read_file(text_file)
    
    words_dic = Unigrams(text_file)
    words = sum(list(words_dic.values()))     
  
    sentences = fread.count(". ") + fread.count("? ") + fread.count("! ")
    sentences = sentences + fread.count(".\n") + fread.count("?\n") + fread.count("!\n")
    sentences = sentences + fread.count(".\t") + fread.count("?\t") + fread.count("!\t")
    sentences = sentences + fread.count(".\'") + fread.count("?\'") + fread.count("!\'")
    sentences = sentences + fread.count(".\"") + fread.count("?\"") + fread.count("!\"")
    
    paragraphs = fread.count("\n\n") + 1
    
    dic["words_per_sentence"] = round(words / sentences, 4)
    dic["sentences_per_par"] = round(sentences / paragraphs, 4)
    
    return dic
    
  
def Distance(text_file1, text_file2, feature):
    
    dis = 0
    
    if feature == "composite":
        
        profile_1 = Composite(text_file1)
        profile_2 = Composite(text_file2)
        
        for word in profile_1:
            
            dis += (profile_1[word] - profile_2[word]) ** 2
            
        dis = m.sqrt(dis)
        
        return round(dis, 4)
    
    elif feature == "punctuation":
        
        profile_1 = Punctuation(text_file1)
        profile_2 = Punctuation(text_file2)
        
        for word in profile_1:
            
            dis += (profile_1[word] - profile_2[word]) ** 2
            
        dis = m.sqrt(dis)
        
        return round(dis, 4)
    
    elif feature == "conjunction":
        
        profile_1 = Conjunction(text_file1)
        profile_2 = Conjunction(text_file2)
        
        for word in profile_1:
            
            dis += (profile_1[word] - profile_2[word]) ** 2
            
        dis = m.sqrt(dis)
        
        return round(dis, 4)
    
    elif feature == "unigrams":
        
        profile_1 = Unigrams(text_file1)
        profile_2 = Unigrams(text_file2)
        
        for word in profile_1:
                  
            # Sum = profile_1[word] 
            
            if profile_2.get(word, 0) != 0:
                
                dis += (profile_1[word] - profile_2[word]) ** 2
                
                # remember you delete sth in dictionary here, pay attention to the return in the main function
                del profile_2[word]         
            
            else:
                
                dis += profile_1[word] ** 2
                
        # go through the character only existing in the profile_2         
        for words in profile_2:
            
            dis += profile_2[words] ** 2
            
        dis = m.sqrt(dis)
        
        return round(dis, 4)
            


