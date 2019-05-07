year =int(input("Please enter the year you were born:" ))
age =  2019 - year

print("you must be“, age, "years old")

if age < 50:
    print("you are not yet a senior citizen")

elif age == 50:
    print("welcome to deny's, may I take your order please")

else:
    print("you are a senior citizen")
