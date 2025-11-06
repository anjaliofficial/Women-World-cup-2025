import pandas as pd
import os


RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

def load_raw_data(filename):
    """Loads raw CSV file."""
    path = os.path.join(RAW_DATA_PATH, filename)
    return pd.read_csv(path)



def load_processed_data(filename):
    """Loads cleaned CSV file."""
    path = os.path.join(RAW_DATA_PATH, filename)
    return pd.read_csv(path)



def save_processed_data(df, filename):
    path = os.path.join(PROCESSED_DATA_PATH, filename)
    df.to_csv(path, index=False)
    print(f"✅ Saved processed file at: {path}")