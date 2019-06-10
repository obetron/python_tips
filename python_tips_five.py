
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spider Man', 'Superman', 'Deadpool', 'Batman']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')
"""
OUTPUT:
Peter Parker is actually Spider Man
Clark Kent is actually Superman
Wade Wilson is actually Deadpool
Bruce Wayne is actually Batman
"""

#for cleaner code
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')
"""
OUTPUT:
Peter Parker is actually Spider Man
Clark Kent is actually Superman
Wade Wilson is actually Deadpool
Bruce Wayne is actually Batman
"""

universes = ['Marvel', 'DC', 'Marvel', 'DC']
for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')
"""
OUTPUT:
Peter Parker is actually Spider Man from Marvel
Clark Kent is actually Superman from DC
Wade Wilson is actually Deadpool from Marvel
Bruce Wayne is actually Batman from DC
"""

for value in zip(names, heroes, universes):
    print(value)
"""
OUTPUT:
('Peter Parker', 'Spider Man', 'Marvel')
('Clark Kent', 'Superman', 'DC')
('Wade Wilson', 'Deadpool', 'Marvel')
('Bruce Wayne', 'Batman', 'DC')
"""
