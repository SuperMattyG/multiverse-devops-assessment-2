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

def get_input(filename):

    #Initialise list that values will be appneded to
    expected_output=[]

    with open(filename, 'r') as f: #Open the input file
        
        #Read the CSV file into a list of dictionaries
        reader = csv.DictReader(f)
        
        #Create a set to store unique values
        unique_values = set()

        #Iterate over each row in the input file
        for row in reader:
            #Get the value of the field to check for duplicates
            field_value = row ['user_id']
            
            #If the value has not already been seen, add it to the set and write the row to the output file
            if field_value not in unique_values:
                #If statement to cover off Ticket 3.  Will ignore empty lines
                if len(field_value) > 0:
                    unique_values.add(field_value)
                    #print(row)
                    expected_output.append(row)
    
    #Print final list of values.
    print(expected_output)


def file_exists(filename):
    try:
        open(filename)
    except FileNotFoundError:
        print("File not found")