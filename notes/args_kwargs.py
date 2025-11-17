#ER 2nd ARGS AND KWARGS NOTES

"""def hello(name, age):
    return f"Hello {name}! You are {age}!"

print(hello("Treyson", 19))
print(hello(age = 19, name = "Treyson"))"""


"""def hello(name = "Tia", age = 29):
    return f"Hello {name}! You are {age}!"

print(hello())
print(hello("Xavier"))
print(hello(age = 19, name = "Treyson"))"""

"""def hello(last, *names, vlast): #star puts them in a tuple, this is also positional
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last} {vlast}")
        else:
            print(f"Hello {name} {last}")

hello("LaRose", "Alex", "Katie", "Andrew", "Vienna", "Tia", "Xavier", "Jake", "Treyson", vlast = "Atkin")"""


#positional arguments, *args, keywork arguments, **kwargs
def hello(*names, **last):
    print(last)
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last['alast']} {last['vlast']}")
        else:
            print(f"Hello {name} {last['alast']}")

hello("LaRose", "Alex", "Katie", "Andrew", "Vienna", "Tia", "Xavier", "Jake", "Treyson", alast = "LaRose", vlast = "Atkin")