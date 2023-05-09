#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_numeric = number % 10
else:
    last_numeric = ((number * -1) % 10) * -1

content = "Last digit of %d is %d and is" % (number, last_numeric)

if last_numeric == 0:
    print(content, "0")
elif last_numeric > 5:
    print(content, "greater than 5")
else:
    print(content, "less than 6 and not 0")
