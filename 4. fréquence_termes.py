import pandas as pd
from collections import Counter
import plotly.express as px

# Charger le fichier CSV prétraité depuis GitHub
url = 'https://raw.githubusercontent.com/fmadore/Musulmanes-presse/master/preprocessed_corpus.csv'
df = pd.read_csv(url)

# Liste des mots à exclure
exclusion_list = ['être', 'Burkina', 'il', '-t', 'Bénin']


def analyze_word_frequency_plotly(text, title_suffix, save_filename):
    word_counts = Counter(text.split())
    for word in exclusion_list:
        word_counts.pop(word, None)  # Utiliser pop pour éviter KeyError si le mot n'existe pas

    word_freq_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency',
                                                                                                ascending=False)

    # Créer le graphique avec Plotly
    fig = px.bar(word_freq_df.head(25), x='Frequency', y='Word', orientation='h',
                 title=f'25 mots les plus fréquents - {title_suffix}',
                 labels={'Word': 'Mot', 'Frequency': 'Fréquence'},
                 color='Frequency', color_continuous_scale='Viridis')
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    fig.write_html(f'{save_filename}.html')


# Analyse pour l'ensemble du corpus
all_text = ' '.join(df['Processed_Content'].dropna())
analyze_word_frequency_plotly(all_text, "corpus entier", "top_25_mots_frequents_total")

# Analyse par pays
for country in df['Pays'].unique():
    country_text = ' '.join(df[df['Pays'] == country]['Processed_Content'].dropna())
    if country_text:  # Vérifier si le texte n'est pas vide
        analyze_word_frequency_plotly(country_text, f"Pays : {country}", f"top_25_mots_{country}")
