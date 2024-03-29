"""All read write activities on files can be done using this module"""
import pandas as pd


def get_csv_as_list(file_path):
    df = pd.read_csv(filepath_or_buffer=file_path, delimiter=";")
    return df.values.tolist()


def get_excel_as_list(file_path, sheetname):
    df = pd.read_excel(io=file_path, sheet_name=sheetname)
    return df.values.tolist()


"""method to get value from json file"""


def get_value_from_json(filepath, key):
    dic = pd.read_json(path_or_buf=filepath, typ="dictionary")
    return dic[key]
