#ER 2nd Caesar Cypher

#create encoding function
def encode():
    #get the message you want to code
    message = input("What message would you like to encode? ").upper().strip()
    #input how far they want to shift
    shift = int(input("How far do you want to shift? "))
    #for every character in code switch to numbers
    for char in message:
        char = ord(char)
        #add shift to the number value assigned to each letter
        new = char + shift
    #if number is greater than z restart back at a
        if new > 90:
            new -=26
    #turn adjusted numbers back into letters suing a for loop
        letter = chr(new)
    #code = adjustedcode
        print(letter)
    #return code
    return 
#create decoding function
    #get the coded message
    #for every character turn it into numbers
    #get how far it was shifted
    #subtract how far it shifted from all the numbers
    #make it go right from a to z
    #Turn back into letters using a for loop
    #newmessage = adjustedcode
    #return newmessage

#while true
#ask if they want to do option 1 encode option 2 decode and call the appropriate function or option 3 exit
#If that gives the functions and the else breaks

print(f"{encode()}")