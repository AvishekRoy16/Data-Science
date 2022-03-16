import csv
with open('year2017.csv') as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)

country_casualties = {}
for row in file_list:
    key = row['Country']
    value = row['casualities']
    if value != '':
        value = int(float(value))
    else:
        value = 0
        
    if key in country_casualties:
        country_casualties[key] += value
    else:
        country_casualties[key] = value
        
print(country_casualties)
