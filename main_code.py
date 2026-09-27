# Portfolio Project 3
# main_code.py
# ENDG 233 F25
# Fiona Welsh and Amelia Radford
# GROUP 5
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.


import numpy as np                                                                # import numpy
import matplotlib.pyplot as plt                                                   # import matplotlip
from user_csv import read_csv, write_csv                                          # import required functions
from functions import to_numpy_2d, merge_rows, merge_2d_lists, extract_column     # import fumctions from functions.py
import data_files                                                                 # import the csvs from data_files 


def main_menu():
    """
    Prints the main menu thats prompts the user to select
        an option and returns a valid option number

    Returns:
        int: a valid input provided by the user
    """
    print("You have reached the main menu. Please select an option:")
    while True:                                                         # while loop to keep asking selection until user enters valid or quits entirely
        print("Enter the number of the option you want to select:")     # print this to let the user know there is a menu
        print(f"\t1) Play game")                                        # option 1
        print(f"\t2) See current user stats")                           # option 2
        print(f"\t3) end program")                                      # option 3
        choice = input(">> ")                                           # ask for what option user wants and include greater than signs to differentiate user input
        

        if choice in ["3", "1", "2"]:                           # check if choice is valid
            return int(choice)                                  # return the valid choice as an interger
        else:                                                   # if not a valid input
            print()                                             # print a blank line
            print("Error! Invalid input. Please try again.\n")  # print error statement if choice is not valid

def get_pop_change(country, array):
    """
    Returns the change in population from 2000 to 2020 of a country
    
    parameters:
        country = chosen country
        array = 2d numpy array with the following relevant data
            Row 0 = headers
            Column 0 = country name
            Col 1 = 2020 population
            Col 21 = 2000 population
    
    Returns:
        change in pop from 2000 to 2020 or None if not found
    """

    for row in array[1:]:                                           # skip header
        if str(row[0]).upper().strip() == country.upper().strip():  # check if country matches (case insensitive, strip spaces)

            pop_2020 = row[1]                                       # get populations
            pop_2000 = row[21]                      

            if pop_2020 == "" or pop_2000 == "":                    # Handle missing data (empty strings stored in numpy arrays)
                return "None"                                       # return None if data is missing

            return pop_2020 - pop_2000                              # return change in population  

    return "None"                                                   # return None if country not found 


def get_species_most_endangered(country, data):
    """
    takes the max of numbers in a row and returns the header of the row
    
    Parameters:
        data: 2D numpy array (dtype=object)
        country: given country

    Returns:
        header of max value in row of country
    """
    headers = data[0]                                               # header row: ['Country', 'Mammals', 'Birds', 'Fish', 'Plants']

    for row in data[1:]:                                            # skip header
        if str(row[0]).upper().strip() == country.upper().strip():  # check if country matches (case insensitive, strip spaces)

            species_counts = row[1:]                                # the numeric values
            max_index = int(np.argmax(species_counts))              # index of max value in species_counts

            return headers[max_index + 1]                           # +1 to account for country name column


def get_country_area(country, data):
    """ 
    finds the maximum area of a country from the data file

    Parameters:
        country (str): Name of the country.
        data (2D numpy array, dtype=object): 
            Column 0 = country name
            Column 3 = area in Sq Km
            
    Returns:
        float: Area in Sq Km or 'None' if not found.
"""
    for row in data[1:]:                                            # skip header
        if str(row[0]).upper().strip() == country.upper().strip():  # check if country matches (case insensitive, strip spaces)

            area_value = row[3]                                     # Sq Km column

            if area_value == "":                                    # Handle missing data (empty strings stored in numpy arrays)
                return "None"                                       # return None if data is missing

            return float(area_value)                                # return area as float 



def compare_values(value_1, value_2):
    """
    Compares two values.
    - Returns True if exactly equal.
    - Returns percent difference if both are numbers.
    
    Parameters:
        value_1: First value to compare (str or float).
        value_2: Second value to compare (str or float).
        
    Returns:
        True if values are exactly equal.
        Float percent difference if both values are numeric.
        0.0 if either value is "None".
    """
    if value_1 == "None" or value_2 == "None":                                                      # check if either value is None  
        return 0.0                                                                                  # return 0.0 if they are none                             
    
    if str(value_1).replace(".", "", 1).isdigit() and str(value_2).replace(".", "", 1).isdigit():   # Convert to float if possible
        value_1_f = float(value_1)                                                                  # convert to float  
        value_2_f = float(value_2)                                                                  # convert to float                                            

    if value_1_f == value_2_f:                                                                      # check if values are exactly equal    
            return 0.0                                                                              # return 0.0 if they are equal                                 

    return ((value_2_f - value_1_f) / value_1_f) * 100                                              # therwise return percent difference       


