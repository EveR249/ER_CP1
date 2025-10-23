#ER 2nd Caesar Cipher

#create encoding function
def encode():
    #create empty list and string
    letter_list = []
    #get the message you want to code
    message = input("What message would you like to encode? ").strip()
    #input how far they want to shift
    shift = int(input("How far do you want to shift? "))
    #for every character in code switch to numbers
    for char in message:
        char = ord(char)
        #add shift to the number value assigned to each letter
        new = char + shift
    #if number is greater than z restart back at a
        if new > 122:
            new -=26
        if new > 90 and new < 97:
            new -=26
        if new <= 64:
            new = char
    #turn adjusted numbers back into letters
        letter = chr(new)
    #code = adjustedcode
        letter_list.append(letter)
    #return code
        x = ""
        encoded_message = x.join(letter_list)
    return encoded_message

#create decoding function
def decode():
    letter_list = []
    #get the coded message
    message = input("What message would you like to decode? ")
    #get how far it was shifted
    shift = int(input("How far was it shifted? "))
    #for every character turn it into numbers
    for char in message:
        char = ord(char)
    #subtract how far it shifted from all the numbers
        new = char - shift
    #make it go right from a to z
        if new > 122:
            new -=26
        if new > 90 and new < 97:
            new -=26
        if new <= 64:
            new = char
    #Turn back into letters
        letter = chr(new)
    #newmessage = adjustedcode
        letter_list.append(letter)
    #return newmessage
        x = ""
        encoded_message = x.join(letter_list)
    return encoded_message

while True:
#while true
    choice = int(input("What option are you choosing? 1. Encode 2. Decode or 3. Exit  "))
#ask if they want to do option 1 encode option 2 decode and call the appropriate function or option 3 exit
    if choice == 1:
        print(f"{encode()}")
    elif choice == 2:
        print(f"{decode()}")
    else:
        break
#If that gives the functions and the else breaks