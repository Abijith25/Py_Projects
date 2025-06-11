print("\t\t\t\t TEMPERATURE CONVERTOR")
def celsius_Conversions():
    celsius=float(input("ENTER THE DEGREE IN CELSIUS"))
    if choice==1:
        fahrenheit = (celsius * 9/5) + 32
        print("THE DEGREE IN FAHRENHEIT IS,",fahrenheit)
    elif choice==2:
        kelvin = celsius + 273.15
        print("THE DEGREE IN KELVIN IS,",kelvin)
def fahrenheit_Conversions():
    fahrenheit =float(input("ENTER THE DEGREE IN FAHRENHEIT"))
    if choice==3:
        Celsius = (Fahrenheit - 32) * (5/9)
        print("THE DEGREE IN CELSIUS IS,",Celsius)
    elif choice==4:
        Kelvin = (Fahrenheit - 32) * 5/9 + 273.15
        print("THE DEGREE IN KELVIN IS,",Kelvin)
def kelvin_Conversions():
    Kelvin =float(input("ENTER THE DEGREE IN KELVIN"))
    if choice==5:
        Celsius = Kelvin - 273.15
        print("THE DEGREE IN CELSIUS IS,",Celsius)
    elif choice==6:
        Fahrenheit = (Kelvin - 273.15) * 9/5 + 32
        print("THE DEGREE IN FAHRENHEIT IS,",fahrenheit)
loop_Variable=0
while loop_Variable==0:
    print("\t\t\t\tTEMPERATURE CONVERTER")
    print("SELECT ONE OF THE OPTIONS GIVEN BELOW")
    print("\t\t\t1.CELSIUS TO FAHRENHEIT")
    print("\t\t\t2.CELSIUS TO KELVIN")
    print("\t\t\t3.FAHRENHEIT TO CELSIUS")
    print("\t\t\t4.FAHRENHEIT TO KELVIN")
    print("\t\t\t5.KELVIN TO CELSIUS")
    print("\t\t\t6.KELVIN TO FAHRENHEIT")
    print("\t\t\t7.EXIT")
    choice=int(input("ENTER THE CHOICE"))
    if choice==1 or choice==2:
        celsius_Conversions()
    elif choice==3 or choice==4:
        fahrenheit_Conversions()
    elif choice==5 or choice==6:
        kelvin_Conversions()
    else:
        break
    value=1 if input("DO YOU WANT TO CONTINUE") in ('NO','no') else 0
    loop_Variable=value
