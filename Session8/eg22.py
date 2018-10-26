while True:
    List = ["One", "Two", "Three", "Four", "Five", "Six"]
    print('''"CRUD"

    C- Create
    R-Read
    U-Update
    D-Delete''')

    print ('You can get out by entering "DONE"')
    

    i = input("Choose the part you want to go to.").upper()

    if i == "C":
        j = input("What do you want to add in the List ?")
        List.append(j)
        for n in List:
            print(n)
    elif i == "R":
        for n in List:
            print(n)
    elif i == "U":
        m = int(input("The number you want to change?"))
        List[m] = input("What do you wnat to change it to ?")
        for n in List:
            print(n)
    elif i == "D":
        p = int(input("The number do you want to DELETE."))
        List.pop(p)
        for n in List:
            print(n)
    elif i == 'DONE':
        break
    else:
        print ("You can only type 'C' or 'R' or 'U' or 'D'")