def compare_str(value_1, value_2):
    """
    Compares two strings for equality, ignoring case and leading/trailing whitespace.
    
    Parameters:
        value_1: First string to compare (str).
        value_2: Second string to compare (str).
        
    Returns:
        True if strings are equal (case-insensitive, trimmed), False otherwise.
    """
    if value_1.upper().strip() == value_2.upper().strip():  # compare case insensitive and strip spaces
        return True                                         # return true if equal

    return False                                            # return false if not equal


def print_closeness(accuracy, category):
    """
    Prints feedback based on the accuracy of a guess.
    Parameters:
        accuracy: True if correct, False if incorrect, or float percent difference.
        category: Description of the category being compared (str).  
        """
    if accuracy == True:                                                                                # if accuracy is true
        print(f"Your guessed country's {category} is correct!")                                         # print correct statement

    elif accuracy == 0.0 or accuracy == False:                                                          # if accuracy is false or 0.0   
        print(f"Your guessed country's {category} is incorrect.")                                       # print incorrect statement 

    else:                                                                                               # if accuracy is a float percent difference       
        if accuracy < 0:                                                                                # if accuracy is negative    
            accuracy = accuracy * -1                                                                    # make accuracy positive for printing    
            print(f"Your guessed country's {category} is incorrect. You are {accuracy:.1f}% too high.") # print too high statement

        else:                                                                                           # if accuracy is positive      
            print(f"Your guessed country's {category} is incorrect. You are {accuracy:.1f}% too low.")  # print too low statement
          

def fail_menu():
    """Prints the fail menu and prompts the user to select an option.

    Returns:
        int: a valid input provided by the user
    """
    
    while True:                                                         # while loop to keep asking selection until user enters valid option    
        print("Please choose an option from the menu below:")           # print this to let the user know there is a menu
        print(f"\t1) Contiue guessing")                                 # option 1  
        print(f"\t2) Use one of the three availible hints")             # option 2
        print(f"\t3) Give up :(")                                       # option 3
        choice = input(">> ").strip()                                   # ask for what option user wants and include greater than signs to differentiate user input
        
        if choice in ["1","2","3"]:                                     # check if choice is valid 
            return choice                                               # return int(choice)
    
        else:                                                           # if not a valid input    
            print("Oops, invalid selection. Try again!")                # print error statement if choice is not valid and continue asking for selection

def rank_country_by_pop_change(country, data):
    """
    Ranks the specified country by its population change from 2000 to 2020 among all countries.

    Parameters:
        country (str): Name of the country.
        data (2D numpy array, dtype=object): 
            Column 0 = country name
            Column 1 = 2020 population
            Column 21 = 2000 population
            
    Returns:
        int: Rank of the country based on population change (1 = highest change).
    """

    changes = np.array([float(row[1])-float(row[21]) for row in data[1:]])  # calculate changes for all countries
    countries = [row[0] for row in data[1:]]                                # list of country names
    
    country_index = countries.index(country)                                # find index of specified country
    country_change = changes[country_index]                                 # get change for specified country
    
    rank = (changes > country_change).sum() + 1                             # rank is number of countries with greater change + 1
    return rank                                                             # return rank   

def get_country_continent(country, country_array):
    """
    Returns the continent of the specified country.
    
    Parameters:
        country (str): Name of the country.
        country_array (2D numpy array, dtype=object): 
            Column 0 = country name
            Column 1 = continent
            
    Returns:
        str: Continent name or 'Not available' if not found.
    """
    country_upper = country.upper().strip()                  # standardize country name for comparison  
    
    for row in country_array[1:]:                           # skip header
        if str(row[0]).upper().strip() == country_upper:    # check if country matches (case insensitive, strip spaces)
            continent = row[1]                              # get continent
            return continent                                # return continent
    else:
        return "Not availible"                              # return not availible if country not found

   
def get_user_guess(data):
    """
    Prompts the user to input a country guess and validates it against the provided data.

    Parameters:
        data (list): List of valid country names.
        
    Returns:
        str: Validated country name guessed by the user.
    """
       
    print()  
    while True:
        print("What do you think the mystery country is?:")                             # prompt user for country guess
        guess = str(input(">> "))                                                       # get user input
        
        guess_upper = guess.upper().strip()                                             # ensure case and speces are not an issue 
        
        valid_guess = False                                                             # set flag to see if guess is valid
        for name in data[1:]:                                                           # iterate through country list to check if guess is valid
            name = str(name).upper().strip()                                            # ensure case and spaces are not an issue
            if name == guess_upper:                                                     # check if guess matches country name   
                valid_guess = True                                                      # change flag to true

        if valid_guess == True:                                                         # if existing country is found:                                                        
            return guess_upper                                                          # return valid country to continue program
            
        print("Error! Invalid input. Check your spelling and if the country exists.")   # print error statement if guess is not valid and prompt user to try again
        print("Please try again\n")    


