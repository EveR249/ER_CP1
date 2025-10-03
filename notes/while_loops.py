#ER 2nd while loops notes
import time
import random

#infinite loop
num = 0
break_point = random.randint(1,30)
while num <= 20:
    num +=1
    if num == break_point:
        break
    elif num%2 != 0:
        continue
    print(num)
    time.sleep(0.1)
else:
    print("this loop met the condition")

print("the loop ended")