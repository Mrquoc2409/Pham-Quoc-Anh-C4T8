name = input("Enter your name.")
numbers = ["0","1","2","3","4","5","6","8","9","7"]
loop = True
flag = False
while loop:
    # scan
    for i in range(len(numbers)):
        if numbers[i] in name:
            flag = True
    # check
    if (flag == True):
        print("No number allow!")
        loop = False
    else:
        name = input("Enter your name.")
    

