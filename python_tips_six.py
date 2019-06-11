#Normal usage of lists or tuples
items = (1, 2)
print(items)
"""
OUTPUT:
(1, 2)
"""

#Unpacking
a, b = (1, 2)
print(a)
print(b)
"""
OUTPUT:
1
2
"""

#Ignoring variable in python is name it with underscore
a, _ = (1, 2)
print(a)
"""
OUTPUT:
1
"""

#more variables than values
# a, b, c = (1, 2)
"""
OUTPUT:
ValueError: need more than 2 values to unpack
"""

#more values than variables
# a, b = (1, 2, 3)
"""
OUTPUT:
ValueError: too many values to unpack
"""

#
a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
"""
(with python3 and higher)
OUTPUT:
1
2
[3, 4, 5]
"""

d, e, *_ = (1, 2, 3, 4, 5)
print(d)
print(e)
"""
OUTPUT:
1
2
"""

f, g, _, *h = (1, 2, 3, 4, 5)
print(f)
print(g)
print(h)
"""
OUTPUT:
1
2
[4, 5]
"""

i, j, *_, k = (1, 2, 3, 4, 5)
print(i)
print(j)
print(k)
"""
OUTPUT:
1
2
5
"""

l, m, *n, o = (1, 2, 3, 4, 5)
print(l)
print(m)
print(n)
print(o)
"""
OUTPUT:
1
2
[3, 4]
5
"""
