import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Charger le fichier CSV prétraité depuis GitHub
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Convertir tout le texte en minuscules pour assurer la cohérence
df['Processed_Content'] = df['Processed_Content'].str.lower()

# Combiner tous les textes prétraités en une seule chaîne de caractères
all_text = ' '.join(df['Processed_Content'].dropna())

# Définir une liste de mots à exclure (stopwords) en plus des stopwords par défaut
additional_stopwords = {"el", "être", "t", "mme"}  # Ajouter ici les mots à exclure
stopwords = set(STOPWORDS).union(additional_stopwords)

# Créer un objet WordCloud en excluant les stopwords définis
wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=stopwords, min_font_size=10).generate(all_text)

# Afficher le nuage de mots
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

# Sauvegarder le nuage de mots en format PNG
plt.savefig('wordcloud.png')

print("Le nuage de mots a été généré et sauvegardé en tant que 'wordcloud_with_exclusions.png'.")
