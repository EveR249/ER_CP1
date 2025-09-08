#ER 2nd FORMATTING OUTPUTS NOTES

name = "Jake"
age = 21
grade = .75
money = 25

print("hello {}, nice to meet you! You are {:b}, that is really old! You have a {:%} in this class. You have ${:.2f}, that is a lot of money!".format (name, age, grade, money))

print(f"hello {name}, nice to meet you! You are {age:b}, that is really old! You have a {grade:%} in this class. You have ${money:.2f}, that is a lot of money!")