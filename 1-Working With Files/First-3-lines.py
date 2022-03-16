import csv
with open('year2017.csv') as file_obj:
    csv_data = csv.reader(file_obj)
    csv_list = list(csv_data)
    for i in range(1,4):
        print(csv_list[i])