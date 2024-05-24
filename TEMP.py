Temp = float(input("Enter temperature: "))
Unit = input("Enter unit (C/F): ").upper()
if Unit == "C":
    Converted_temp = (Temp * 9/5) + 32
    print("Temperature in Fahrenheit:", Converted_temp, "degrees Fahrenheit")
elif Unit == "F":
    Converted_temp = (Temp - 32) * 5/9
    print("Temperature in Celsius:", Converted_temp, "degrees Celsius")
else:
    print("Invalid unit entered.")
