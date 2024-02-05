import sys
import pandas as pd
import random
import matplotlib.pyplot as plt

#Initialisation de toutes les variables qui vont servir
output_data=[]
current_commande = None
current_quantite = 0
current_timbre = 0
current_ville = None
current_nb = 0
current_moyenne = 0

# Lecture de chaque ligne depuis STDIN (mapper)
for line in sys.stdin :
    line = line.strip()
    lineSplit = line.split("\t")
    # Affectation des données telles qu'enregistrées dans le mapper
    code_commande = lineSplit[0]
    ville = lineSplit[1]
    quantite = lineSplit[2]
    timbre_client = lineSplit[3]
    
    # Conversion de quantite (string) en nombre (int)
    try : 
        quantite = int(quantite)
    except ValueError :
        continue
    # Aggreger les commandes par code_commande identique, sommer les quantités, compter les lignes
    # et calcul de la moyenne de la quantité sur la commande 
    if current_commande == code_commande :
        current_quantite += quantite
        current_nb += 1
        current_moyenne = current_quantite/current_nb
    else :
        if current_commande :
            #écrire dans la table output
            output_data.append((current_commande, current_ville, current_quantite, current_moyenne))
        current_quantite = quantite
        current_commande = code_commande
        current_timbre = timbre_client
        current_ville = ville
        current_nb = 1
        current_moyenne = current_quantite/current_nb

#On enregistre aussi la dernière ligne
if current_commande == code_commande :
    output_data.append((current_commande, current_ville, current_quantite, current_moyenne))

# Convertir output_data en DataFrame pandas
df = pd.DataFrame(output_data, columns=['Code_Commande', 'Ville', 'Quantite', 'Moyenne'])
# Trier grouped_data par 'Quantite' en ordre décroissant
sorted_data = df.sort_values(by=['Quantite'], ascending=[False])
# Sélectionner les 100 100 premières (=meilleures) commandes
top_100 = sorted_data.head(100)
# Sélectionner aléatoirement 5% (=0.05) des meilleures commandes
random_5_percent = top_100.sample(frac=0.05, random_state=42) #random_state pour conserver le même tirage
# Exporter vers Excel
excel_file = "/datavolume1/lot2.xlsx"
random_5_percent.to_excel(excel_file, index=False)

# Créer un graphe (PIE) par Ville et sauvegarder en PDF
plt.pie(x=random_5_percent['Moyenne'], labels=random_5_percent['Ville'], autopct='%.1f%%')
plt.title("Répartition des quantités moyennes par ville" ,
          loc='center', pad=3, fontsize=15, color="Darkred", fontweight='bold')
plt.savefig("/datavolume1/commandes_par_ville.pdf")
plt.show()      
