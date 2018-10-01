password = input("Enter your password.")
numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z"]
loop = True
flag = False
while loop:
    #scan
    for i in range(len(numbers)) :
        if numbers[i] in password:
            flag = True
            print("kay")
    #check
        if (flag == True):
            print("ur good")
            loop = False
        else: 
            password = input("Enter your password.")





