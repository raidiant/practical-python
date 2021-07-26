# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    """Open portfolio and read into structured data

    :filename: name of portfolio file
    :returns: python list of shares and their information

    """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name':   row[0],
                'shares': int(row[1]),
                'price':  float(row[2])
            }

            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    """Open prices file and read into structured data

    :filename: name of prices file
    :returns: python list of prices for a share

    """
    prices = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                share = {
                    'name':   row[0],
                    'price':  float(row[1])
                }
                prices.append(share)
            except IndexError as e:
                print("Error indexing incoming data")
                continue

    return prices
