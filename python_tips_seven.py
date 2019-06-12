
class Person():
    pass

person1 = Person()

#in python we can add attributes and values dynamically
person1.first = 'Eren'
person1.last = 'Basaran'
print(person1.first)
print(person1.last)
"""
OUTPUT:
Eren
Basaran
"""


person2 = Person()
first_key = 'first'
first_val = 'Eren'
setattr(person2, first_key, first_val)
print(person2.first)
"""
OUTPUT:
Eren
"""

person3 = Person()
second_key = 'second'
second_val = 'Asil'
setattr(person3, second_key, second_val)
second = getattr(person3, second_key)
print(person3.second)
"""
OUTPUT:
Asil
"""

person4 = Person()
person4_info = {'name': 'Eren', 'surname': 'Basaran'}
for key, value in person4_info.items():
    setattr(person4, key, value)
print(person4.name)
print(person4.surname)
"""
OUTPUT:
Eren
Basaran
"""

person5 = Person()
person5_info = {'name': 'Asil', 'surname': 'Basaran'}
for key, value in person5_info.items():
    setattr(person5, key, value)
for key in person5_info.keys():
    print(getattr(person5, key))
"""
OUTPUT:
Asil
Basaran
"""
