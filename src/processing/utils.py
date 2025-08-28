import json
import os
import re


def clean_and_format_json(malformed_string):
    """
    Cleans and formats a JSON string that follows a specific escape pattern.

    Args:
        malformed_string (str): The raw JSON string with formatting errors.

    Returns:
        list | dict: A valid Python JSON object, or None if an error occurs.
    """
    # Step 1: Remove the known garbage wrapping the JSON content.
    # We use a pattern to isolate the array content and remove the "errors" and "ok" fields.
    json_content_match = re.search(r'"json":"\[(.*)\]",', malformed_string, re.DOTALL)

    if not json_content_match:
        print("Error: Could not find the JSON content wrapped in the 'json' field.")
        return None

    extracted_content = json_content_match.group(1)

    # Step 2: Un-escape quotes and remove the extra comma at the end.
    cleaned_content = extracted_content.replace('\\"', '"')

    # Check for a trailing comma and remove it. This is a common error in such strings.
    if cleaned_content.endswith(',{"'):
        cleaned_content = cleaned_content[:-2]
    elif cleaned_content.endswith("},"):
        cleaned_content = cleaned_content[:-1]

    # Wrap the content back in an array to make it a valid JSON list.
    final_json_string = f"[{cleaned_content}]"

    try:
        # Step 3: Attempt to parse the cleaned string.
        return json.loads(final_json_string)
    except json.JSONDecodeError as e:
        print(f"JSON decoding error in the extracted content: {e}")
        return None


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
