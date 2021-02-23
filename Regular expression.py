import re

Pattern = "pet:cats i love pets pet:cow I love cows"
Result = re.search(r'pet:\w\w\w\w',Pattern)
print(Result)
print(Result.group())

results = re.match(r'pet:\w\w\w\w\s',Pattern)
print(results)
print(results.group())

Out = re.findall(r'pet:\w\w\w',Pattern)
print(Out)

Split = re.split(r'pet:\w\w\w',Pattern)
print(Split)

String = "Hello Welcome to Python"
S = re.split(r'\S',String)
s = re.split(r'\s',String)
print(S)
print(s)

Int = '1,2,3,4,5,6,7,8,9'
D = re.split(r'\D',Int)
d = re.split(r'\d',Int)
print(D)
print(d)

Substitute = "Vinay357@co.in,Vijay@co.in"
Change = re.sub(r'@\w+','@gmail',Substitute)
print(Change)
