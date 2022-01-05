# Given a file Sample.txt we have to read the first 100 bytes of the text
a = open('Sample.txt')
var = a.read(100)
print(var)