# n = int(input())
# word = input()
# print(word+word+word+word+word+word+word)
#
# print(n*word)


# print(-10)  # -10
# print(-(100 + 200))  # -300
#
# print(7 % 2)  # 1, because 7 is an odd number
# print(8 % 2)  # 0, because 8 is an even number
#
# # Divide the number by itself
# print(4 % 4)     # 0
# # At least one number is a float
# print(11 % 6.0)  # 5.0
# # The first number is less than the divisor
# print(55 % 77)   # 55
# # With negative numbers, it preserves the divisor sign
# print(-11 % 5)    # 4
# print(11 % -5)    # -4
#
#
# print(10 ** 2)  # 100
#
# print(((3 + 5) // 2 * 2 ** 3) % 7)

# better code
# Yes: easy to match operators with operands
# income = (gross_wages
#           + taxable_interest
#           + (dividends - qualified_dividends)
#           - ira_deduction
#           - student_loan_interest)

# a = True
# b = False
#
# not a or b
#
# (a or b) and not (a and b)
#
# (a and b) or not (a or b)
#
# (a and not b) or (not a and b)
#
# a and not b



# #---------------
#
# # the average amount of money per month
# money = int(input("How much money do you spend per month: "))
#
# # the number of miles per piece of money
# n_miles = 2
#
# # earned miles
# miles_per_month = money * n_miles
#
# # the distance between London and Paris
# distance = 215
#
# # how many months do you need to get
# # a free trip from London to Paris and back
# print(distance * 2 / miles_per_month)


# # ----------------------
# pasta = "tomato, basil, garlic, salt, pasta, olive oil"
# apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
# ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
# chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
# omelette = "egg, milk, bacon, tomato, salt, pepper"
#
# ingredient = input()
#
# if ingredient in pasta:
#     print("pasta time!")
# if ingredient in apple_pie:
#     print("apple pie time!")
# if ingredient in ratatouille:
#     print("ratatouille time!")
# if ingredient in chocolate_cake:
#     print("chocolate cake time!")
# if ingredient in omelette:
#     print("omelette time!")

# # ---------------
# i = 0
# a = 'a'
# while i < 8:
#     a *= 2
#     i += 1
# print(a)
# print(len(a))


# --------------
# While loop → Half-life
#
# N = int(input())
# R = int(input())
# T = 0
#
# while N > R:
#     T += 12
#     N /= 2
#
# print(T)

# # ------------------
# # While loop → Factorial
# N = int(input())
# output = 1
#
# while N > 0:
#     output = output * N
#     N -= 1
#
# print(output)


# # ---------------
# print('Hello! My name is Aid.')
# print('I was created in 2020.')
# print('Please, remind me your name.')
#
# name = input()
#
# print('What a great name you have, ' + name + '!')
# print('Let me guess your age.')
# print('Enter remainders of dividing your age by 3, 5 and 7.')
#
# rem3 = int(input())
# rem5 = int(input())
# rem7 = int(input())
#
# age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
#
# print("Your age is " + str(age) + "; that's a good time to start programming!")
# print('Now I will prove to you that I can count to any number you want.')
#
# # read a number and count to it here
# count = int(input())
# counter = 0
#
# while counter <= count:
#     print(str(counter) + "!")
#     counter += 1
#
# print('Completed, have a nice day!')

#----------------
# def is_even(number):
#     return number % 2 == 0

#-----------------
#
# def captain_adder(name):
#     print("captain" + name)
#
# captain_adder(Milad)

# ----------------
# An if-else statement is another type of conditional expressions in Python.
# It differs from an if statement by the presence of the additional keyword else.
# The block of code that else contains executes when the condition of
# your if statement does not hold (the Boolean value is False).
# Since an else statement is an alternative for an if statement,
# only one block of code can be executed.
# Also, else doesn't require any condition:

# if today == "holiday":
#     print("Lucky you!")
# else:
#     print("Keep your chin up, then.")

# Note that the 4-space indentation rule applies here too.

# As you may soon find out, programmers do like all sorts of shortcuts.
# For conditional expressions there's a trick as well – you can write an
# if-else statement in one line just like that:

# print("It’s a day now!" if sun else "It’s a night for sure!")

# Or, more generally:

# first_alternative if condition else second_alternative
# It's a matter of convenience, but remember that the code you create should still be readable.

# --------------------
# if x < 100:
#     print('x < 100')
# else:
#     if x == 100:
#         print('x = 100')
#     else:
#         print('x > 100')
#     print('This will be printed only because x >= 100')


# --------------------
# year = int(input())
#
# if year % 400 == 0:
#     print("Leap")
# else:
#     if year % 4 == 0 and year % 100 != 0:
#         print("Leap")
#     else:
#         print("Ordinary")

# ----------------------
# number = int(input())
#
# if number < 0:
#     print("negative")
# elif number > 0:
#     print("positive")
# else:
#     print(number)

# ----------------------
#
# Let's write a simple calculator!
# It will read 3 lines:
#
# the first number
# the second number
# the arithmetic operation.
# Numbers are floats!
#
# The output is the result of the following: first_number operation second_number.
#
# Operations are: +, -, /, *, mod, pow, div.
# mod — modulo operation, i.e. the remainder of the division first_numer % second_number,
# pow — exponentiation, the first number will be the base and the second — the power: first_number ** second_number,
# div — integer division first_number // second_number.
# Note that if the second number is 0 and you want to perform any of the operations /, mod, or div, the calculator should say "Division by 0!"
# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Division by 0!
# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0
# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5




first_number = float()

while first_number != "exit":
    first_number = float(input())
    second_number = float(input())
    operation = input()
    if first_number == "exit":
        print("See you!")
    else:
        if operation == "+":
            print(first_number + second_number)
        elif operation == "-":
            print(first_number - second_number)
        elif operation == "/":
            if second_number == 0:
                print("Division by 0!")
            else:
                print(first_number / second_number)
        elif operation == "*":
            print(first_number * second_number)
        elif operation == "mod":
            if second_number == 0:
                print("Division by 0!")
            else:
                print(first_number % second_number)
        elif operation == "pow":
            print(first_number ** second_number)
        elif operation == "div":
            if second_number == 0:
                print("Division by 0!")
            else:
                print(first_number // second_number)