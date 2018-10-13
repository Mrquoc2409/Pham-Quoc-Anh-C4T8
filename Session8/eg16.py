Movies = ["Spider-man", "Infinity war","Dragon ball"]

print(*Movies, sep = " | ")

i = int(input("The number you want to DELETE."))

Movies.pop(i)

print("Updated:", *Movies, sep = " | ")