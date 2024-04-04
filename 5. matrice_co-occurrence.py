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
        words = re.findall(r'\b\w+\b', text.lower())  # Convertir en minuscules pour uniformiser
        return [word for word in words if word not in exclusion_list]  # Exclure lors de la nettoyage
    else:
        return []

# Définir la liste des mots à exclure
exclusion_list = ['il', 't', "aujourd", "hui", "Burkina", "El", "el", "burkina", "faso", "bénin"]

# Calculer les co-occurrences
def calculate_co_occurrences(content_list, window_size=5):
    co_occurrence = defaultdict(int)
    for content in content_list:
        for i in range(len(content)):
            target_word = content[i]
            start = max(0, i - window_size)
            end = min(len(content), i + window_size + 1)
            for j in range(start, end):
                if i != j:
                    co_occurred_word = content[j]
                    # Ignorer si le mot cible est identique au mot co-occurrent
                    if target_word == co_occurred_word:
                        continue
                    ordered_pair = tuple(sorted((target_word, co_occurred_word)))
                    co_occurrence[ordered_pair] += 1
    return co_occurrence


# Fonction pour générer et sauvegarder le graphique de co-occurrences
def generate_co_occurrence_chart(co_occurrence, title, filename):
    co_occurrence_df = pd.DataFrame(list(co_occurrence.items()), columns=['Word Pair', 'Co-occurrence'])
    co_occurrence_df['Word1'] = co_occurrence_df['Word Pair'].apply(lambda x: x[0])
    co_occurrence_df['Word2'] = co_occurrence_df['Word Pair'].apply(lambda x: x[1])
    co_occurrence_df.drop('Word Pair', axis=1, inplace=True)
    top_co_occurrences = co_occurrence_df.sort_values(by='Co-occurrence', ascending=False).head(25)

    plt.figure(figsize=(10, 8))
    # Afficher les paires les plus fréquentes en haut du graphique
    plt.barh(top_co_occurrences['Word1'] + '-' + top_co_occurrences['Word2'], top_co_occurrences['Co-occurrence'])
    plt.xlabel('Co-occurrence')
    plt.ylabel('Paires de mots')
    plt.title(title)
    plt.subplots_adjust(left=0.3)  # Ajuster selon le besoin

    # Inverser l'axe y pour que les paires les plus fréquentes apparaissent en haut
    plt.gca().invert_yaxis()

    plt.savefig(f'{filename}.png', format='png')
    plt.close()

# Pré-traitement du contenu
df['Processed_Content'] = df['Processed_Content'].apply(clean_and_convert_to_list)

# Co-occurrences pour l'ensemble du corpus
all_content_list = df['Processed_Content'].tolist()
all_co_occurrences = calculate_co_occurrences(all_content_list)
generate_co_occurrence_chart(all_co_occurrences, '25 paires de mots les plus fréquentes - corpus entier', 'top_25_co_occurrences_total')

# Co-occurrences par pays
for country in df['Pays'].unique():
    country_content_list = df[df['Pays'] == country]['Processed_Content'].tolist()
    if country_content_list:  # Vérifier si la liste n'est pas vide
        country_co_occurrences = calculate_co_occurrences(country_content_list)
        generate_co_occurrence_chart(country_co_occurrences, f'25 paires de mots les plus fréquentes - {country}', f'top_25_co_occurrences_{country}')

print("Les graphiques ont été générés et sauvegardés.")
