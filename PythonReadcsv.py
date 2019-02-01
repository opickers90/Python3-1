import csv

with open('phonebook.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=";")
  for row in address_reader:
    print(row)

