import random
import csv

with open('names.txt', 'r') as f:
    names = f.readlines()

    names = list(names) #convert readlines object

    while len(names) > 0:
        idx = random.randrange(len(names))
        name = names.pop(idx)
        name = name.split(', ')
        print(name[1].strip() + ' ' + name[0])
        input()
