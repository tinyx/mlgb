import future
import csv
import glob


for csv_file_name in glob.glob("samples/*.csv"):
    with open(csv_file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        headers = reader.fieldnames
        print(headers)
        for line in reader:
            print([line[header] for header in headers])
