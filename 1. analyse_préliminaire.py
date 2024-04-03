import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration pour améliorer la présentation des graphiques
sns.set(style="whitegrid")

# Télécharger le fichier CSV depuis GitHub
url = 'https://github.com/fmadore/Musulmanes-presse/raw/master/Corpus.csv'
df = pd.read_csv(url, usecols=['dcterms:title', 'dcterms:creator', 'dcterms:publisher', 'dcterms:date', 'bibo:content'])

# Renommer les colonnes pour simplifier
df.columns = ['Title', 'Creator', 'Publisher', 'Date', 'Content']

# Convertir la colonne 'Date' au format datetime de pandas
df['Date'] = pd.to_datetime(df['Date'])

# Visualisation 1: Distribution des articles par année
plt.figure(figsize=(10, 6))
df['Date'].dt.year.value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Nombre d\'articles par année')
plt.xlabel('Année')
plt.ylabel('Nombre d\'articles')
plt.xticks(rotation=45)
plt.tight_layout() # Ajuste automatiquement les paramètres de la figure pour qu'elle s'adapte
plt.savefig('articles_par_annee.png') # Enregistrer la figure
plt.show()

# Visualisation 2: Répartition des articles par journal
plt.figure(figsize=(12, 8)) # Ajustez la taille de la figure si nécessaire pour mieux adapter les noms des journaux
sns.countplot(y='Publisher', data=df, order=df['Publisher'].value_counts().index, palette='viridis')
plt.title('Nombre d\'articles par journal')
plt.xlabel('Nombre d\'articles')
plt.ylabel('Journal')
plt.tight_layout(rect=[0.15, 0, 1, 1]) # Ajustez cette ligne pour augmenter l'espace à gauche
plt.savefig('articles_par_journal.png') # Enregistrer la figure
plt.show()
