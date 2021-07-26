# pcost.py
#
# Exercise 1.27

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

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
