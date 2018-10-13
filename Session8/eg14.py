Movies = ["Spider-man", "Infinity war","Dragon ball"]

print(*Movies, sep = " | ")

i = int(input("The number you want to change."))
Movies[i] = input("What do you wnat to change it to ?")
Movies.pop(1)

print("Updated:", *Movies, sep = " | ")