import csv
import os

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

# Function to get result
def get_result(l):
    l = [i[2] for i in l]

    # remove duplicates
    names = list(set(l))
    ''' return list
    [[candidate, number of votes for candidate]]
    '''
    return [[names[i], l.count(names[i])] for i in range(len(names))]

# Function to print out result
def put_data(l, file_write = False, filename = "analysis/file_write.txt"):
    result = []

    election_result = get_result(l)
    tot_votes = sum([i[1] for i in election_result])
    
    # descending sort by number of votes
    election_result.sort(key=lambda x:x[1], reverse=True)

    result.append("Election Results")
    result.append("-------------------------")
    result.append(f"Total Votes: {tot_votes}")
    result.append("-------------------------")

    for i in election_result:
        vote_ptg = round(i[1]/tot_votes*100, 3)
        result.append(f"{i[0]}: {format(vote_ptg, '.3f')}% ({i[1]})")

    result.append("-------------------------")
    result.append(f"Winner: {election_result[0][0]}")
    result.append("-------------------------")
    
    for line in result:
        print(line)
    
    # check if writing into file is needed. Default: False
    if(file_write):
        path = os.path.dirname(__file__)
        # to get directory name that user wants
        folder = os.path.dirname(filename)
        
        # to make sure there's no directory having same name
        try:
            os.makedirs(os.path.join(path, folder))
        except OSError:
            pass
        
        # writing into file
        with open(os.path.join(path, filename), mode = "w+") as txt_file:
            for line in result:
                txt_file.write(line+"\n")

rel_path = "Resources/election_data.csv"
# If csv file has header, header = True
header = True
data = get_csv_data(rel_path, header)
put_data(data, True)
