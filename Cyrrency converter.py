# currnncy converter in all currency
inr_to_usd = 0.085
inr_to_eur = 0.042
inr_to_kwa = 0.012

def in_to_USD(amont):
    return amount * inr_to_usd

def in_to_EUR(amont):
    return amount * inr_to_eur

def in_to_KWA(amont):
    return amount * inr_to_kwa


print("welcome to currnecy calculator")
amount = int(input("enter your amount in INR:"))

transfer = int(input("enter your choice to convert in 1/2/3:"))

if transfer == 1:
   print(f"your amount {amount} in INR to {in_to_USD(amount)} USD")

elif transfer == 2:
    print(f"your amount {amount} in INR to {in_to_EUR(amount)} EUR")

elif transfer == 3:
    print(f"your amount {amount} in INR to {in_to_KWA(amount)} KWA")

else:
    print('invalid opreator')

print("thanks to use my currency converter")





    


