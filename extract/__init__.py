import csv
#Author: matthew Gardner

#def get_input() - Covers this Ticket
#Ticket #1:   Read a CSV file
#Description: In your input script, create a function that will read data from a CSV file.
#Objectives:  The results.csv data file can be successfully processed into an array.
#             Each line of the file is read into a new array item.
#             The file read method must be in a sub-module.

#def get_input() - Covers this Ticket
#Ticket #2:     Remove duplicate entries
#Description:   Add functionality to your input script to ignore or remove any duplicate entries
#from the input data.
#Duplicates are based on the User Id field.
#Objectives:    A final array is created with duplicate entries removed.
#               Where duplicates are found, the first entry is retained.

#def get_input() - Covers this Ticket
#Ticket #3:     Ignore empty lines
#Description:   Update your input script to ignore any empty lines found when reading in the
#               input data file.
#Objectives:    A final array is created with any empty lines omitted.

#Ticket #4:     Capitalise user name fields
#Description:   Add functionality to your input script to automatically capitalise the first_name
#               and last_name fields found in the input data.
#Objectives:    All names are capitalised in all data entries

def get_input(filename):

    #Initialise list that values will be appneded to
    cleansed_list=[]
    final_list=['user_id','first_name','last_name','answer_1','answer_2','answer_3']

    with open(filename, 'r') as f: #Open the input file
        
        #Read the CSV file into a list of dictionaries
        #Ticket #1
        reader = csv.DictReader(f)
        
        #Create a set to store unique values
        #Ticket #2
        unique_values = set()

        #Iterate over each row in the input file
        for row in reader:
            #Get the value of the field to check for duplicates
            field_value = row ['user_id']
            
            #If the value has not already been seen, add it to the set and write the row to the output file
            if field_value not in unique_values:
                #Ticket #3: If statement to cover off Ticket 3.  Will ignore empty lines
                if len(field_value) > 0:
                    unique_values.add(field_value)
                    cleansed_list.append(row)
        
        #Ticket #4: capitilize name field
        #changing from list of dictionaries to a final list
        i = 0
        for rows in cleansed_list:
            final_list.append(cleansed_list[i]['user_id'])
            final_list.append(cleansed_list[i]['first_name'].capitalize())
            final_list.append(cleansed_list[i]['last_name'].capitalize())
            final_list.append(cleansed_list[i]['answer_1'])
            final_list.append(cleansed_list[i]['answer_2'])
            final_list.append(cleansed_list[i]['answer_3'])
            i += 1

    return list(final_list)

def file_exists(filename):
    try:
        open(filename)
    except FileNotFoundError:
        print("File not found")
    return

def capitalize_name():
    for capitilized_list in cleansed_list:
        #capitilized_list[0] = capitilized_list[0]
        print(cleansed_list[2])
    return
