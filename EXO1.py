import csv

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

