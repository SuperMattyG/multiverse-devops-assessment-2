import csv
#Author: matthew Gardner

def get_input(filename):
    #rows = []
    #with open(filename, 'r') as f: #Open as readonly and then append
    #    for line in f.readlines():
    #        rows.append(line.strip().split(","))
    #return rows
    with open(filename, 'r') as f: #Open as readonly and then append
        reader = csv.DictReader(f)

        unique_values = set()

        for row in reader:
            field_value = row ['user_id']

            if field_value not in unique_values:
                unique_values.add(field_value)
                print(row)

def file_exists(filename):
    try:
        open(filename)
    except FileNotFoundError:
        print("File not found")


#def get_input(filename):
#    rows = []
#    with open(filename, 'r') as f: #Open as readonly and then append
#        for line in f.readlines():
#            rows.append(line.strip().split(","))
#    return rows

#with open('file') as f:
#    seen = set()
#    for line in f:
#        line_lower = line.lower()
#        if line_lower in seen:
#            print(line)
#        else:
#            seen.add(line_lower)