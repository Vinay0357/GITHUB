import re

# RE Match
PyLine = "pet:Cat I Like Pets"
PyMatch = re.match(r"pet:\w\w\w",PyLine)
print(PyMatch)

# RE Search
PyLine = "pet:Cat I Like Pets"
PyMatch = re.search(r"pet:\w\w\w",PyLine)
print(PyMatch)
print(PyMatch.group()) # pet:Cat

# RE Find All

PyLine = "pet:Cat I Like Pets Pet:cow I like cows"
PyMatch = re.findall(r"pet:\w\w\w",PyLine)
print(PyMatch)
