# This program prints the largest odd number, if any.
# Inputs 3 integers: x, y, z
x, y, z = 0, 0, 0
x = int(raw_input("Enter #1 integer: "))
y = int(raw_input("Enter #2 integer: "))
z = int(raw_input("Enter #3 integer: "))

if (x%2 == 0):
    if (y%2 == 0):
        # x and y are not odd
        if (z%2 == 0):
            #x, y, z are not odd
            print("None of the entered integer are odd")
        else:
            # z is the only odd
            print(str(z) + " is the largest odd integer")
    else:
        # x is not odd and y is odd
        if (z%2 == 0):
            # y is the only odd
            print(y + " is the largest odd integer")
        else:
            # y and z are odd
            if (y > z):
                print(str(y) + " is the largest odd integer")
            else:
                print(str(z) + " is the largest odd integer")
else:
    # x is odd
    if (y%2 == 0):
        # y is not odd
        if (z%2 == 0):
            # y and z are not odd
            print(str(x) + " is the largest odd integer")
        else:
            # x and z are odd
            if (x > z):
                print(str(x) + " is the largest odd integer")
            else:
                print(str(z) + " is the largest odd integer")
    else:
        # x and y are odd
        if (z%2 == 0):
            # z is not odd
            if (x > y):
                print(str(x) + " is the largest odd integer")
            else:
                print(str(y) + " is the largest odd integer")
        else:
            #x, y and z are odd
            if (x > y) and (x > z):
                print(str(x) + " is the largest odd integer")
            elif (y > z):
                print(str(y) + " is the largest odd integer")
            else:
                print(str(z) + " is the largest odd integer")