def display_guessing_per_round_stats(guesses):
    """
    Displays a bar chart of the number of guesses per round.
    
    Parameters:
        guesses (list): List of integers representing the number of guesses per round.
    """
    
    rounds = [i for i in range(1, len(guesses) + 1)]    # create list of round numbers

    plt.figure(figsize=(15, 5))                         # set figure size
    
    plt.subplot(1, 3, 1)                                # Create subplot first
    plt.xticks(rounds)                                  # set x ticks   
    plt.yticks(range(0, max(guesses) + 1))              # set y ticks

    plt.bar(rounds, guesses)                            # create bar chart
    plt.ylabel("Number of Guesses")                     # set y label
    plt.xlabel("Round Number")                          # set x label
    plt.title("Guesses per Round")                      # set title 

    plt.tight_layout()                                  # adjust layout
    plt.savefig("final_plots/guess_stats.png")          # save figure
    plt.close()                                         # close plot

   

def display_closeness_stats(list_1, list_2):
    """
    Displays line plots of population change closeness and area change closeness per round.
    
    Parameters:     
        list_1 (list of lists): 2D list where each sublist contains percent errors for population change per round.
        list_2 (list of lists): 2D list where each sublist contains percent errors for area change per round.
    """
    plt.figure(figsize=(14, 6))                                                 # set figure size     

    plt.subplot(1, 2, 1)                                                        # Population subplot  
    for round_num, round_data in enumerate(list_1, start=1):                    # iterate through rounds
        guesses = list(range(1, len(round_data) + 1))                           # create list of guess numbers
        plt.plot(guesses, round_data, marker='o', label=f'Round {round_num}')   # plot line with markers
        plt.scatter(guesses, round_data)                                        # scatter points   

    plt.title("Population Change Closeness per Round")                          # set title
    plt.xlabel("Guess Number")                                                  # set x label  
    plt.ylabel("Percent Error")                                                 # set y label   
    plt.legend()                                                                # show legend     
    plt.grid(True)                                                              # show grid    
  
    plt.subplot(1, 2, 2)                                                        # Area subplot  
    for round_num, round_data in enumerate(list_2, start=1):                    # iterate through rounds
        guesses = list(range(1, len(round_data) + 1))                           # create list of guess numbers
        plt.plot(guesses, round_data, marker='s', label=f'Round {round_num}')   # plot line with markers
        plt.scatter(guesses, round_data)                                        # scatter points    

    plt.title("Area Change Closeness per Round")                                # set title 
    plt.xlabel("Guess Number")                                                  # set x label     
    plt.ylabel("Percent Error")                                                 # set y label    
    plt.legend()                                                                # show legend       
    plt.grid(True)                                                              # show grid   

    plt.tight_layout()                                                          # adjust layout    
    plt.savefig("final_plots/pop_and_area_stats.png")                           # save figure
    plt.close()                                                                 # close plot   
   


#*******************************************************************************************************************************************
# main code

include_headers = True                                                                                                  # set include headers to true   

country_data_list = read_csv("data_files/country_data.csv", include_headers)                                            # read in country data csv  
pop_data_list = read_csv("data_files/population_data.csv",  include_headers)                                            # read in population data csv
threatened_species_list = read_csv("data_files/threatened_species.csv", include_headers)                              # read in threatened species data csv

np_country_data_list = to_numpy_2d(country_data_list)                                                                   # convert country data to numpy array
np_pop_data_list = to_numpy_2d(pop_data_list)                                                                           # convert population data to numpy array
np_threatened_species_list = to_numpy_2d(threatened_species_list)                                                       # convert threatened species data to numpy array

guess_count_list = []                                                                                                   # set list for number of guesses per round  
user_total_pop_guesses = []                                                                                             # set total list for user's guess closeness including every round (will be 2d list)
user_total_area_guesses = []                                                                                            # set total list for user's guess closeness including every round (will be 2d list)
overwrite_file = True                                                                                                   # set overwrite file to true
output_file_list = merge_2d_lists(country_data_list, pop_data_list , threatened_species_list)                           # merge all three data files for output csv - used in hint 3
only_countries_list = extract_column(country_data_list, 0)                                                              # get list of only countries from country data file 

