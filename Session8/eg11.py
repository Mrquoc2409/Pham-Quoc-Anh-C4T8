Movies = ["Spider-man", "Infinity war","Dragon ball"]

print(*Movies, sep = " | ")

Movies[0] = 'Spider-man 3'

print("Updated:", *Movies, sep = " | ")