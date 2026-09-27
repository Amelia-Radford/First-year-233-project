# Portfolio Project 3
# user_csv.py
# ENDG 233 F25
# Fiona Welsh and Amelia Radford
# GROUP 5
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

import numpy as np          # import numpy as np
import csv                  # import the csv package
import data_files           # import data files

def read_csv(filename, include_headers):
    """
    Reads a csv file and return a 2D list
    
    Paramaters:
    Takes in the file name needed to read and if the function includes headers or not
    """
    with open(filename, "r") as file:               # open the file and read it
        lines = file.readlines()                    # read the lines

    contents = []                                   # define an emptry list 
    header = lines[0].strip().split(",")            # make sure the string is only the letters

    if include_headers:                             # check if needed to include the headers
        contents.append(header)                     # append the header to the contents

    for line in lines[1:]:                          # iterate through the rows of code after the header line
        row = line.strip().split(",")               # make sure the string is only letters

        processed_row = []                          # reset for each row

        for item in row:                            # iterate through the row
        
            if item.replace(".", "", 1).isdigit():  # check if the item is a number 
                processed_row.append(float(item))   # convert to a float and append
            else:
                processed_row.append(item)          # if not just append the item

        contents.append(processed_row)              # append the processed row 

    return contents


    
#read_csv(Country_Data)

def write_csv(filename, data, overwrite_file):
    '''takes 2D list and adds it to another file or creates a new file. returns the list in a CSV file
        flag- overwtrite indicates whether data should be overwritting or appending to existing file

    Arguments: 
        filename - the name of the file to write to
        data - 2D list containing data that will be written as a CSV'''    

    if overwrite_file == True:                          # check if the function is to overwrite the file or not
        overwrite = "w"                                 # define the variable
    elif overwrite_file == False:
        overwrite = "a"

    written_file = open(filename, overwrite)            # open the file to write in
    
    for row in data:                                    # iterate through the data
            line = ",".join(str(item) for item in row)  # turn the list into a single comma separated line
            written_file.write(line + "\n")             # write the line and then go to the next line

    written_file.close()                                # close the written file
