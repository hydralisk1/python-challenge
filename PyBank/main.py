import csv
import os

# Function to get total number of months
def get_tot_month(l):
    return len(l)

# Function to get total
def get_total(l):
    return sum(int(i[1]) for i in l)

# Function to get average of change
def get_avg_change(l):
    # (very last profit - very first profit) / (total number of profits - 1), rounded 2 decimal places
    return round((int(l[-1][1]) - int(l[0][1]))/(get_tot_month(l) - 1), 2)

# Function to get greatest increase and decrease
def get_great_change(l):
    diff = [int(l[i][1]) - int(l[i-1][1]) for i in range(1, get_tot_month(l))]
    ''' return 2 x 2 list
                    [0]                      [1]
        ┌──────────────────────────┬─────────────────────┐
     [0]│month of greatest increase│  greatest increase  │
        ├──────────────────────────┼─────────────────────┤
     [1]│month of greatese decrease│  greatest decrease  │
        └──────────────────────────┴─────────────────────┘'''
    return [[l[diff.index(max(diff))+1][0], max(diff)], [l[diff.index(min(diff))+1][0], min(diff)]]

# Function to read csv file
def get_csv_data(filename, header = False):
    path = os.path.dirname(__file__)
    data = []

    with open(os.path.join(path, filename), newline = "", mode = "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
    
        # if csv file has header, skip the first line
        if header:
            next(csv_reader)

        for row in csv_reader:
            data.append(row)

    return data

# Function to print out result
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
    
    # check if writing into file is needed. Default: False
    if(file_write):
        path = os.path.dirname(__file__)
        # to get directory name that user wants
        folder = filename.rsplit("/", 1)[0]

        # to make sure there's no directory having same name
        try:
            os.makedirs(os.path.join(path, "..", folder))
        except OSError:
            pass
        
        # writing into file
        with open(os.path.join(path, filename), mode = "w+") as txt_file:
            for line in result:
                txt_file.write(line+"\n")

rel_path = "Resources/budget_data.csv"
# If CSV file has header, header = True
header = True
data = get_csv_data(rel_path, header)
put_data(data, True)
