n = input("Input your month!")
if n in ["January" , "March" , "May" , "July" , "August" , "October" , "December" ]:
    print("There are 31 days in this month.")
elif n in ["April" , "June" , "September" , "November"]:
    print("There are 30 days in this month.")
elif n in ["February"]:
    print("There are 27 or 28 days in this month.")