import csv
with open('year2017.csv') as file_obj:
    file_data = csv.reader(file_obj)
    csv_list = list(file_data)
    for i in range(1,11):
        print(csv_list[i][3])
        