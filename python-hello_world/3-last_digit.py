#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
if '-' in number:
    last_digit = '-' + number[-1]
else:
    last_digit = number[-1]
number = int(number)
last_digit = int(last_digit)
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5", end="\n")
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0", end="\n")
if last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0", end="\n")
    
    
