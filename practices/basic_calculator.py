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

print(f"{num1}+{num2}={eq1}\n{num1}-{num2}={eq2}\n{num1}*{num2}={eq3}\n{num1}^{num2}={eq4}\n{num1}%{num2}={eq5}\n{num1}/{num2}={eq6:.2f}\n{num1}//{num2}={eq7}")