w = int(input('Input width.'))
h = int(input('Input height.'))
x = int(input('Input x coordinate.'))
y = int(input('Input y coordinate.'))


x_x = x - 1
x_y = y - 1

for i in range (h):   
    for j in range (w):
        if j == x_x and i == x_y:
            print("x", end = " ")
        else:
            print("o", end =" ")

    print()