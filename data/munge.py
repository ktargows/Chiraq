import csv

data = []

chicago = open("homicides.csv")
for row in csv.DictReader(chicago):
    origin = "chicago"
    date = row["Date"][:10]
    data.append({"origin":origin, "date":date})

iraq = open("soldiers.csv")
for row in csv.DictReader(iraq):
    origin = "iraq"
    date = row["Date"]
    data.append({"origin":origin, "date":date})

with open("formatted.csv", "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames = ["date", "origin"], lineterminator = '\n')
    writer.writeheader()
    writer.writerows(data)
