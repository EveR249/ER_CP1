#ER 2nd Factorials 

#define function solve_factorial(number)
def solve_factorial(num):
    #set num to number
    #I had to move this part
    #reset total to 1
    total = 1
    #for range(num)
    for i in range(num): #had to add for i in range
        #total x num
        total *= num #had to change format
        #num -1
        num -=1
    #return(number, total)
    return (total) #changed the return

#while loop
while True:
    #while loop
    while True:
        #ask for the users input as a number
        num = input("What number do you want the factorial of? (Whole numbers only)\n")
        number = num #set num to number here instead of in the function
        #if it can be changed to an int and bigger than -1 change it to an int
        if num.isdigit(): #had to move the num > -1 under it
            num = int(num)
            if num > -1:
            #break loop
                break
        #else
        else:
            #ask for them to do it again
            print("Invalid, try again.")

    #number,total become the answer of solve_factorial(number)
    total = solve_factorial(num)
    #write that the factorial of their number is the total
    print(f"The factorial of {number} is {total}")
#ask if they want to quit
    quit = input("Would you like to quit the program? (yes/no)\n").lower().strip()
#if they want to quit
    if quit == "yes":
    #break the loop
        break