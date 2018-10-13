import string

while True:
        password = input("Enter password.")
        if len(password) >= 8:
            
            for i in password:
                if i in string.ascii_letters: 
                    break
            for i in password:
                if i in string.digits:
                    break
            for i in password:
                if i in string.ascii_uppercase:
                    break 
            if password != "Techkid123":
                print("Wrong password")
            else:
                print("welcome!")
                break