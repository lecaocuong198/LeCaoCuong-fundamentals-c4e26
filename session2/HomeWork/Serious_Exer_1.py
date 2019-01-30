height = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))

height = height*0.01
BMI = float(weight/(height*height))

print("Your BMI is ", BMI)

if(BMI<16):
    print("Severely underweight")
elif (BMI<18.5):
    print("Underweight")
elif(BMI<25):
    print("Normal")
elif(BMI<30):
    print("Overweight")
else:
    print("Obese")