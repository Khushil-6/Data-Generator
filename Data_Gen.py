import csv
import random
import time

xvalue = 0
newValue_1 = 1000
newValue_2 = 1000

fieldnames = ['xvalue', 'newValue_1', 'newValue_2']

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

        info = {
            'xvalue' : xvalue,
            "newValue_1" : newValue_1,
            "newValue_2" : newValue_2
        }

        csv_writer.writerow(info)
        print(xvalue, newValue_1, newValue_2)

        xvalue += 1
        newValue_1 = newValue_1 + random.randint(-4,8)
        newValue_2 = newValue_2 + random.randint(-5,9)

    time.sleep(3)