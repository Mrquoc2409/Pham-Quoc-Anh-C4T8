yob = int(input("year of birth?"))
age = 2018 - yob 
print(age)
if age < 14:
     print("You can't watch this video!")
elif age < 18:
    print("Teenager")
else:
    print("You can watch this video!")