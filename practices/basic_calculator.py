#ER 2nd Basic Calculator

num1 = int(input("Type in a whole number: "))
num2 = int(input("Type in another whole number: "))

eq1 = num1+num2
eq2 = num1-num2
eq3 = num1*num2
eq4 = num1**num2
eq5 = num1%num2
eq6 = num1/num2
eq7 = num1//num2

print(f"\n\nEquation 1: {num1}+{num2}={eq1:.2f}\n\nEquation 2: {num1}-{num2}={eq2:.2f}\n\nEquation 3: {num1}*{num2}={eq3:.2f}\n\nEquation 4: {num1}^{num2}={eq4:.2f}\n\nEquation 5: {num1}%{num2}={eq5:.2f}\n\nEquation 6: {num1}/{num2}={eq6:.2f}\n\nEquation 7: {num1}//{num2}={eq7:.2f}")