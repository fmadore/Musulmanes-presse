import pandas as pd
from collections import defaultdict
import re
import matplotlib.pyplot as plt
import networkx as nx

# Charger les données
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Définir la liste des mots à exclure
exclusion_list = ['El', 'aujourd', 'hui', 'à', 'il', 't', 'el', 'non', 'Faso', 'Burkina', 'mme']

# Fonction pour nettoyer et convertir les données en listes Python
def clean_and_convert_to_list(text):
    if isinstance(text, str):
        words = re.findall(r'\b\w+\b', text)
        # Filtrer les mots en utilisant la liste d'exclusion
        words = [word for word in words if word not in exclusion_list]
        return words
    else:
        return text

# Appliquer la fonction de nettoyage à la colonne 'Processed_Content'
df['Processed_Content'] = df['Processed_Content'].dropna().apply(clean_and_convert_to_list)

# Créer un dictionnaire pour compter les co-occurrences
co_occurrence = defaultdict(int)

# Définir la fenêtre pour la co-occurrence
window_size = 5

# Calculer les co-occurrences en excluant les paires de mots identiques
# et en combinant les paires dans les deux sens (homme-femme et femme-homme)
for content in df['Processed_Content']:
    for i in range(len(content)):
        target_word = content[i]
        start = max(0, i - window_size)
        end = min(len(content), i + window_size + 1)
        for j in range(start, end):
            if i != j:
                co_occurred_word = content[j]
                # S'assurer que les mots ne sont pas identiques
                if target_word != co_occurred_word:
                    # Ordonner les mots alphabétiquement pour combiner les paires dans les deux sens
                    ordered_pair = tuple(sorted((target_word, co_occurred_word)))
                    co_occurrence[ordered_pair] += 1

# Transformer le dictionnaire de co-occurrence en DataFrame
co_occurrence_df = pd.DataFrame(list(co_occurrence.items()), columns=['Word Pair', 'Co-occurrence'])
co_occurrence_df['Word1'] = co_occurrence_df['Word Pair'].apply(lambda x: x[0])
co_occurrence_df['Word2'] = co_occurrence_df['Word Pair'].apply(lambda x: x[1])
co_occurrence_df.drop('Word Pair', axis=1, inplace=True)

# Filtrer pour ne garder que les paires de mots avec une co-occurrence significative
seuil_co_occurrence = 50  # Ajustez ce seuil selon vos besoins
co_occurrence_df_filtré = co_occurrence_df[co_occurrence_df['Co-occurrence'] > seuil_co_occurrence]

# Créer un graphe à partir des paires de mots filtrées
G = nx.Graph()

# Ajouter des arêtes au graphe basées sur le DataFrame filtré
for index, row in co_occurrence_df_filtré.iterrows():
    word1, word2, co_occurrence = row['Word1'], row['Word2'], row['Co-occurrence']
    G.add_edge(word1, word2, weight=co_occurrence)

# Filtrer les nœuds isolés qui peuvent apparaître après l'application de la liste d'exclusion
G.remove_nodes_from(list(nx.isolates(G)))

# Dessiner le graphe
plt.figure(figsize=(12, 12))
pos = nx.kamada_kawai_layout(G)  # Utiliser Kamada-Kawai layout

edges = G.edges(data=True)
weights = [edata['weight'] / 50 for _, _, edata in edges]  # Ajustement pour des arêtes plus fines

nx.draw_networkx_edges(G, pos, width=weights, edge_color='grey')
nx.draw_networkx_labels(G, pos, font_size=12)
plt.title('Graphe de Co-occurrence')
plt.axis('off')
plt.savefig('graphe_co-occurrence.png', format='png', dpi=300, bbox_inches='tight')
plt.show()

