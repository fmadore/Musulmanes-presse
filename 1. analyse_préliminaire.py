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

# Dictionnaire des pays aux éditeurs
country_to_publishers = {
    "Burkina Faso": ["Burkina 24", "Carrefour africain", "L’Observateur", "L’Observateur Paalga", "Le Pays", "LeFaso.net", "Mutations", "San Finna", "Sidwaya"],
    "Bénin": ["Boulevard des Infos", "Daho-Express", "Ehuzu", "La Nation"],
}

# Inverser le dictionnaire pour obtenir les éditeurs aux pays
publisher_to_country = {publisher: country for country, publishers in country_to_publishers.items() for publisher in publishers}

# Utiliser le dictionnaire pour ajouter la nouvelle colonne 'Pays'
df['Pays'] = df['Publisher'].map(publisher_to_country)

# Visualisation 1: Distribution des articles par année
plt.figure(figsize=(10, 6))
df['Date'].dt.year.value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Nombre d\'articles par année')
plt.xlabel('Année')
plt.ylabel('Nombre d\'articles')
plt.xticks(rotation=45)
plt.tight_layout() # Ajuste automatiquement les paramètres de la figure pour qu'elle s'adapte
plt.savefig('articles_par_annee.png')
plt.show()

# Visualisation 2: Répartition des articles par journal
plt.figure(figsize=(12, 8))
publisher_counts = df['Publisher'].value_counts().reset_index()
publisher_counts.columns = ['Publisher', 'Counts']
sns.barplot(x='Counts', y='Publisher', data=publisher_counts, palette='viridis', order=publisher_counts['Publisher'], hue='Publisher', legend=False)
plt.title('Nombre d\'articles par journal')
plt.xlabel('Nombre d\'articles')
plt.ylabel('Journal')
plt.legend().remove()  # Retirer la légende générée par l'utilisation de hue
plt.tight_layout(rect=[0, 0, 1, 1])
plt.savefig('articles_par_journal.png')
plt.show()

# Visualisation 3: Distribution des articles par pays
plt.figure(figsize=(12, 8))
country_counts = df['Pays'].value_counts().reset_index()
country_counts.columns = ['Pays', 'Nombre d\'articles']
sns.barplot(x='Nombre d\'articles', y='Pays', data=country_counts, palette='coolwarm', order=country_counts['Pays'], hue='Pays', legend=False)
plt.title('Nombre d\'articles par pays')
plt.xlabel('Nombre d\'articles')
plt.ylabel('Pays')
plt.legend().remove()  # Retirer la légende générée par l'utilisation de hue
plt.tight_layout(rect=[0, 0, 1, 1])
plt.savefig('articles_par_pays.png')
plt.show()
