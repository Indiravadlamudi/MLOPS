Year = int(input("Enter a year: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(Year,"is a Leap year")
else:
    print(Year,"is not a leap year.")