# Read 5 lines of Sample.txt using readlines
with open('Sample.txt') as a:
    var = a.readlines()
for i in range(5):
    print(var[i])