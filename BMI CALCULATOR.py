print("\t\tBMI CALCULATOR")
weight=float(input("ENTER THE WEIGHT IN KILOGRAMS"))
height=float(input("ENTER THE HEIGHT IN METERS"))
bmi_Value=(weight/(height**2))*10000
print("YOUR BMI VALUE IS",bmi_Value)
if bmi_Value<18.5:
    print("SORRY,YOUR ARE IN UNDERWEIGHT CATEGORY")
elif bmi_Value>=18.5 and bmi_Value<=24.9:
    print("YOUR ARE IN NORMALWEIGHT CATEGORY")
elif bmi_Value>=25 and bmi_Value<=29.9:
    print("YOUR ARE IN OVERWEIGHT CATEGORY")
else :
    print("YOUR ARE IN OBESITY CATEGORY")
    
