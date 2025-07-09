



filepath = "/workspaces/comp-170-su-2025-week-06-OmarDiaz578/data/" #temperatures.txt"
name = "temperatures.txt"

#Load and Analyze Temperature Data
def load_to_list(filepath: str) -> list[float]:
    final_list: list[float] = []
    with open(filepath+name, "r") as temp_file:
        for line in temp_file:
            value: float = float(line)
            final_list.append(value)
    return final_list

def descriptive_statistics(source_data: list[float]) -> None:
    count: int = len(source_data)
    total: float = 0.0
    min_temp: float = source_data[0]
    max_temp: float = source_data[0]

    for temp in source_data:
        total += temp
        if temp < min_temp:
            min_temp = temp
        if temp > max_temp:
            max_temp = temp
    average: float = round(total / count, 2)
    print(f"There are {count} values in the data source.")
    print(f"The average value is {average}.")
    print(f"The highest value is {max_temp} and the smallest value is {min_temp}.")


source_data: list[float] = load_to_list(filepath)
descriptive_statistics(source_data)

filepath = "/workspaces/comp-170-su-2025-week-06-OmarDiaz578/data/"
name = "markup.txt" 

def apply_markup(filepath: str) -> None:
    with open(filepath+name, "r") as mark_file:
        lines: list[str] = mark_file.readlines()
        for line in lines:
            individual_words: list[str] = line.strip().split()
            individual_line: str = ""
            for word in individual_words:
                if word.startswith("."):
                    new_word: str = word[1:].upper()
                elif word.startswith("_"):
                    characters: list[str] = list(word[1:])
                    new_word: str = " ".join(characters)
                else:
                    new_word: str = word
                individual_line += new_word + " "
            print(individual_line.strip())

apply_markup(filepath)



























































#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

