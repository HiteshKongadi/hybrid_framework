import pandas as pd


def get_csv_as_list(file_path):
    df = pd.read_csv(filepath_or_buffer=file_path, delimiter=";")
    return df.values.tolist()
