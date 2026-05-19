

###Data types###
#strings
len("Hello")

# Integers
print(123_456_789)

# Floats
print(123.456)

#booleans
print(False)
print(True)

###Type Error, Checking and Conversion###
len("Hallo")

print(type("hallo"))

print(type(123))

print(type(False))

print(type(123.456))

#Mathematical Operations
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

# PEMDASLR Order
# ()
# **
# * OR /
# + OR -

# Outputs 7
print(3 * 3 + 3 / 3 - 3)

# Outputs 3
print(3 * 3 + 3 / 3 - 3)

###Number Manipulation###

bmi = 84 / 1.65 ** 2

# Original Float with decimal places
print(bmi)

# Flooring the number by converting it into int
print(int(bmi))

# Rounding the number into a whole number
print(round(bmi))

# Rounding only to 2 decimal places
print(round(bmi, 2))


## Accumulate
score = 0

# User scores a point
score += 1
print(score)

#Also
score -= 1
score *= 2
score /= 2

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

###Tip Calculator###
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")



