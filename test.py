import csv

with open('phones.csv', 'r') as file:
    phones = list(csv.DictReader(file, delimiter=';'))

    for phone in phones:
        ph = (
            phone['id'],
            phone['name'],
            phone['price'],
            phone['image'],
            phone['release_date'],
            phone['lte_exists'],
        )
        print(ph)