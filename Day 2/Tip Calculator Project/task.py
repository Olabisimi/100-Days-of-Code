print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_given = bill * (tip/100)
Amount_paid = bill + tip_given
Amount_paid_per_person = Amount_paid / people
Final_payment_per_person = round(Amount_paid_per_person, 2)
print(f"Each person should pay: ${Final_payment_per_person}")



