
while True:
    yob_str =  input("Your year of birth: ")
    if yob_str.isdigit():
        yob = int(yob_str)
        if 1974<yob<2000:
            break
        else:   
            print("You must enter number: ")
    else:   
        print("You must enter number: ")



age = 2019 - yob
print(age)