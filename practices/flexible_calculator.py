# ER 2nd Flexible Calculator

#Create functions for each operation, and have the arg be *nums so when you call the function you do sum(nums)
def sum(*nums):
    total = 0
    for num in nums:
        total+=num
    print(f"Result: {total}")

def average(*nums):
    total = 1
    for num in nums:
        total *=num
    print(f"Result: {total}")

#print welcome
print("Welcome to the Flexible Calculator!")
#Have the user input asking what caluculation that want to preform
operation = int(input("What operation do you want to preform? (Input the number) \n1. Sum\n2. Average\n3. Max\n4. Min\n5. Product"))
#if it = 1, call sum function, etc.
#Have user input for numbers, have it loop until they write done
while True:
    num  = int(input("Number: "))
    #add those numbers to a list called nums
    nums = []
    if num == int:
        nums.append(num)
    else:
        break
