from random import randint

number = randint(0, 100000)
digit = number % 10
print(digit)
if digit % 2 == 0:
    print("Number ", number, " is a multiple of 2")
elif digit % 3 == 0:
    print("Number ", number, " is a multiple of 5")
elif digit % 5 == 0:
    print("Number", number, " is a multiple of 5")
else:
    print("Number ", number, " is not a multiple of 2, 3 0r 5")
number2 = 9 % 5
print(number2)