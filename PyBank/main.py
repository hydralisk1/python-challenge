import csv
import os

def get_tot_month(l):
    return len(l)

def get_total(l):
    return sum(int(i[1]) for i in l)

def get_avg_change(l):
    return round((int(l[-1][1]) - int(l[0][1]))/(len(l) - 1), 2)

def get_great_change(l):
    diff = [int(l[i][1]) - int(l[i-1][1]) for i in range(1, len(l))]
    return [[l[diff.index(max(diff))+1][0], max(diff)], [l[diff.index(min(diff))+1][0], min(diff)]]

def get_csv_data(filename, header = False):
    path = os.path.dirname(__file__)
    data = []

    with open(os.path.join(path, filename), newline = "", mode = "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
    
        for row in csv_reader:
            data.append(row)

    if(header):
        return data
    else:
        return data[1:]

def put_data(l, file_write = False, filename = "analysis/file_write.txt"):
    great_change = get_great_change(l)
    result = []

    result.append("Financial Analysis")
    result.append("----------------------------------------------------")
    result.append(f"Total Months: {get_tot_month(l)}")
    result.append(f"Total: ${get_total(l)}")
    result.append(f"Average Change: ${get_avg_change(l)}")
    result.append(f"Greatest Increase in Profits: {great_change[0][0]} (${great_change[0][1]})")
    result.append(f"Greatest Decrease in Profits: {great_change[1][0]} (${great_change[1][1]})")

    for line in result:
        print(line)
    
    if(file_write):
        path = os.path.dirname(__file__)
        folder = "/".join(filename.split("/")[:-1])

        try:
            os.makedirs(os.path.join(path, folder))
        except OSError:
            pass

        with open(os.path.join(path, filename), mode = "w+") as txt_file:
            for line in result:
                txt_file.write(line+"\n")

rel_path = "Resources/budget_data.csv"
data = get_csv_data(rel_path)
put_data(data, True)