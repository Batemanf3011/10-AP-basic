error = "please enter a number more than zero\n"
while True:
     try:
        width = float(input("width:"))

        if width > 0:
            break
        else:
            print(error)

     except ValueError:
         print(error)