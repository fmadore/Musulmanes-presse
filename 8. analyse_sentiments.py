import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le fichier CSV depuis GitHub
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url, usecols=['Content'])

# Analyse des sentiments
def analyse_sentiment(text):
    try:
        analysis = TextBlob(text)
        return pd.Series([analysis.sentiment.polarity, analysis.sentiment.subjectivity])
    except:
        return None

df[['Polarity', 'Subjectivity']] = df['Content'].apply(analyse_sentiment)

sns.set(style="whitegrid")

# Histogramme des scores de polarité
plt.figure(figsize=(10, 6))
sns.histplot(df['Polarity'], bins=30, kde=False, color='skyblue')
plt.title('Distribution des scores de polarité')
plt.xlabel('Polarité')
plt.ylabel('Nombre de textes')
plt.savefig('distribution_polarité.png')
plt.show()

# Nuage de points de polarité vs subjectivité
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Polarity', y='Subjectivity', data=df, alpha=0.5, edgecolor=None, color='red')
plt.title('Polarité vs Subjectivité')
plt.xlabel('Polarité')
plt.ylabel('Subjectivité')
plt.savefig('polarité_vs_subjectivité.png')
plt.show()
