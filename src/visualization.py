import matplotlib.pyplot as plt
import seaborn as sns


def plot_top_run_scorers(df):
    top_players = df.groupby('player')['runs'].sum().sort_values(ascending=False).head(10)
    top_players.plot(kind='bar')
    plt.title('Top 10 run Scorers')
    plt.show()