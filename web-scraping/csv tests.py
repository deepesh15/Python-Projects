import csv
filename = "1000 words in german.csv"
field  =["S.no","German","English"]
with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(field)
