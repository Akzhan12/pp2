with open('abc.txt', "w", encoding='utf8') as f:
    f.write("Hello\n")
    f.write('Test text')
x = open('abc.txt') 
print(x.read())