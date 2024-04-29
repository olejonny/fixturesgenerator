import pandas as pd
import json


def excel_to_json(excel_file_path, model_name, json_file_path):
    # Read the excel file
    df = pd.read_excel(excel_file_path)

    # Initialize an empty list to store the records
    records = []

    # Iterate over the DataFrame rows
    for index, row in df.iterrows():
        # Create a dictionary for each row
        record = {
            "model": model_name,
            "pk": index + 1,  # pk starts at 1
            "fields": row.to_dict(),
        }
        # Append the dictionary to the list
        records.append(record)

    # Write the list to a json file
    with open(json_file_path, "w") as json_file:
        json.dump(records, json_file, indent=4)


def csv_to_json(csv_file_path, model_name, json_file_path):
    # Read the csv file
    df = pd.read_csv(csv_file_path)

    # Initialize an empty list to store the records
    records = []

    # Iterate over the DataFrame rows
    for index, row in df.iterrows():
        # Create a dictionary for each row
        record = {
            "model": model_name,
            "pk": index + 1,  # pk starts at 1
            "fields": row.to_dict(),
        }
        # Append the dictionary to the list
        records.append(record)

    # Write the list to a json file
    with open(json_file_path, "w") as json_file:
        json.dump(records, json_file, indent=4)


if __name__ == "__main__":
    my_file = "raw/component_k_value.csv"
    output_file = "component_k_value.json"
    model_name = "headloss.KValue"

    csv_to_json(my_file, model_name, output_file)
