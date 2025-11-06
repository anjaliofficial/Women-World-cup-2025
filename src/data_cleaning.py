import pandas as pd

def clean_match_data(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=['team1', 'team2', 'winner'])
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df
