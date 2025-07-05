import pandas as pd

# function named extract_csv which returns read csv
def extract_csv(filepath):
    return pd.read_csv(filepath)

# to more understanding just remove this file and directly add pd.read_csv() in main.py