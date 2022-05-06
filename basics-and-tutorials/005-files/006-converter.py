import json

csv_file = '006-csv-file.txt'

with open(csv_file, 'r') as c:
    with open('006-json-file.txt', 'w') as j:
        lines = c.read().split('\n')
        filtered = [line.replace('\n', '') for line in lines]
        clubs = []
        for line in filtered:
            club , city,  country =  line.split(',')
            clubs.append({'club': club, 'country': country, 'city': city.strip()})

        json.dump(clubs, j)
