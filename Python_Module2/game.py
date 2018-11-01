
x = int(input('Input x coordinate.'))
y = int(input('Input y coordinate.'))


x_x = x - 1
x_y = y - 1

for i in range (4):   
    for j in range (4):
        if j == x_x and i == x_y:
            print("P", end = " ")
        else:
            print("⍰", end =" ")

    print()