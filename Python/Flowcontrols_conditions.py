"""
Syntax:

if CONDITION:
   # Condition is True
else:
   # Condition is False

Usage: Condition is relace with an expression
True path: you write logic for the true case
False path: you write logic for the false case

"""
value = input("Give me a number: ")
if isinstance(value, int):
    print("All good, keep going")
else:
    value = float(value)

if value == 100:
    print("Value is equel to 100")
elif value>100:
    print("value is greater than 100")
elif value<100:
    print("value is less than 100")
else:
    print("value is NOT equal to9 100")