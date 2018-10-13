Movies = ["Spider-man", "Infinity war","Dragon ball"]

print(*Movies, sep = " | ")

i = input("What do you want to DELETE ?")
Movies.remove(i)

j = input("Input new movies you like.").upper()
m = input("Input new movies you like.").upper()
n = input("Input new movies you like.").upper()

Movies.append(j)
Movies.append(m)
Movies.append(n)

print("Updated:", Movies[0].upper(), Movies[1].upper(), Movies[2].upper(), Movies[3].upper(), Movies[4].upper(), sep = " \n ")
