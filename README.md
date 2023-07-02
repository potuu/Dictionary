# Dictionary
This Python program is a simple dictionary application. It prompts the user to enter a word and retrieves its translation from a dictionary file, then prints it on the screen.

# Interactive Dictionary

This is a simple interactive dictionary program written in Python. It allows users to enter a word and get its definitions from a pre-defined dictionary. If the entered word is not found in the dictionary, the program suggests similar words and prompts the user for confirmation.

## Features

- Load dictionary data from a JSON file.
- Perform case-insensitive word lookup.
- Handle incorrect word entries by suggesting similar words.
- Ask for user confirmation on suggested words.
- Display multiple definitions for a word if available.
- Allow users to exit the program by pressing ENTER.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository or download the source code files.
3. Prepare a JSON file containing the dictionary data. The file should follow the format `{"word": ["definition1", "definition2", ...]}`.
4. Replace the `data_file` variable in the code with the path to your JSON file.
5. Open a terminal or command prompt and navigate to the project directory.
6. Run the following command to execute the program:
    ```
    python dictionary.py
    ```
7. Enter a word when prompted. The program will display the definitions if the word is found in the dictionary.
8. If the entered word is not found, the program will suggest similar words. Confirm or reject the suggestion by entering "Y" or "N" accordingly.
9. To exit the program, simply press ENTER when prompted for a word.

## Dependencies

This program requires the following dependencies:

- Python 3.x
- The `json` module (included in Python standard library)
- The `difflib` module (included in Python standard library)

## File Structure

The file structure of the project is as follows:

