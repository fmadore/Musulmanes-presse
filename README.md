## Analyse préliminaire

Ce code vous aidera à charger votre fichier CSV, à le préparer pour l'analyse en renommant les colonnes pour plus de commodité, et à effectuer une analyse préliminaire. Vous pourrez ainsi obtenir une idée de la répartition des articles par journal et par année, ce qui est essentiel pour comprendre le corpus avant de plonger dans des analyses de texte plus détaillées.

## Prétraitement

SpaCy est utilisé ici pour traiter chaque article, en retirant les stopwords et la ponctuation, et en appliquant la lemmatisation. Le modèle moyen (fr_core_news_md) est choisi pour une meilleure précision par rapport au modèle petit sans être trop lourd comme le modèle grand.
Tqdm est utilisé pour fournir une barre de progression visuelle durant l'application du prétraitement. Notez l'utilisation de tqdm.pandas() pour l'intégrer avec les opérations pandas.
La fonction preprocess_spacy remplace preprocess_texts pour le prétraitement des textes avec spaCy. Elle crée une liste de lemmes pour chaque token qui n'est ni un stopword ni un signe de ponctuation, puis joint ces lemmes en une chaîne de caractères unique.
Ce script effectue le prétraitement en utilisant spaCy et sauvegarde les résultats dans un nouveau fichier CSV. Cela devrait améliorer la qualité du prétraitement grâce à l'usage d'un modèle linguistique plus avancé et spécifique au français.

## Nuage de mots

Ce script vous permettra de visualiser les termes les plus fréquents dans votre corpus après prétraitement.

## Fréquence de termes

Analyse de fréquence Term-Frequency (TF) sur le corpus. Ce processus  donne une vue quantitative précise des termes qui apparaissent le plus souvent dans le corpus, offrant des insights sur les sujets et thèmes dominants dans vos données.

## Matrice de co-occurrence

Créer une matrice de co-occurrence pour un corpus de texte est une façon d'explorer les relations et les contextes dans lesquels les mots apparaissent ensemble. Cette approche peut révéler des associations entre les mots qui ne sont pas immédiatement évidentes. La matrice de co-occurrence compte combien de fois chaque paire de mots apparaît ensemble dans un contexte donné, souvent dans la même phrase ou dans un fenêtre de mots fixe.
