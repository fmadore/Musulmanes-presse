import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Assurez-vous d'avoir téléchargé les ressources nécessaires de NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


# Fonction pour convertir les tags de nltk en tags compatibles avec wordnet lemmatizer
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


# Initialiser le lemmatizer
lemmatizer = WordNetLemmatizer()


# Prétraitement des textes
def preprocess_texts(text):
    # Tokenisation
    tokens = word_tokenize(text.lower())  # Convertir en minuscule et tokeniser

    # Filtrage des stopwords
    tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('french')]

    # Lemmatisation
    lemmatized_tokens = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in tokens]

    return lemmatized_tokens


# Appliquer le prétraitement à chaque article
df['Processed_Content'] = df['Content'].apply(preprocess_texts)

# Afficher les résultats
print(df[['Content', 'Processed_Content']].head())
