# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f)

        total = 0
        for line in f:
            name, shares, price = line.split(',')
            try:
                total = total + int(shares.strip()) * float(price.strip())
            except ValueError as e:
                print('Encountered unproccessable values!')

    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
