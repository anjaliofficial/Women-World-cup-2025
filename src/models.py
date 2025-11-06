from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib 


def train_match_winner_model(df):
    x = df[['team1_rank', 'team2_rank', 'venue_rating']]
    y = df['winner']
    x_train, x_test, x=y_train, y_test, = train_test_split(x, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    joblib.dump(model, 'models/final_model.pkl')
    return model
