# ER 2nd Flexible Calculator

#Create functions for each operation, and have the arg be *nums so when you call the function you do sum(nums)
def sum(*nums):
    total = 0
    for num in nums:
        total+=num
    print(f"\nResult: {total}")

def average(*nums):
    total = 0
    for num in nums:
        total +=num
    total = total/len(nums)
    print(f"\nResult: {total}")

def product(*nums):
    total = 1
    for num in nums:
        total *=num
    print(f"\nResult: {total}")

#print welcome
print("Welcome to the Flexible Calculator!")
#Have the user input asking what caluculation that want to preform
operation = int(input("What operation do you want to preform? (Input the number) \n1. Sum\n2. Average\n3. Max\n4. Min\n5. Product\n6. Exit the program\n"))
#if it = 1, call sum function, etc.
#Have user input for numbers, have it loop until they write done
#add those numbers to a list called nums
print("Type your list of numbers: (Type done when finished)")
nums = []
while True:
    num  = input("Number: ")
    if num == "done":
        break
    if num.isdigit():
        num = int(num)
        nums.append(num)
        continue
    
cont = "yes"

#check which operation was selected, call the function, and ask if they want to do another one. If they do then continue, also stupid proof
while cont == "yes":
    if operation == 1:
        sum(*nums)
        cont = input("Would you like to preform another calculation? (yes/no) ").lower().strip()
        operation = int(input("What operation do you want to preform? (Input the number) \n1. Sum\n2. Average\n3. Max\n4. Min\n5. Product\n6. Exit the program\n"))
        continue
    if operation == 2:
        average(*nums)
        cont = input("Would you like to preform another calculation? (yes/no) ").lower().strip()
        operation = int(input("What operation do you want to preform? (Input the number) \n1. Sum\n2. Average\n3. Max\n4. Min\n5. Product\n6. Exit the program\n"))
        continue
    if operation == 3:
        result = max(nums)
        print(f"\nResult: {result}")
        cont = input("Would you like to preform another calculation? (yes/no) ").lower().strip()
        operation = int(input("What operation do you want to preform? (Input the number) \n1. Sum\n2. Average\n3. Max\n4. Min\n5. Product\n6. Exit the program\n"))
        continue
    if operation == 4:
        result = min(nums)
        print(f"\nResult: {result}")
        cont = input("Would you like to preform another calculation? (yes/no) ").lower().strip()
        operation = int(input("What operation do you want to preform? (Input the number) \n1. Sum\n2. Average\n3. Max\n4. Min\n5. Product\n6. Exit the program\n"))
        continue
    if operation == 5:
        product(*nums)
        cont = input("Would you like to preform another calculation? (yes/no) ").lower().strip()
        operation = int(input("What operation do you want to preform? (Input the number) \n1. Sum\n2. Average\n3. Max\n4. Min\n5. Product\n6. Exit the program\n"))
        continue
    if operation == 6:
        print("Thank you for using this calculator!")
        break
    else:
        print("Invalid")
        operation = int(input("What operation do you want to preform? (Input the number) \n1. Sum\n2. Average\n3. Max\n4. Min\n5. Product\n6. Exit the program"))
        continue