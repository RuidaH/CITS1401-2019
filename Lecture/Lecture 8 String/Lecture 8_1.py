# Abbreviation of special names.
"""
names of species are abbriviated to the first 3 letter of the fisrt part and
  2 letters of the second part
"""
def bioin(first, last):
    abr = first[:3] + last[:2]
    return abr.upper()

# when you enter a full name such as "doctor mubashar", you need to split it out first
def bioin(fullname):
    fn = fullname.split()
    first = fn[0]
    last = fn[1]
    abr = first[:3] + last[:2]
    return abr.upper()

def encode(msg):         # turning the string to number
    coded_message = ""   # it is an empty string, nothing in it
    for c in msg:
        code = ord(c)    # ord() is turning the character into the corresponding number
        coded_message = coded_message + str(code) + " "
    return coded_message

# this time msg is the sequence and numbers as a string
def decode(msg):          # turning back the number to the string again
    decoded_message = ""
    msg_sp = msg.split()    # since the number all stick together, we need to split out of them.(split the string into a sequence of small strings/digits)
    for asc in msg_sp:
        ch = chr(int(asc))                  # since the characters in the string is the type of str, so we need to convert the str into int.(change the digits into the number they represent
        decoded_message = decoded_message + ch    # you dont need to add " " since you are turning the number back to the string
    return decoded_message