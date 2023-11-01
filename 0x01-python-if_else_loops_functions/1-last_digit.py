#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    abs_value = -number
else:
    abs_value = number
last_digit = abs_value % 10
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"
print("Last digit of", number, "is", last_digit, message)
