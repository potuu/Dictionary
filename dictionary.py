import json
from difflib import get_close_matches

def load_data_from_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: The data file could not be found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to load data from the JSON file.")
        return {}


def translate(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    elif word.title() in dictionary:
        return dictionary[word.title()]
    elif word.upper() in dictionary:
        return dictionary[word.upper()]
    else:
        close_matches = get_close_matches(word, dictionary.keys())
        if close_matches:
            yn = input(f"Did you mean {close_matches[0]} instead? Enter Y if yes, or N if no: ")
            if yn.upper() == "Y":
                return dictionary[close_matches[0]]
            elif yn.upper() == "N":
                return "The word doesn't exist. Please double check it."
            else:
                return "Invalid input. Please enter Y or N."
        else:
            return "The word doesn't exist. Please double check it."


def main():
    data_file = "data.json"
    dictionary = load_data_from_json(data_file)

    while True:
        word = input("Enter a word (Press ENTER to exit): ")
        if not word:
            print("Exiting...")
            break
        output = translate(word, dictionary)
        if isinstance(output, list):
            for item in output:
                print(item)
        else:
            print(output)


if __name__ == "__main__":
    main()
