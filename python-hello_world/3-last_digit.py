#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last_digit = number[-1]
number = int(number)
last_digit = int(last_digit)
if number > 0 and last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
if int(last_digit) == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
if int(last_digit) < 6 and int(last_digit) != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
    
