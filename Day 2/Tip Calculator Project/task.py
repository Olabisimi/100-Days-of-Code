print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_given = bill * (tip/100)
amount_paid = bill + tip_given
amount_paid_per_person = amount_paid / people
final_payment_per_person = round(amount_paid_per_person, 2)
print(f"Each person should pay: ${final_payment_per_person}")



