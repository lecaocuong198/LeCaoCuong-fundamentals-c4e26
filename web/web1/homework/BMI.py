def BMI(x,y):
    result = x/(y*y)
    if result<16:
        return "Severely underweight"
    if result<18.5:
        return "Underweight"
    if result<25:
        return "Normal"
    if result<30:
        return "Overweight"
    else:
        return "Obese"
