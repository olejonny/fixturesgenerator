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


def csv_to_json(csv_file, model_name):
    # Read the csv file
    csv_file_path = f"raw/{csv_file}.csv"
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

    json_file_path = f"fixtures/{csv_file}.json"
    # Write the list to a json file
    with open(json_file_path, "w") as json_file:
        json.dump(records, json_file, indent=4)


if __name__ == "__main__":
    my_files = {
        "headloss.KValue": "component_k_value",
        "headloss.PipeDimension": "pipe_dimension",
        "headloss.PipeMaterial": "pipe_material",
        "water.Dscw_1_9": "dscw_1_9",
        "water.Dscw_1_10": "dscw_1_10",
        "water.Dscw_1_11": "dscw_1_11",
        "water.Dscw_1_12": "dscw_1_12",
        "water.Dscw_1_13": "dscw_1_13",
    }

    for key, value in my_files.items():
        csv_to_json(value, key)
