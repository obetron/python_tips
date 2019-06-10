#with python print the list like;
names = ['Eren', 'Asil', 'Ebru']

for name in names:
    print(name)

#add an index for all elements;
index = 0
for name in names:
    print(index, name)
    index += 1

#for more clean code
for index, name in enumerate(names):
    print(index, name)

#want to index start from 1
for index, name in enumerate(names, start=1):
    print(index, name)
