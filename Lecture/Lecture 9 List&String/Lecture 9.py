def encode(msg):
    encoded_msg = ""
    for i in msg:               # the loop is to show the i character in the string
        #code = ord(msg[i])
        code = ord(i)      
        encoded_msg = encoded_msg + str(code) + " "
    return encoded_msg

def decode(msg):
    decoded_msg = ""
    msg_sp = msg.split()        # msg_sp is the list  # store the splited string into a new address
    for j in msg_sp:
        code = chr(int(j))
        decoded_msg = decoded_msg + code
    return decoded_msg

def decode1(msg):
    #decoded_msg = ""
    char = []
    msg_sp = msg.split()        # msg_sp is the list  # store the splited string into a new address
    for j in msg_sp:
        code = chr(int(j))
        char.append(code)
    decoded_msg = "".join(char)  # join with empty string seperator
    return decoded_msg



# string is the sequence of the collectors


# when you are using the string
# One weakness is that i cannot have the entire name of the months
def num_turn_into_month(n):
    string_month = "JanFebMarAprMayJunJulAugSepOctNovDec"
    post = (n-1) * 3
    return string_month[post:post+3]
   
