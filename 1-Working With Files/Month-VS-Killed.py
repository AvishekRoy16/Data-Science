import csv
with open('year2017.csv') as file_obj:
    file_data = csv.DictReader(file_obj)
    file_list = list(file_data)
    killed = {}
    for row in file_list:
        key = row['Month']
        value = row['Killed']
        
        if value != '':
            value = int(float(value))
        else:
            value = 0
        
        if key in killed:
            killed[key] += value
        else:
            killed[key] = value
    for months in killed:
        print(months, killed[months]) 