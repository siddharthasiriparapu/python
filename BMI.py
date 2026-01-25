print("BMI calcuater")
height=float(input("enter your height in cm"))
weight=float(input("enter your weight in Kg"))

BMI=weight/(height/100)**2

print("your BMI is ",BMI)

if BMI<=18.4:
    print("your underweight")
elif BMI<=24.9:
    print("your healty")
elif BMI<=29.9:
    print("your overweight")
elif BMI<=34.9:
    print("your severly overweigt")
else: 
    print("your are obease")