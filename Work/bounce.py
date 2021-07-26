# bounce.py
#
# Exercise 1.5

height = 100
ratio = 3/5
bounces = 1

while height > 1:
    height = height * ratio
    print(bounces, round(height, 4))
    bounces = bounces + 1
