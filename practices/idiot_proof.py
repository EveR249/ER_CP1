#ER 2nd Idiot proofing 

name = input("What is your full name? ").title().strip()
phone = input("what is your phone number? ").replace("-", " ").replace(","," ").strip()
gpa = float(input("What is your GPA? ").strip())

print(f"{name}'s phone number is {phone} and their GPA is {gpa:.1f}")