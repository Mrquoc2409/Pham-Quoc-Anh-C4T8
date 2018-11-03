Player = "P"
Key = "K"
Exit = "E"
Space = "-"


xp = 0
yp = 3 
xk = 0
yk = 2
xe = 3
ye = 3
k = False

print ("Your move keys : W, A, S, D")


def map():
    for i in range (4):
        for j in range (4):
            if i == xe and j == ye:
                print(Exit, end = '')
            elif i == xk and j == yk:
                if k == False :
                    print(Key, end = ' ')
                else:
                    print(Space, end = " ")
            elif j == xp and i == yp:
                print(Player, end = '')
            else:
                print(Space, end = '')
                    
        print() 

while True:

    dx = 0
    dy = 0

   
    map()
    m = input('Move?').lower()

    if m == "w":
        dy = -1
        
    elif m == "a":
        dx = -1
        
    elif m == "s":
        dy = 1
        
    elif m == "d":
        dx = 1
    if 0 <= xp + dx < 4 and 0 <= yp + dy < 4: 
        xp += dx
        yp += dy
    if xp == yk and yp == xk:
        print('Key acquired!')
        k = True
    if xp == xe:
        if yp == ye:
            if k == True :
                print('You hveve won')
                break    
            else:
                print("You can't exit, please acquire the key first")   