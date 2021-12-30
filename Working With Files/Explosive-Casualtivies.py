import csv
with open('year2017.csv') as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
    casualties = []
    for row in file_data:
        if row['Weapon_type'] == 'Explosives' and row['casualities'] != '' :
            casualties.append(float(row['casualities']))
    print(int(sum(casualties)))