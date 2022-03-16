import csv
with open('year2017.csv') as file_obj:
    file_data = csv.reader(file_obj)
    csv_list = list(file_data)
    wounded = []
    for row in csv_list[1:]:
        val = row[10]
        if row[10] != '':
            wounded.append(float(val))
    print(int(sum(wounded)))
    