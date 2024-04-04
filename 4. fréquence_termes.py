import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Charger le fichier CSV prétraité depuis GitHub
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Liste des mots à exclure
exclusion_list = ['être', 'Burkina']


# Fonction pour analyser la fréquence des mots et générer un graphique
def analyze_word_frequency(text, title_suffix, save_filename):
    word_counts = Counter(text.split())
    # Enlever les mots de la liste d'exclusion du compteur
    for word in exclusion_list:
        if word in word_counts:
            del word_counts[word]
    # Convertir le compteur en DataFrame
    word_freq_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency',
                                                                                                ascending=False).reset_index(
        drop=True)

    # Visualiser les 25 mots les plus fréquents
    plt.figure(figsize=(10, 8))
    plt.barh(word_freq_df['Word'].head(25), word_freq_df['Frequency'].head(25))
    plt.gca().invert_yaxis()  # Inverser l'axe y pour afficher le mot le plus fréquent en haut
    plt.xlabel('Fréquence')
    plt.ylabel('Mot')
    plt.title(f'25 mots les plus fréquents - {title_suffix}')
    plt.savefig(f'{save_filename}.png')
    plt.close()  # Fermer le graphique pour éviter l'affichage en mode batch


# Analyser la fréquence des mots pour l'ensemble du corpus
all_text = ' '.join(df['Processed_Content'].dropna())
analyze_word_frequency(all_text, "Corpus Entier", "top_25_mots_fréquents_total")

# Analyser la fréquence des mots par pays
for country in df['Pays'].unique():
    country_text = ' '.join(df[df['Pays'] == country]['Processed_Content'].dropna())
    if country_text:  # Vérifier si le texte n'est pas vide
        analyze_word_frequency(country_text, country, f"top_25_mots_{country}")

print("Les graphiques ont été générés et sauvegardés.")
