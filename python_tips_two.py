#it is hard to read that numbers
num1 = 10000000000
num2 = 100000000
total = num1 + num2
print(total)
"""
OUTPUT:
10100000000
"""

#python do not care the underscore in an integers
num3 = 10_000_000_000
num4 = 100_000_000
total = num3 + num4
print(total)
"""
OUTPUT:
10100000000
"""

#for the result the output become more readable with format the it like
print(f'{total:,}')
"""
OUTPUT:
10,100,000,000
"""
