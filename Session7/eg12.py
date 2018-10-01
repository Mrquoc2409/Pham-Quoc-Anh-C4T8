import string


username = input("What's your username?")

if username == ("techkids"):
    
    while True:
        password = input("Enter password.")
        if len(password) >= 8:
            
            for i in password:
                if i in string.ascii_letters: 
                    break
            for i in password:
                if i in string.digits:
                    break
            if password != "techkid123":
                print("Wrong password")
            else:
                break
    while True: 
        con1 = False
        con2 = False
        email = input ("Enter email.")
        if "@" in email :
            con1 = True
                
        if "." in email:
            con2 = True 
        if con1 and con2 :
            break
    
    print("Welcome user", username )
    

    
else:
    print("You are not superuser!")