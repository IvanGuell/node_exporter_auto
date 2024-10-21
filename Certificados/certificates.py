import csv
from pprint import pprint

data_list = []

print('Info Certs:')
with open('certificates.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')

    for row in reader:
        row_dict = {}
        for field, value in row.items():
            row_dict[field] = value


        fingerprint_exists = any(d['fingerprint'] == row_dict['fingerprint'] for d in data_list)

        if not fingerprint_exists:
            data_list.append(row_dict)

pprint(data_list)






