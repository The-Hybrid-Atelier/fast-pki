#Script to clean sponge data from question pro survey

import pandas as pd

def open_data(file_path):
    # Read data
    df = pd.read_csv(file_path)

    return df


def remove_empty_columns(df):
    # Remove columns with all NaN values
    df = df.dropna(axis=1, how='all')

    return df

def remove_incomplete_surveys(df):
    # Remove rows where column "Response Status" is not "Complete"
    df = df[df["Response Status"] == "Completed"]

    return df

def save_to_bin(df, file_path):
    # Save data to binary file
    df.to_pickle(file_path)

    return None

if __name__ == "__main__":
    # Path to data
    file_path = "raw_sponge_data.csv"

    # Load data
    df = open_data(file_path)

    # Clean data
    df = remove_empty_columns(df)
    df = remove_incomplete_surveys(df)

    # Save data
    save_to_bin(df, "clean_sponge_data.pkl")

    print(df.head())
