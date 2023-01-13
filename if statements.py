"""Price of the house is $1M
house_value = 1000000
credit_score = 100000

if credit_score > 1000000:
    down_payment = house_value * 0.1
else:
    down_payment = house_value * 0.2
print (f'Put downpayment of ${down_payment}')"""

enter_full_name = input("Enter Name = ")

if len(enter_full_name) < 3:
    print("error ! - name must be at least 4 characters")

elif len(enter_full_name) > 20:
    print("error ! - name can be a maximum of 20 characters")

else:
    print(enter_full_name)
    print("Continue with the form")


