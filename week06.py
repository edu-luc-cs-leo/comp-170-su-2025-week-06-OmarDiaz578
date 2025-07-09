



filepath = "/workspaces/comp-170-su-2025-week-06-OmarDiaz578/data/"
#Path to the file without name
name = "temperatures.txt"
#Name of the file

#Load and Analyze Temperature Data
def load_to_list(filepath: str) -> list[float]:
    #This function reads the file given line by line, converts each line to float
    #Then stores the values in a list which it returns
    final_list: list[float] = []
    #Makes the empty list to store float values
    with open(filepath+name, "r") as temp_file:
        #Connects to file for reading and gives it an alias
        for line in temp_file:
            #A loop to go through  every line and convert to float
            #Then adds it to the empty list
            value: float = float(line)
            final_list.append(value)
    return final_list
    #Returns the completes list of temperatures

def descriptive_statistics(source_data: list[float]) -> None:
    #This function receives a list if float numbers and prints:
    #The total number of items
    #The average value(rounded)
    #And the min and max values
    count: int = len(source_data)
    #Counts the total number of temperatures
    total: float = 0.0
    #Stores the sum of all values
    min_temp: float = source_data[0]
    #Assumes the first element is min
    max_temp: float = source_data[0]
    #Assumes the first element is max

    for temp in source_data:
    #A loop that goes through every temp value in the list
        total += temp
        #Adds current tempt to total
        if temp < min_temp:
            min_temp = temp
        if temp > max_temp:
            max_temp = temp
        #Updates the min or max temp if needed
    average: float = round(total / count, 2)
    #Calculates the average temp
    print(f"There are {count} values in the data source.")
    print(f"The average value is {average}.")
    print(f"The highest value is {max_temp} and the smallest value is {min_temp}.")
    #Prints messages with appropriate values


source_data: list[float] = load_to_list(filepath)
#Calls the function load_to_list and returns a list which ten is tored in source_data
descriptive_statistics(source_data)
#Calls the function descriptive_statistics and passes the float list in source_data as an argument



filepath = "/workspaces/comp-170-su-2025-week-06-OmarDiaz578/data/"
#Path to the file without name
name = "markup.txt" 
#Name of file



#Apply Simple Markup to Text
def apply_markup(filepath: str) -> None:
#This function reads a file line by line
#A word that starts with "." is printed in uppercase
#A word that starts with "_" is printed in expanded form (a space in between each letter)
#All other words print normally
    with open(filepath+name, "r") as mark_file:
    #Connects to file and gives it an alias
        lines: list[str] = mark_file.readlines()
        #Read all lines into a tuple
        for line in lines:
        #Goes through each line of the file one by one
            individual_words: list[str] = line.strip().split()
            #Removes newline characters and splits the line into individual words
            individual_line: str = ""
            #Creates a string to store ecah word
            for word in individual_words:
            #A loop that goes through every word in the string
                if word.startswith("."):
                    new_word: str = word[1:].upper()
                elif word.startswith("_"):
                    characters: list[str] = list(word[1:])
                    new_word: str = " ".join(characters)
                else:
                    new_word: str = word
                individual_line += new_word + " "
            #Formats the word accordingly depending with what they begin with
            print(individual_line.strip())
            #After every word is processed, removes trailing space and prints the line

apply_markup(filepath)
#Calls the function apply_markup



























































#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

