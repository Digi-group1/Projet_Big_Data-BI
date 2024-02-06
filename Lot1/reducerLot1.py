from operator import itemgetter
import sys
import pandas as pd

#Initialisation de toutes les variables qui vont servir
output_data=[]
current_commande = None
current_quantite = 0
current_timbre = 0
current_ville = None

# Lecture de chaque ligne depuis STDIN (mapper)
for line in sys.stdin:
    line = line.strip()
    lineSplit = line.split("\t")
    # Affectation des données telles qu'enregistrées dans le mapper
    code_commande = lineSplit[0]
    ville = lineSplit[2]
    quantite = lineSplit[-1]
    timbre_commande = lineSplit[4]
    
    # Conversion de quantite et timbreCde (type=string) en nombres (int ou float)
    try : 
        quantite = int(quantite)
        timbre_commande = float(timbre_commande)
    except ValueError :
        continue # ignorer les lignes si erreurs
    
    # Aggreger les commandes par numCde identiques et sommer les quantités
    if current_commande == code_commande :
        current_quantite += quantite
    else :
        if current_commande :
            # écrire dans la table output (STDOUT)
            output_data.append((current_commande,current_ville,current_quantite,current_timbre))
        current_quantite = quantite
        current_commande = code_commande
        current_timbre = timbre_commande
        current_ville = ville
            
      
# On enregistre aussi la dernière ligne
if current_commande == code_commande :
    output_data.append((current_commande,current_ville,current_quantite,current_timbre))

# Convertir output_data en DataFrame pandas
df = pd.DataFrame(output_data, columns=['Code_Commande', 'Ville', 'Quantite', 'TimbreCommande'])
# Trier par 'Quantite' et 'TimbreCommande' en ordre décroissant
sorted_data = df.sort_values(by=['Quantite', 'TimbreCommande'], ascending=[False, False])
# Sélectionner les 100 premières (=meilleures) commandes
top_100 = sorted_data.head(100)
# Exporter vers Excel (dans Hadoop)
excel_file = "/datavolume1/lot1.xlsx"
top_100.to_excel(excel_file, index=False)
