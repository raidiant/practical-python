# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)

    total = 0
    for line in f:
        name, shares, price = line.split(',')
        tot_share_cost = int(shares.strip()) * float(price.strip())
        print(name, 'total cost', tot_share_cost)
        total = total + tot_share_cost

print('Total cost', total)

