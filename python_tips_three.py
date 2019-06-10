
#for all read file code at the end of the code file should closed.
f = open('test.txt', 'r')
file_contents = f.read()
f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

#for all the time use a file closing it is became a big job.
with open('test.txt', 'r') as f:
    #python manage the file life cycle
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
