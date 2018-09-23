print("a^2 + 2*a*b + b^2 = 0")
a = int(input("a=? "))
b = int(input("b=? "))
c = int(input("c=? "))
Delta = (b**2) - 4 * a * c 
if Delta < 0:
    print("There is(are) no root(s)")
elif Delta == 0:
    n = (-b) / (2*a)
    print("there's one root!")
    print("m= ", n)
elif Delta > 0:
    n1 = ((-b) - (Delta)**0.5) / (2*a)
    n2 = ((-b) + (Delta)**0.5) / (2*a)
    print("there're two roots!")
    print("m1=", n1)
    print("m2=", n2)