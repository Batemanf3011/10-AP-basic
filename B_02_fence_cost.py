def num_check(question):
    error = "please enter a number more than zero\n"
    while True:
        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
    width = num_check("width: ")   
    height = num_check("height: ")
    cost = num_check("cost: ")

    perimeter = 2 * (width + height)
    price = perimeter * cost


    print()
    print(f"perimeter: {perimeter} meters")

    print(f"Price: {price:.2f} Dollars")
    keep_going = input("press enter to keep going or any key to quit")
    print()

print("thank you for using area perimeter calculator")


