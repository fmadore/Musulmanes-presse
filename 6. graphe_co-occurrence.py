import pandas as pd
from collections import defaultdict
import re
from pyvis.network import Network
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

for content in df['Processed_Content']:
    for i in range(len(content)):
        target_word = content[i]
        start = max(0, i - window_size)
        end = min(len(content), i + window_size + 1)
        for j in range(start, end):
            if i != j:
                co_occurred_word = content[j]
                if target_word != co_occurred_word:
                    ordered_pair = tuple(sorted((target_word, co_occurred_word)))
                    co_occurrence[ordered_pair] += 1

# Créer un graphe NetworkX à partir des données de co-occurrence
G = nx.Graph()

# Ajouter des arêtes basées sur le dictionnaire de co-occurrence
for (word1, word2), weight in co_occurrence.items():
    if weight > 50:  # Filtrer par un seuil de co-occurrence si nécessaire
        G.add_edge(word1, word2, weight=weight)

# Initialiser PyVis Network
nt = Network('800px', '100%', notebook=True)
nt.force_atlas_2based(gravity=-50, central_gravity=0.01, spring_length=100, spring_strength=0.02, damping=0.4, overlap=0)

# Ajouter les nœuds et les arêtes du graphe NetworkX au graphe PyVis
for node in G.nodes:
    nt.add_node(node, title=node)

max_weight = max([edata['weight'] for _, _, edata in G.edges(data=True)])
min_width, max_width = 0.5, 5.0  # Définissez ces valeurs selon vos préférences

for source, target, edata in G.edges(data=True):
    weight = edata['weight']
    width = min_width + (max_width - min_width) * (weight / max_weight)  # Normaliser la largeur
    nt.add_edge(source, target, width=width)

# Activer la physique pour un placement initial optimisé des nœuds
nt.toggle_physics(True)

# Générer et ouvrir la visualisation interactive
nt.show('co_occurrence_graph.html')
