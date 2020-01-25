units = int(input(" Please enter Number of Units you Consumed this month : "))
urjaakar = 219       // Tax taken by government
digitaloffer = 5.43  // Offer
othertaxes = 12.56   // Other taxes
if(units > 500):
    amount = units * 9.65
    surcharge = 40
elif(units >= 300):
    amount = units * 7.75
    surcharge = 30
elif (units >= 200):
    amount = units * 5.26
    surcharge = 20
elif (units >= 100):
    amount = units * 3.76
    surcharge = 10
else:
    amount = units * 2.25
    surcharge = 25

total = amount + surcharge + urjaakar - digitaloffer - othertaxes
print("\nYour Electricity Bill in rupees is = %.2f"  %total)