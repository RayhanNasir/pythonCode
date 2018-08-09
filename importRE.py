import re

string = "I'm willing to do the right thing,BUT I CAN'T"
print(string)
new = re.sub('[A-Z]', ' ', string)
print(new)
new = re.sub('[a-z]', ' ', string)
print(new)
new = re.sub('[.,\']', ' ', string)
print(new)
new = re.sub('[.,\']', ' ', string)
print(new)
