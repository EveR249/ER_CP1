#ER 2nd Strings methods notes

name = input("What is your name?").strip().title()
#.lower() => makes it all lowercase
#.upper() => makes it all uppercase
#.capitalize => capitalizes the very first letter
#.title => capitalizes first letter of all the words


age = int(input("How old are you?"))

#print("Hello {}, nice to meet you! I cannot believe you are {:2f}".format(name, age))

print(f"Hello {name}, nice to meet you! I cannot believe you are {age:.1f}!")

#print(age.isdigit())

#print("really? " +age+" is old")

sentence = "The quick brown fox jumps over the lazy dog"

word = "brown"
start = sentence.find(word)
length= len(word)

#print(sentence.replace(word, "yellow"))

#print(sentence.find("fox"))