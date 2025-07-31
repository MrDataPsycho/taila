import csv

DEFAULT_DATA_PATH = "./data/mini-llama-articles.csv"

def read_mini_llama_csv(file_path):
    rows = []
    # Load the CSV file
    data_path = file_path if file_path else DEFAULT_DATA_PATH
    with open(data_path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)

        for idx, row in enumerate(csv_reader):
            if idx == 0: continue; # Skip header row
            rows.append(row)

        # The number of artickes in the dataset.
        print("number of articles:", len(rows))
        return rows
    

def read_mini_llama_csv_for_notebook():
    file_path_notebook = "../data/mini-llama-articles.csv"
    return read_mini_llama_csv(file_path_notebook)