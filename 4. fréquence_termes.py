import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Charger le fichier CSV prétraité depuis GitHub
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Combiner tous les textes prétraités en une seule chaîne de caractères
all_text = ' '.join(df['Processed_Content'].dropna())

# Calculer la fréquence de chaque terme dans le corpus
word_counts = Counter(all_text.split())

# Liste des mots à exclure
exclusion_list = ['être']  # Mots à exclure

# Enlever les mots de la liste d'exclusion du compteur
for word in exclusion_list:
    if word in word_counts:
        del word_counts[word]

# Convertir le compteur en DataFrame pour une manipulation plus facile
word_freq_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False).reset_index(drop=True)

# Afficher les 20 mots les plus fréquents
print(word_freq_df.head(25))

# Visualiser les 25 mots les plus fréquents
plt.figure(figsize=(10, 8))
plt.barh(word_freq_df['Word'].head(25), word_freq_df['Frequency'].head(25))
plt.gca().invert_yaxis()  # Inverser l'axe y pour afficher le mot le plus fréquent en haut
plt.xlabel('Fréquence')
plt.ylabel('Mot')
plt.title('25 mots les plus fréquents')

# Enregistrer le graphique en format PNG
plt.savefig('top_25_mots_fréquents.png')

# Afficher le graphique
plt.show()

print("Le graphique a été enregistré.")
