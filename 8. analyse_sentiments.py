import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le fichier CSV depuis GitHub, en incluant une colonne pour les pays
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url, usecols=['Processed_Content', 'Pays'])  # Assurez-vous que 'Pays' est le nom correct de la colonne

# Analyse des sentiments
def analyse_sentiment(text):
    try:
        analysis = TextBlob(text)
        return pd.Series([analysis.sentiment.polarity, analysis.sentiment.subjectivity])
    except:
        return pd.Series([None, None])

df[['Polarity', 'Subjectivity']] = df['Processed_Content'].apply(analyse_sentiment)

sns.set(style="whitegrid")

# Fonction pour tracer les graphiques par pays
def plot_sentiment_by_country(country):
    df_country = df[df['Pays'] == country]
    # Histogramme des scores de polarité
    plt.figure(figsize=(10, 6))
    sns.histplot(df_country['Polarity'], bins=30, kde=False, color='skyblue')
    plt.title(f'Distribution des scores de polarité - {country}')
    plt.xlabel('Polarité')
    plt.ylabel('Nombre de textes')
    plt.savefig(f'distribution_polarité_{country}.png')
    plt.show()

    # Nuage de points de polarité vs subjectivité
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Polarity', y='Subjectivity', data=df_country, alpha=0.5, edgecolor=None, color='red')
    plt.title(f'Polarité vs Subjectivité - {country}')
    plt.xlabel('Polarité')
    plt.ylabel('Subjectivité')
    plt.savefig(f'polarité_vs_subjectivité_{country}.png')
    plt.show()

# Générer les visualisations pour chaque pays
for country in df['Pays'].unique():
    plot_sentiment_by_country(country)
