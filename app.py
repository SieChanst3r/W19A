import addition
import subtraction
import multiplication
import division

print("Please choose a number to do the following and then hit ENTER: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

userSelection = input()
userOne = int(input("First Number Selected: "))
userTwo = int(input("Second Number Selected: "))

if userSelection == "1":
    addition.addNumbers(userOne, userTwo)
elif userSelection == "2":
    subtraction.subtractNumbers(userOne, userTwo)
elif userSelection == "3":
    multiplication.multipyNumbers(userOne, userTwo)
elif userSelection == "4":
    division.divideNumbers(userOne, userTwo)
else:
    print("uh oh, there was an error.. Make new selection")