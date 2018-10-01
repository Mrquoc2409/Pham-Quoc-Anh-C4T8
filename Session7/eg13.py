import random

points = 0 

while True:
       
        c = 0
        e = 0

        a = random.randint(0,10)
        b = random.randint(0,10)
        d = random.randint(1,2)
        #Addition:
        if d == 1:
            c = a + b
            e = c + random.randint(-2,2)
            print(str(a)+'+'+str(b)+'='+str(e))
            
            if e == c:
                check1 = True 
            else:
                check1 = False
            
            n = str(input("What's your answer? Type 't' for TRUE and 'f' for FALSE'")).upper()
            if n == "T":
                check2 = True
            elif n == "F":
                check2 = False 
            if check2 == check1:
                points +=1
            else:
                print("You lose!")
                print("You have "+str(points)+" points")
                break
            
            
        #Subtraction:
        if d == 2:
            c = a - b 
            e = c+random.randint(-2,2)
            print(str(a)+'-'+str(b)+'='+str(e))
            
            if e == c:
                check1 = True 
            else:
                check1 = False
                        
            n = str(input("What's your answer? Type 't' for TRUE and 'f' for FALSE'")).upper()
            if n == "T":
                check2 = True
            elif n == "F":
                check2 = False 
            if check2 == check1:
                points +=1
            else:
                print("You lose!")
                print("You have "+str(points)+" points")
                break

end = input("Press ENTER to exit")