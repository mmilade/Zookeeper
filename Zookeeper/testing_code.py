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


# ---------------
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
count = int(input())
counter = 0

while counter <= count:
    print(str(counter) + "!")
    counter += 1

print('Completed, have a nice day!')
