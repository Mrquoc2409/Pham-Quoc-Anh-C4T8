List = ["One", "Two", "Three", "Four", "Five", "Six"]
print('''"CRUD"
C- Create
R-Read
U-Update
D-Delete''')
 

i = input("Choose the part you want to go to.").upper()

if i == "C":
    print("C")