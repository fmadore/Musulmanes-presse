## Analyse préliminaire

Analyse préliminaire sur le corpus pour obtenir une idée de la répartition des articles par journal et par année.

## Prétraitement

SpaCy est utilisé ici pour traiter chaque article, en retirant les stopwords et la ponctuation, et en appliquant la lemmatisation. Le modèle moyen (fr_core_news_md) est choisi pour une meilleure précision. SpaCy crée une liste de lemmes pour chaque token qui n'est ni un stopword ni un signe de ponctuation, puis joint ces lemmes en une chaîne de caractères unique. Les résultats sont sauvegardé dans un nouveau fichier CSV.

## Nuage de mots

Script permettant de visualiser les termes les plus fréquents dans le corpus après prétraitement.

## Fréquence de termes

Analyse de fréquence Term-Frequency (TF) sur le corpus. Ce processus donne une vue quantitative précise des termes qui apparaissent le plus souvent dans le corpus, offrant des insights sur les sujets et thèmes dominants dans vos données.

## Matrice de co-occurrence

Création d'une matrice de co-occurrence pour le corpus. Permet d'explorer les relations et les contextes dans lesquels les mots apparaissent ensemble. Cette approche peut révéler des associations entre les mots qui ne sont pas immédiatement évidentes. La matrice de co-occurrence compte combien de fois chaque paire de mots apparaît ensemble dans un contexte donné, souvent dans la même phrase ou dans un fenêtre de mots fixe.
