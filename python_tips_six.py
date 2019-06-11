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

import sys
print(sys.executable)
