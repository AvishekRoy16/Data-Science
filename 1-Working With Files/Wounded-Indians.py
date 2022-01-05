import csv
with open('year2017.csv') as file_obj:
    file_data = csv.reader(file_obj)
    csv_list = list(file_data)
    wounded = []
    for row in csv_list[1:]:
        if row[3] == 'India' and row[10] != '':
            wounded.append(float(row[10]))
    print(int(sum(wounded)))
    