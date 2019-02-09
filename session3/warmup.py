yob_str = input("Your year of birth? ")

while (not yob_str.isdigit()):
    print("You must enter number")
    yob_str =  input("Enter number")
yob = int(yob_str)
age = 2019-yob
print(age)
