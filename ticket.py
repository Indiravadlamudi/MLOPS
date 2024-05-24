Age = int(input("Please enter your age: "))
if Age >= 65:
    print("Ticket price for adults: $10.00")
elif Age < 12:
    print("Ticket price for children: $8.00")
else:
    print("Ticket price for seniors: $12.50")