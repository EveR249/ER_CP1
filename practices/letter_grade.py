#ER 2nd What is my grade?

grade = float(input("What is your percentage grade? (Don't include the % sign) "))
  
if grade > 100:
    print(f"You have a {grade:.2f}% in the class, which is better than an A!")
elif grade >= 94:
    print(f"You have a {grade:.2f}% in the class, which is an A!")
elif grade >= 90:
    print(f"You have a {grade:.2f}% in the class, which is an A-")
elif grade >= 87:
    print(f"You have a {grade:.2f}% in the class, which is a B+")
elif grade >= 84:
    print(f"You have a {grade:.2f}% in the class, which is a B")
elif grade >= 80:
    print(f"You have a {grade:.2f}% in the class, which is a B-")
elif grade >= 77:
    print(f"You have a {grade:.2f}% in the class, which is a C+")
elif grade >= 74:
    print(f"You have a {grade:.2f}% in the class, which is a C")
elif grade >= 70:
    print(f"You have a {grade:.2f}% in the class, which is a C-")
elif grade >= 67:
    print(f"You have a {grade:.2f}% in the class, which is a D")
elif grade >= 60:
    print(f"You have a {grade:.2f}% in the class, which is a D-")
elif grade >= 0:
    print(f"You have a {grade:.2f}% in the class, which is an F!")
else:
    print("Your grade is less than zero!! That shouldn't even be possible!")   