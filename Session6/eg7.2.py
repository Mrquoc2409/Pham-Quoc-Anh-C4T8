password = str(input("Type your password : "))
loop = True
flag = False
import string
while loop:
    #scan
    loop = False
    for i in password:
        if i in string.digits:
            flag = True
            break
    #check
    if (flag == True):
        print("Your password suck!!")
        break
