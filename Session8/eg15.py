Movies = ["Spider-man", "Infinity war","LOL"]

print(*Movies, sep = " | ")
i = int(input("The number you want to change."))
Movies[i] = input("What do you wnat to change it to ?")

            
if "LOL" in Movies:
    print("There is something called LOL in Movies!")
else:
    print("There is nothing called LOL in Movies!")



print("Updated:", *Movies, sep = " | ")