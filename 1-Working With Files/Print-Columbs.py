import csv
with open('year2017.csv') as file_obj:
    file_data = csv.reader(file_obj)
    list_data = list(file_data)
    for i in list_data[0]:
        print(i)
