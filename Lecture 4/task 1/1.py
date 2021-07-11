import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x.start())
print(x.endpos)
print(x.span())
print(x.group())