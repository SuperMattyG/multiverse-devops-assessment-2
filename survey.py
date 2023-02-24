import sys
from extract import get_input, file_exists

#Ticket #1:   Read a CSV file
#Description: In your input script, create a function that will read data from a CSV file.
#Objectives:  The results.csv data file can be successfully processed into an array.
#             Each line of the file is read into a new array item.
#             The file read method must be in a sub-module.

#Ticket #2:     Remove duplicate entries
#Description:   Add functionality to your input script to ignore or remove any duplicate entries
#from the input data.
#Duplicates are based on the User Id field.
#Objectives:    A final array is created with duplicate entries removed.
#               Where duplicates are found, the first entry is retained.

def get_args():
    try:
        return(sys.argv[1])
    except IndexError:
        print("Please provide only 1 argument!\n")
        print("USAGE: [file name]\n")
        raise IndexError
    except:
        print("Unknown Error! See full details below")
        raise


def main():
    filename = get_args() #Get filename for sys arg
    file_exists(filename) # Check if file exists
    mylist = get_input(filename)



if __name__ == '__main__':
    sys.exit(main())