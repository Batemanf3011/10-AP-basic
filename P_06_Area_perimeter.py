
#ask user for width and height
Width = float(input("width: "))
Height = float(input("height"))

# calculate area and perimeter
area = Width * Height
perimeter = 2 * (Width + Height)

# output area and perimeter
print()
print(f"perimeter: {perimeter} units")
print(f"Area: {area} square units")

keep_going = input("press enter to keep going or any key to quit.")
print()

print("Thank you for using area perimeter calculator")