# Portfolio Project 3
# functions.py
# ENDG 233 F25
# Fiona Welsh and Amelia Radford
# GROUP 5
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

import numpy as np                              # Import numpy in order to use

def to_numpy_2d(list_2d):
    """
    Converts a 2D list (list of lists) into a 2D numpy array.

    Paramaters:
    Takes in a 2D list

    Returns: 
    The same data set as a 2D numpy array
    """
    return np.array(list_2d, dtype=object)      # return the 2D list as an np array


def merge_rows(rowdata1, rowdata2, rowdata3):
    """
    Combines the rows of corresponding data sets, while assuring no duplicates

    Paramaters: 
    Takes in three 1D lists for three rows of corresponding data

    Returns:
    A combined 1D list of values wihtout duplicates
    """
    seen = set()                                                        # Set a variable to check if the value has been seen or not
    merged = []                                                         # Set an empty list for the merged rows
    for row in (rowdata1 or [], rowdata2 or [], rowdata3 or []):        # Iterate through the rows of data
        for value in row:                                               # Iterate through the list
            if value not in seen:                                       # Prevent duplicates
                merged.append(value)                                    # Append the value to the list of merged
    return merged                                                       # Return the merged list

def merge_2d_lists(data1, data2, data3):
    """
    Combines three 2D lists into one 2D list
    
    Paramaters:
    Takes in three sets of 2D data

    Returns:
    A combined 2D list, where each row of data is added to the corresponding row of the other data sets
    """
    max_rows = max(len(data1 or []), len(data2 or []), len(data3 or []))    # get the maximum lenth of any of the lists
    merged = []                                                             # Set an empty list for the merged rows
    for i in range(max_rows):                                               # Iterate through the list
        r1 = data1[i] if i < len(data1) else []                             # for each index get the row if it exists, otherwise return an empty list
        r2 = data2[i] if i < len(data2) else []
        r3 = data3[i] if i < len(data3) else []
        merged.append(merge_rows(r1, r2, r3))                               # merge the rows and then append them to the 2D list
    return merged

def extract_column(data, index):
    """
    Returns a 1D list from a 2D list.

    Paramaters:
    Takes a 2D list (list of rows) and an index

    Returns:
    A 1D list containing that element from each row.
    """
    column = []                         # define an empty list
    for row in data:                    # iterate through the data
        if len(row) > index:            # Safely handle rows that may be too short
            column.append(row[index])   # append the index from the row
        else:
            column.append(None)         # return that there is no index
    return column
 
