n = int(input("Input your number?"))
for i in range (n+1):
    if n < 0 :
        print("Input a number bigger than 0!")
        break
    else:
        print(i)