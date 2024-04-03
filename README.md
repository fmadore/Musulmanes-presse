## Analyse préliminaire

Ce code vous aidera à charger votre fichier CSV, à le préparer pour l'analyse en renommant les colonnes pour plus de commodité, et à effectuer une analyse préliminaire. Vous pourrez ainsi obtenir une idée de la répartition des articles par journal et par année, ce qui est essentiel pour comprendre le corpus avant de plonger dans des analyses de texte plus détaillées.

## Prétraitement

Ce script commence par définir une fonction get_wordnet_pos qui convertit les tags de partie du discours (POS tags) utilisés par NLTK en tags compatibles avec le WordNetLemmatizer. Ensuite, il définit une fonction preprocess_texts qui effectue la tokenisation, la suppression des stopwords, et la lemmatisation sur un texte donné. Enfin, cette fonction de prétraitement est appliquée à chaque article dans le DataFrame df, et les résultats sont stockés dans une nouvelle colonne Processed_Content. Cette étape de prétraitement prépare vos données pour des analyses plus complexes et aide à réduire le bruit dans vos données, améliorant ainsi la qualité de vos résultats analytiques.

## Nuage de mots

Ce script vous permettra de visualiser les termes les plus fréquents dans votre corpus après prétraitement.
