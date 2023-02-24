#Author:      Matthew Gardner

#Ticket #1:   Read a CSV file
#Description: In your input script, create a function that will read data from a CSV file.
#Objectives:  The results.csv data file can be successfully processed into an array.
#             Each line of the file is read into a new array item.
#             The file read method must be in a sub-module.

from extract import get_input

def test_input_is_list():
    #Arrange
    filename = "results.csv"
    expected_output = list

    #Act
    output = get_input(filename)

    #Assert
    assert type(output) == expected_output

def test_input_is_correct():
    #Arrange
    filename = "results.csv"
    expected_output = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]

    #Act
    output = get_input(filename)
    output_first_line = output[0]

    #Assert
    assert output_first_line == expected_output

#Ticket #2:     Remove duplicate entries
#Description:   Add functionality to your input script to ignore or remove any duplicate entries
#from the input data.
#Duplicates are based on the User Id field.
#Objectives:    A final array is created with duplicate entries removed.
#               Where duplicates are found, the first entry is retained.