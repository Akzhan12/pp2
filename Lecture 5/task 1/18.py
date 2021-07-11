def count_words(filepath):
       with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("test2.txt"))