#ER 2nd Madlibs Practice

#It was a _, cold November day. I woke up to the _ smell of roasting _ in the _ downstairs. I _ down the stairs to see if I could help _ the dinner. My mom said, "See if _ needs a fresh _." So i carried a tray of _ into the _ room. When I got there, I couldn't believe my _! There were _ _ on _!

adjective_nov = input("Type an adjective: ")
adjective_smell = input("Type an adjective: ")
bird = input("Type a kind of bird: ")
room = input("Type a room in a house: ")
verb_past = input("Type a past tense verb: ")
name = input("Type the name of a family member: ")
noun_fresh = input("Type a noun: ")
food = input("Type a food (plural): ")
verb_ing = input("Type a verb ending in -ing: ")
body = input("Type a body part (plural): ")
plural_noun = input("Type a plural noun: ")

madlib = "It was a "+adjective_nov+", cold November day. I woke up to the "+adjective_smell+" smell of roasting "+bird+" in the "+room+" downstairs. I "+verb_past+" down the stairs to see if I could help with the dinner. My mom told me to see if "+name+" needed a fresh "+noun_fresh+" so I carried a tray of "+food+" into the "+verb_ing+" room. When I got there, I couldn't believe my "+body+"! There were "+plural_noun+" "+verb_ing+" on "+name+"!"

print(madlib)