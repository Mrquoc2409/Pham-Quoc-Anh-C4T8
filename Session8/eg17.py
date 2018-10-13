Movies = ["Spider-man", "Infinity war","Dragon ball"]

print(*Movies, sep = " | ")

i = input("What do you want to DELETE ?")

Movies.remove(i)

print("Updated:", *Movies, sep = " | ")