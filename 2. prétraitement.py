import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from tqdm import tqdm

tqdm.pandas()

# Téléchargements nécessaires de NLTK, assurez-vous qu'ils sont déjà effectués
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Charger le DataFrame
url = 'https://github.com/fmadore/Musulmanes-presse/raw/master/Corpus.csv'
df = pd.read_csv(url, usecols=['dcterms:title', 'dcterms:creator', 'dcterms:publisher', 'dcterms:date', 'bibo:content'])
df.columns = ['Title', 'Creator', 'Publisher', 'Date', 'Content']

# Fonctions de prétraitement
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

lemmatizer = WordNetLemmatizer()

def preprocess_texts(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('french')]
    lemmatized_tokens = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in tokens]
    return lemmatized_tokens

# Application du prétraitement et sauvegarde du résultat
df['Processed_Content'] = df['Content'].progress_apply(preprocess_texts)

# Sauvegarder dans un nouveau fichier CSV
output_path = 'preprocessed_corpus.csv'
df.to_csv(output_path, index=False)

print(f"Le fichier prétraité a été sauvegardé avec succès à l'emplacement suivant : {output_path}")
