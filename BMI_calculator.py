wt = float(input("Enter your weight(in kg): "))  # weight in kilogram
ht = float(input("Enter your height(in m): "))  # height in meters
bmi = wt/(ht**2)      # (Body Mass Index)bmi calculation formula
print(f"BMI: {bmi} kg/m^2")
if(bmi < 18.5):
    print("You are Underweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("You are Normal weight")
elif(bmi>=25 and bmi<=29.9):
    print("You are Overweight")
else:
    print("You are Obesity")
