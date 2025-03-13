import csv
import matplotlib.pyplot as plt

# Lecture du fichier CSV
def lire_csv(Magass):
    """
    Lit un fichier CSV et retourne une liste de dictionnaires.
    """
    donnees = []
    with open(Magass, mode='r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier, delimiter=',')
        for lec in lecteur:
            # Conversion des nombres en entiers
            lec['Cas'] = int(lec['Cas'])
            lec['Dèces'] = int(lec['Dèces'])
            donnees.append(lec)
    return donnees

# Calculs statistiques
def calculer_statistiques(donnees):
    """
    Calcule les totaux et taux de mortalité par préfecture.
    Retourne un dictionnaire {préfecture: {cas, deces, taux}}.
    """
    stats = {}
    for entree in donnees:
        prefect = entree['Préfecture']
        if prefect not in stats:
            stats[prefect] = {'cas': 0, 'deces': 0}
        stats[prefect]['cas'] += entree['Cas']
        stats[prefect]['deces'] += entree['Dèces']
    
    # Calcul du taux de mortalité
    for prefect in stats:
        cas = stats[prefect]['cas']
        deces = stats[prefect]['deces']
        stats[prefect]['taux'] = deces / cas if cas > 0 else 0.0
    return stats

# Visualisation
def visualiser_donnees(stats):
    """
    Génère deux diagrammes à barres : cas totaux et taux de mortalité.
    """
    prefectures = list(stats.keys())
    cas = [stats[prefect]['cas'] for prefect in prefectures]
    taux = [stats[prefect]['taux'] for prefect in prefectures]

    # Diagramme des cas
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, cas, color='blue')
    plt.title('Nombre total de cas par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Cas')

    # Diagramme du taux de mortalité
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, taux, color='yellow')
    plt.title('Taux de mortalité par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Taux (Décès/Cas)')
    plt.ylim(0, 1)  # Une meilleure lisibilité

    plt.show()

# Exécution principale
if __name__ == "__main__":
    donnees = lire_csv('ebola_guinea.csv')
    stats = calculer_statistiques(donnees)
    visualiser_donnees(stats)
