import pandas as pd
import numpy as np
from collections import defaultdict
from itertools import combinations
import matplotlib.pyplot as plt

# Charger les données
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Prétraitement pour s'assurer que les données sont correctes
df['Processed_Content'] = df['Processed_Content'].dropna().apply(eval)

# Créer un dictionnaire pour compter les co-occurrences
co_occurrence = defaultdict(int)

# Définir la fenêtre pour la co-occurrence
window_size = 5

for content in df['Processed_Content']:
    for i in range(len(content)):
        # Obtenir le mot cible
        target_word = content[i]
        # Déterminer la fenêtre de co-occurrence dans le contexte
        start = max(0, i - window_size)
        end = min(len(content), i + window_size + 1)
        # Parcourir les mots dans la fenêtre
        for j in range(start, end):
            if i != j:  # S'assurer que nous ne comptons pas le mot avec lui-même
                co_occurred_word = content[j]
                co_occurrence[(target_word, co_occurred_word)] += 1

# Transformer le dictionnaire de co-occurrence en DataFrame pour une meilleure manipulation
co_occurrence_df = pd.DataFrame(list(co_occurrence.items()), columns=['Word Pair', 'Co-occurrence'])
co_occurrence_df['Word1'] = co_occurrence_df['Word Pair'].apply(lambda x: x[0])
co_occurrence_df['Word2'] = co_occurrence_df['Word Pair'].apply(lambda x: x[1])
co_occurrence_df.drop('Word Pair', axis=1, inplace=True)

# Afficher les paires de mots avec les plus hautes co-occurrences
print(co_occurrence_df.sort_values(by='Co-occurrence', ascending=False).head(20))

# Optionnel : Sauvegarder la matrice de co-occurrence pour une analyse plus poussée
co_occurrence_df.to_csv('co_occurrence_matrix.csv', index=False)
