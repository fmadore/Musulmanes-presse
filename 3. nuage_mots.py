import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Charger le fichier CSV prétraité depuis GitHub
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Convertir tout le texte en minuscules pour assurer la cohérence
df['Processed_Content'] = df['Processed_Content'].str.lower()

# Définir une liste de mots à exclure (stopwords) en plus des stopwords par défaut
additional_stopwords = {"el", "être", "t", "mme", "m"}  # Ajouter ici les mots à exclure
stopwords = set(STOPWORDS).union(additional_stopwords)

# Fonction pour générer un nuage de mots
def generate_wordcloud(text, filename):
    wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=stopwords, min_font_size=10, collocations=False).generate(text)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(f'{filename}.png')
    plt.close()  # Fermer la figure après l'enregistrement pour éviter l'affichage superflu

# Générer un nuage de mots pour l'ensemble du corpus
all_text = ' '.join(df['Processed_Content'].dropna())
generate_wordcloud(all_text, 'wordcloud_total')

# Générer un nuage de mots par pays
for country in df['Pays'].unique():
    country_text = ' '.join(df[df['Pays'] == country]['Processed_Content'].dropna())
    if country_text:  # Vérifier si le texte n'est pas vide
        generate_wordcloud(country_text, f'wordcloud_{country}')

print("Les nuages de mots ont été générés et sauvegardés.")
