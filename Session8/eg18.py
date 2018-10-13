Movies = ["Spider-man", "Infinity war","Dragon ball"]

print(*Movies, sep = " | ")

i = input("What do you want to DELETE ?")
Movies.remove(i)

j = input("Input new movies you like.")
m = input("Input new movies you like.")
n = input("Input new movies you like.")

Movies.append(j)
Movies.append(m)
Movies.append(n)

print("Updated:", *Movies, sep = " \n ")
