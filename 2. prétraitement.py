import pandas as pd
import spacy
from tqdm.auto import tqdm

# Initialiser tqdm pour pandas
tqdm.pandas()

# Charger le modèle spaCy français moyen
nlp = spacy.load("fr_core_news_md")

# Charger le DataFrame
url = 'https://github.com/fmadore/Musulmanes-presse/raw/master/Corpus.csv'
df = pd.read_csv(url, usecols=['dcterms:title', 'dcterms:creator', 'dcterms:publisher', 'dcterms:date', 'bibo:content'])
df.columns = ['Title', 'Creator', 'Publisher', 'Date', 'Content']

# Fonction de prétraitement utilisant spaCy
def preprocess_spacy(text):
    # Traiter le texte avec spaCy
    doc = nlp(text)
    # Générer une liste de lemmes, en excluant les stopwords et les ponctuations
    lemmatized_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    # Joindre les tokens pour former une string
    return " ".join(lemmatized_tokens)

# Appliquer le prétraitement avec une barre de progression
df['Processed_Content'] = df['Content'].progress_apply(preprocess_spacy)

# Sauvegarder dans un nouveau fichier CSV
output_path = 'preprocessed_corpus.csv'
df.to_csv(output_path, index=False)

print(f"Le fichier prétraité a été sauvegardé avec succès à l'emplacement suivant : {output_path}")
