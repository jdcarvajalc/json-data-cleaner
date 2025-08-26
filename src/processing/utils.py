import json
import os


def save_json_to_file(data, filename, indent=4):
    """
    Saves JSON data to a file with readable formatting.

    Args:
        data (dict | list): The data object to save.
        filename (str): The name of the output file.
        indent (int): The number of spaces for indentation, by default is 4.
    """
    try:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        print(f"Data successfully saved to '{filename}'")
    except IOError as e:
        print(f"Error saving the file: {e}")
