import pandas as pd
import numpy as np
from collections import defaultdict
import re
import matplotlib.pyplot as plt

# Charger les données
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Fonction pour nettoyer et convertir les données en listes Python
def clean_and_convert_to_list(text):
    if isinstance(text, str):
        words = re.findall(r'\b\w+\b', text)
        return words
    else:
        return text

# Appliquer la fonction de nettoyage à la colonne 'Processed_Content'
df['Processed_Content'] = df['Processed_Content'].dropna().apply(clean_and_convert_to_list)

# Définir la liste des mots à exclure
exclusion_list = ['il', 't', "aujourd", "hui", "Burkina", "El"]

# Créer un dictionnaire pour compter les co-occurrences
co_occurrence = defaultdict(int)

# Définir la fenêtre pour la co-occurrence
window_size = 5

# Calculer les co-occurrences
for content in df['Processed_Content']:
    for i in range(len(content)):
        target_word = content[i]
        if target_word in exclusion_list:  # Ignorer le mot s'il est dans la liste d'exclusion
            continue
        start = max(0, i - window_size)
        end = min(len(content), i + window_size + 1)
        for j in range(start, end):
            if i != j:
                co_occurred_word = content[j]
                if co_occurred_word in exclusion_list:  # Ignorer le mot co-occurrent s'il est dans la liste d'exclusion
                    continue
                if target_word != co_occurred_word:
                    ordered_pair = tuple(sorted((target_word, co_occurred_word)))
                    co_occurrence[ordered_pair] += 1

# Transformer le dictionnaire de co-occurrence en DataFrame
co_occurrence_df = pd.DataFrame(list(co_occurrence.items()), columns=['Word Pair', 'Co-occurrence'])
co_occurrence_df['Word1'] = co_occurrence_df['Word Pair'].apply(lambda x: x[0])
co_occurrence_df['Word2'] = co_occurrence_df['Word Pair'].apply(lambda x: x[1])
co_occurrence_df.drop('Word Pair', axis=1, inplace=True)

# Trier les paires de mots par co-occurrence
top_co_occurrences = co_occurrence_df.sort_values(by='Co-occurrence', ascending=False).head(25)

# Créer un graphique à barres pour les co-occurrences
plt.figure(figsize=(10, 8))
plt.barh(top_co_occurrences['Word1'] + '-' + top_co_occurrences['Word2'], top_co_occurrences['Co-occurrence'])
plt.xlabel('Co-occurrence')
plt.ylabel('Paires de mots')
plt.title('25 paires de mots les plus fréquentes')

# Ajuster l'espace autour du graphique pour s'assurer que la légende est complètement affichée
plt.subplots_adjust(left=0.3)  # Ajustez cette valeur selon vos besoins

# Sauvegarder le graphique
plt.savefig('top_25_co_occurrences.png', format='png')

plt.show()
