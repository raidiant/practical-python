# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
original_payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    # larger payment for starting 12 months
    # if month < 12:
    #     payment = original_payment + 1000
    # else:
    #     payment = original_payment
    payment = original_payment

    # start of month payment
    if month % 12 == 0:
        payment = payment + extra_payment_start_month
    # end of month payment
    if month % 12 == 11:
        payment = payment + extra_payment_end_month

    # extra payment for 4 years after first 5 years
    if month >= 12 * 5 and month < 12 * 9:
        payment = payment + extra_payment

    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    print(f'In month {month} total amount paid is ${total_paid}, left principal is ${principal}')

print('Total paid', total_paid, 'over', month)