print("Welcome to our country guessing game!")                                                                          # welcome user and give instructions
print()
print("How to play: You are trying to guess a random country by only knowing the change in population from 2000-2020, most endangered species, and area.") 
print("After every guess you will recieve feedback on your accuracy. If you are struggling, you have three hints per round.")
print("Good luck!")
user_input = input("press enter to continue: ")                                                                         # prompt user to press enter to continue        


main_choice = main_menu()                                                                                               # set main choice

while main_choice == 1 or main_choice == 2:                                                                             # while user chooses to play game or see stats    
    while main_choice == 1:                                                                                             # if user chooses to play game 

        chosen_country = np.random.choice(only_countries_list)                                                          # randomly choose a country from the list of countries
      
        pop_change = get_pop_change(chosen_country, np_pop_data_list)                                                   # get pop change of chosen country from 2000 to 2020 
        endangered_species = get_species_most_endangered(chosen_country, np_threatened_species_list)                    # get most endangered species of chosen country
        country_area = get_country_area(chosen_country, np_country_data_list)                                           # get area of chosen country

        print("Three facts about the mystery country:")                                                                 # give user facts
        if pop_change != "None":                                                                                        # check if pop change data is availible
            print(f"The population change is {pop_change} people from 2000 to 2020")                                    # give user facts about country (call functions to calculate for country)
        else:                   
            print("There is no data availible for the country's change in population")                                  # print if pop change data is missing
        print(f'The most endangered species is {endangered_species}')                                                   # give user most endangered species
        if country_area != "None":                                                                                      # check if country area data is availible                   
            print(f'The area of the country is {country_area}Km^2')                                                     # give user counry area
        else:
            print(f"The country's area is unavailible.")                                                                # if country area is very small or missing print this
        
        
        condolences_list = [
            "Aw Snap! Not this time!", "Haha you didnt guess it.", "Nope. #getbetter", "You guessed it! (almost)", 
            "Womp Womp", "Hey, at least you committed to that guess.", "We checked. Triple-checked. Still no.",
            "Congratulations! You’ve discovered the opposite of the correct answer.",
            "Not correct, but a fantastic example of confidence."]                                                      # have a list of condolences to give loser when they dont guess it
        empty_list = []                                                                                                 # set empty list for resetting combined output file csv
        win_flag = 0                                                                                                    # set win status this round
        hint_count = 0                                                                                                  # set how many hints the user has used
        guess_count = 0                                                                                                 # set how many guesses the user has taken this round
        round_pop_guesses = []                                                                                          # set population guess closeness list for this round
        round_area_guesses = []                                                                                         # set area guess closeness for this round
        write_csv("combined_output.csv", empty_list, overwrite_file)

        country_guess_unformatted = get_user_guess(only_countries_list)                                                 # get the user's guess
        country_guess = country_guess_unformatted.upper().strip()                                                       # format the user's guess to be case insensitive and strip spaces
        guess_count += 1                                                                                                # increment guess count 

        if country_guess == chosen_country.upper().strip():                                                             # check if user guessed correctly on first try
            win_flag = 1                                                                                                # set win flag to 1 if they did
        
        while win_flag == 0:                                                                                            # 0 = ongoing

            if country_guess == chosen_country.upper().strip():                                                         # Check if the guess is correct
                win_flag = 1                                                                                            # set win flag to 1 if they did 

            if win_flag == 0:                                                                                           # only show condolence and fail menu if not won
                condolence = np.random.choice(condolences_list)                                                         # find random condolence message
                print()                                       
                print(condolence)                                                                                       # print condolence message        
                
                
                guessed_change = get_pop_change(country_guess, np_pop_data_list)                                        # get guessed pop change
                guessed_species = get_species_most_endangered(country_guess, np_threatened_species_list)                # get guessed most endangered species
                guessed_area = get_country_area(country_guess, np_country_data_list)                                    # get guessed country area 

                change_closeness = compare_values(pop_change, guessed_change)                                           # compare guessed pop change to actual pop change
                species_closeness = compare_str(endangered_species, guessed_species)                                    # compare guessed most endangered species to actual most endangered species
                area_closeness = compare_values(guessed_area, country_area)                                             # compare guessed country area to actual country area

                round_pop_guesses.append(abs(change_closeness))                                                         # append absolute value of closeness to round pop list 
                round_area_guesses.append(abs(area_closeness))                                                          # append absolute value of closeness to round area list

                print()
                print_closeness(change_closeness, "Change in Population")                                               # print closeness feedback for each category    
                print_closeness(species_closeness, "Endangered Species")                                                # print closeness feedback for each category    
                print_closeness(area_closeness, "Country Area")                                                         # print closeness feedback for each category        
                print()


                fail_menu_ans = fail_menu()                                                                             # Ask the user what they want to do next

                if fail_menu_ans == "1":                                                                                # continue guessing
                    country_guess = get_user_guess(only_countries_list)                                                 # ask user their next guess
                    guess_count += 1                                                                                    # add one to guess count

                elif fail_menu_ans == "2":                                                                              # use a hint
                    hint_count += 1                                                                                     # add one to hint count
                    
                    if hint_count == 1:                                                                                 # first hint
                        print("Hint one!")
                        rank = rank_country_by_pop_change(chosen_country, np_pop_data_list)                             # get rank of country by pop change
                        print(f"This country ranks {rank} in population change from 2000-2020 among all countries.")    # print rank
                    
                    elif hint_count == 2:                                                                               # second hint
                        print("Second hint!")                                                       
                        continent = get_country_continent(chosen_country, np_country_data_list)                         # get continent of country
                        if continent[-1] == "s":                                                                        # check if continent ends in s for grammar purposes
                            print(f"This country is located in the {continent}.")                                       # print continent for plural continents (Americas)   
                        elif continent == "Not availible":                                                              # check if continent is not availible
                            print("The country's continent cannot be found")                                            # print not availible statement      
                        else:
                            print(f"This country is located in {continent}.")                                           # print continent for singular continents (Asia)               
                    
                    elif hint_count == 3:                                                                               # third hint                                   
                        print("Last hint!")
                        print("There is now a csv called combined_output.csv with all data.")                           # inform user of combined output file
                        print("You are welcome to go through it to try and find your country. It might take a while!")  # invite user to look through csv
                        print("This list will be removed once you finish this round")                                   # inform user that file will be removed after round
                        write_csv("combined_output.csv", output_file_list, overwrite_file)                              # write combined output file for user to look through

                    else:
                        print("Trying to get another hint? It's not gonna work.")                                       # inform user they have used all hints

                    country_guess = get_user_guess(only_countries_list)                                                 # ask user their next guess  
                    guess_count += 1                                                                                    # add one to guess count    

                elif fail_menu_ans == "3":                                                                              # give up
                    print(f"You gave up! The country was: {chosen_country}")                                            # print the loser message with the correct country   
                    win_flag = -1                                                                                       # set win flag to -1 for giving up                                      

                    
        if win_flag == 1:                                                                                               # if user won the round                                  
            print()
            print(f"Congratualtions! You guessed it! The country was {chosen_country}!")                                # print winner message with correct country        
            print(f'It took you {guess_count} guesses to get there using {hint_count} hints!')                          # print how many guesses and hints were used
            print()

            round_pop_guesses.append(0)                                                                                 # append 0 to round pop guesses for winning guess   
            round_area_guesses.append(0)                                                                                # append 0 to round area guesses for winning guess  

        user_total_pop_guesses.append(round_pop_guesses)                                                                # append round pop guesses to total pop guesses        
        user_total_area_guesses.append(round_area_guesses)                                                              # append round area guesses to total area guesses           
        guess_count_list.append(guess_count)                                                                            # append guess count to guess count list 
        
        main_choice = main_menu()                                                                                       # ask user main menu choice again        

    if main_choice == 2:                                                                                                # if user chooses to see stats
        print()
    
        if len(guess_count_list) > 1:                                                                                   # check if at least two rounds have been played to show stats   
            print("Graphs of your stats are saved under the 'final plots' folder.")                                     # inform user where graphs are saved
            print("They are not displayed in the desktop")                                                              # inform user they are not displayed in desktop                                   
            print("Your average number of guesses per round is:", np.mean(guess_count_list))                            # print average number of guesses per round
            display_guessing_per_round_stats(guess_count_list)                                                          # display the stats of guesses per round
            display_closeness_stats(user_total_pop_guesses, user_total_area_guesses)                                    # display the closeness of pop and area    
        else:
            print("Stats are unavailible until two rounds have been played. Keep playing!")                             # inform user that stats are unavailible until two rounds have been played
    
        print()
        main_choice = main_menu()                                                                                       # ask user main menu choice again  

if main_choice == 3:                                                                                                    # if user chooses to quit                                  
    print("Thank you for playing!")                                                                                     # thank user for playing                            
    print("Goodbye!")                                                                                                   # say goodbye to user       
    