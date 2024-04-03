import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Charger le fichier CSV prétraité depuis GitHub
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Combiner tous les textes prétraités en une seule chaîne de caractères
# En assumant que les données prétraitées sont dans une colonne nommée 'Processed_Content'
all_text = ' '.join(df['Processed_Content'].dropna())

# Créer un objet WordCloud
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(all_text)

# Afficher le nuage de mots
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

# Sauvegarder le nuage de mots en format PNG
plt.savefig('wordcloud.png')

print("Le nuage de mots a été généré et sauvegardé en tant que 'wordcloud.png'.")
