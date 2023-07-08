import sys
import csv
import json

def csv_to_json(csvFileName, jsonFileName):
    data = {}

    with open(csvFileName, 'r', encoding='cp850') as file:
        reader = csv.DictReader(file)

        for rows in reader:
            key = rows['Number']
            itemList = {}
            for item in rows['Items'].split(';'):
                temp = {}
                for field in item.split('|'):
                    splitLoc = field.index(':')
                    temp[field[:splitLoc]] = field[splitLoc + 1:]
                itemList[len(itemList)] = temp
            rows['Items'] = itemList
            data[key] = rows

    with open(jsonFileName, 'w', encoding='cp850') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

csv_to_json(sys.argv[1], sys.argv[2])
