from processing.utils import clean_and_format_json, save_json_to_file


def execute_json_cleaner():
    """
    Main function to read, clean and save JSON data.
    """
    input_file_path = "../../data/raw/malformed_data.json"
    output_file_path = "../../data/processed_json_files/clean_data.json"

    # 1. Read the raw data file
    try:
        with open(input_file_path, "r", encoding="utf-8") as f:
            malformed_data = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return

    # 2. Clean the JSON data
    clean_data = clean_and_format_json(malformed_data)

    if clean_data is None:
        print("The cleaning process failed. Exiting.")
        return

    # 3. Save the clean data to a new file
    save_json_to_file(clean_data, output_file_path)
