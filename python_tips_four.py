#with python print the list like;
names = ['Eren', 'Asil', 'Ebru']
for name in names:
    print(name)
"""
OUTPUT:
Eren
Asil
Ebru
"""

#add an index for all elements;
index = 0
for name in names:
    print(index, name)
    index += 1
"""
OUTPUT:
0 Eren
1 Asil
2 Ebru
"""

#for more clean code
for index, name in enumerate(names):
    print(index, name)
"""
OUTPUT:
0 Eren
1 Asil
2 Ebru
"""

#want to index start from 1
for index, name in enumerate(names, start=1):
    print(index, name)
"""
OUTPUT:
1 Eren
2 Asil
3 Ebru
"""
