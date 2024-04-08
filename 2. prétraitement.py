import pandas as pd
import spacy
from tqdm.auto import tqdm
import re

# Initialiser tqdm pour pandas
tqdm.pandas()

# Charger le modèle spaCy français moyen
nlp = spacy.load("fr_core_news_md")

# Charger le DataFrame en incluant la colonne 'url'
url = 'https://github.com/fmadore/Musulmanes-presse/raw/master/Corpus.csv'
df = pd.read_csv(url, usecols=['dcterms:title', 'dcterms:creator', 'dcterms:publisher', 'dcterms:date', 'bibo:content', 'url'])

# Renommer les colonnes
df.rename(columns={
    'dcterms:title': 'Title',
    'dcterms:creator': 'Creator',
    'dcterms:publisher': 'Publisher',
    'dcterms:date': 'Date',
    'bibo:content': 'Content',
    'url': 'URL'
}, inplace=True)

# Dictionnaire des pays aux éditeurs
country_to_publishers = {
    "Burkina Faso": ["Burkina 24", "Carrefour africain", "L’Observateur", "L’Observateur Paalga", "Le Pays", "LeFaso.net", "Mutations", "San Finna", "Sidwaya"],
    "Bénin": ["Boulevard des Infos", "Daho-Express", "Ehuzu", "La Nation"],
}

# Inverser le dictionnaire pour obtenir les éditeurs aux pays
publisher_to_country = {publisher: country for country, publishers in country_to_publishers.items() for publisher in publishers}

# Utiliser le dictionnaire pour ajouter la nouvelle colonne 'Pays'
df['Pays'] = df['Publisher'].map(publisher_to_country)

# Fonction de nettoyage de texte
def clean_text(text):
    text = re.sub(r"’", "'", text)  # Convertir apostrophes courbes en droits
    text = re.sub(r"\s+", " ", text)  # Supprimer les espaces doubles
    text = re.sub(r"œ", "oe", text)  # Uniformiser les "oe"
    text = text.strip()  # Supprimer les espaces de début et de fin
    return text

# Fonction de prétraitement utilisant spaCy
def preprocess_spacy(text):
    # Nettoyer le texte en premier
    cleaned_text = clean_text(text)
    # Traiter le texte nettoyé avec spaCy
    doc = nlp(cleaned_text)
    # Générer une liste de lemmes, en excluant les stopwords et les ponctuations
    lemmatized_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    # Joindre les tokens pour former une string
    return " ".join(lemmatized_tokens)

# Appliquer le prétraitement avec une barre de progression
df['Processed_Content'] = df['Content'].progress_apply(preprocess_spacy)

# Sauvegarder dans un nouveau fichier CSV, s'assurer de l'ordre des colonnes
columns_order = ['Title', 'Creator', 'Publisher', 'Date', 'Content', 'URL', 'Pays', 'Processed_Content']
df = df[columns_order]  # Réordonner les colonnes selon l'ordre souhaité
output_path = 'preprocessed_corpus.csv'
df.to_csv(output_path, index=False)

print(f"Le fichier prétraité a été sauvegardé avec succès à l'emplacement suivant : {output_path}")
