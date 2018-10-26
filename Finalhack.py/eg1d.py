n = int(input('Number?'))
for i in range(1,n):
    if i%2 == 0:
        print("*", end=" ")
    elif i%2 != 0:
        print('x', end=" ")
