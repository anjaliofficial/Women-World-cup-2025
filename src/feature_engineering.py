def add_strike_rate(df):
    df['strike_rate'] = (df['runs'] / df['balls_faced'])*100
    return df


