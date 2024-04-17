# check if number which user entered is positive
while True:
    # the code below is the same as scope_1
    user_input = int(input("Enter a number: "))

    if user_input > 0:
        positive = True

    if positive:
        print("Positive!")
    else:
        print("Negative!")
