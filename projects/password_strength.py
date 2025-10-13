#ER 2nd Password strength checker

#Set strength = 4
strength = 4
#set list or special characters
specials = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",".","<",">","?"]
#Ask user for their password (input)
password = input("Please input your password: ")
#Find length of password using len
length = len(password)
#If it is <8
if length <8:
#Strength -=1
    print("You need to make your password longer")
    strength -=1
#find an int
number = any(char.isdigit() for char in password )
#if no number
if number != True:
# take away from strength
    strength -=1
    print("You need to have a number in your password")
#Find uppercase
uppercase = any(char.isupper() for char in password )
#If no uppercase 
if uppercase != True:
#strength-=1
    strength -=1
    print("You need to have an uppercase in your password")
#Find lowercase
lowercase = any(char.islower() for char in password )
#If no lowercase
if lowercase != True:
#Strength -=1
    strength -=1
    print("You need to have a lowercase in your password")
#If you can find !@#$%^&*()_+-=[]{}|;:,.<>? 
for x in specials:
    password.find(x)
    if x in password:
#Strength +=1
        strength +=1
        break
#else need to add
else:
    print("You need to add special characters")

#Display password strength
print(f"Your password strength is {strength}/5")
#Print out strength statement for whatever value you end up with
if strength == 5:
    print("That is very strong!")
elif strength == 4:
    print("That is strong!")
elif strength == 3:
    print("That is moderate.")
elif strength <= 2:
    print("That is weak!")