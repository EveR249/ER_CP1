#ER 2nd Password strength checker

#Set strength = 5
strength = 5
#set list or special characters
special = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",".","<",">","?"]
#Ask user for their password (input)
password = input("Please input your password: ")
#Find length of password using len
length = len(password)
#If it is <8
if length <8:
#Strength -=1
    print("You need to make your password longer")
    strength -=1
#If you cant find !@#$%^&*()_+-=[]{}|;:,.<>? using find
if password is !(alphanumeric):
#Strength -=1
    print("You need to add special characters")
    strength -=1
#If you cant find an int using find
if int not in password:
#Strength -=1
    print("You need to have a number in your password")
    strength -=1
#For character in password 

#Find uppercase

#If no uppercase 

#strength-=1

#Find lowercase

#If no lowercase

#Strength -=1