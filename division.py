def divideNumbers(userOne, userTwo):
    try:
        answer = userOne / userTwo
        print("Result: " + str(answer))
    except ZeroDivisionError:
        print("You broke math pal, you cannot divide by zero!")