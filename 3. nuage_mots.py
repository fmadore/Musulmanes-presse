import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Charger le fichier CSV prétraité
url = 'https://github.com/fmadore/Musulmanes-presse/raw/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Combiner tous les textes prétraités en une seule chaîne
# Assurez-vous que les contenus traités sont bien des chaînes de caractères
all_text = ' '.join(df['Processed_Content'].dropna().astype(str))

# Créer et configurer le wordcloud
wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = None, # Les stopwords ont déjà été filtrés lors du prétraitement
                      min_font_size = 10).generate(all_text)

# Afficher le wordcloud
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

# Sauvegarder le wordcloud en format PNG
plt.savefig('wordcloud.png')

print("Le wordcloud a été généré et sauvegardé en tant que 'wordcloud.png'.")
