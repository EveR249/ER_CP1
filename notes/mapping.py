#ER 2nd Mapping notes

numbers = [234,453,56,346,23,5,245,35,632,4,52]
"""divided = []

for num in numbers:
    divided.append(num/2)"""

"""def divide(number):
    return number/2"""

"""divided = list(map(lambda num: num/2, numbers))

for i, num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}")"""

divided = map(lambda num: num/2, numbers)
print(divided)