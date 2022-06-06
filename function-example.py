#Example without function
value1 = int(input("Please Enter the First Value: "))
value2 = int(input("Please Enter the Second Value: "))
result = value1 + value2
print(result)
#Example with Function
from math import *
def addvalue(numbervalue, numbervalue2):
    addedvalue = numbervalue + numbervalue2
    print(addedvalue)
addvalue(7, 5)
#Light Switch Example
def light(statement):
    if statement == 1:
        print("The light is turned on")
    else:
        print("The light is turned off")
light(1)