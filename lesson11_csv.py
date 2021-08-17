# csv
import csv
from lesson10 import add_suffix_to_filename


def read_csv(filename):
    with open(filename, "r") as csv_file:
        data = []
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            data.append(row)
    return data


def write_csv(filename, data):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


def read_csv_dict(filename):
    with open(filename, "r") as csv_file:
        data = []
        reader = csv.DictReader(csv_file, delimiter=";")
        for row in reader:
            data.append(row)
    return data


def write_csv_dict(filename, data):
    # fieldnames = data[0].keys()
    fieldnames = ["S1", "S5", "S2", "S3"]
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


filename = "data.csv"
data = read_csv_dict(filename)
print(data)
data.append({key: int(data[-1][key]) * 2 for key in data[-1]})
for row in data:
    row["S5"] = int(row["S2"]) + int(row["S3"])

new_filename = add_suffix_to_filename(filename, 'import')
write_csv_dict(new_filename, data)

# data.append([int(val) * 2 for val in data[-1]])
# data[0].append("S4")
# for row in data[1:]:
#     row.append(int(row[-1]) + int(row[-2]))

# new_filename = add_suffix_to_filename(filename, 'add')
# write_csv(new_filename, data)
