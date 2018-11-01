
x = 0
y = 3 

print ("Your move keys : W, A, S, D")


def map():
    for i in range (4):
        for j in range (4):
            if i == 3 and j == 3:
                print("E", end = '')
            elif i == 0 and j == 2:
                print("K", end = '')
            elif j == x and i == y:
                print("P", end = '')
            else:
                print("-", end = '')
                    
        print() 

while True:

    dx = 0
    dy = 0

   
    map()
    m = input('Move?')

    # if x > 3:
    #     dx = 0 
    # elif x < 0:
    #     dx = 0
    # if y  > 3:
    #     dy = 0
    # elif y < 0:
    #     dy = 0


    if m == "w":
        dy = -1
        
    elif m == "a":
        dx = -1
        
    elif m == "s":
        dy = 1
        
    elif m == "d":
        dx = 1
    if x + dx <= 3 :    
        x += dx
        y += dy
    

