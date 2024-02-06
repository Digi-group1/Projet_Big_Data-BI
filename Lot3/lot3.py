import happybase
import pandas as pd
import csv

# Fonction de creation et remplissage table 

def createTable():
    connection.create_table(
    'commande_goodies',
	{'commande': dict()
 	})

# Connection à HBase
connection=happybase.Connection('node175832-env-1839015-etudiant12.sh1.hidora.com',9090)
connection.open()

# Création de la table 'commande_goodies'
createTable()

# Connexion à la table 'commande_goodies'
table=connection.table('commande_goodies')

# Écriture dans la table
with open("dataw_fro03.csv", "r", encoding='utf-8') as csvfile :
	data = csv.reader(csvfile, delimiter=',', quotechar='"')
	numligne=1

	# Lecture du fichier csv et stockage dans des variables.
	# Si les valeurs sont à NULL :
	# - remplacées par "0" pour les valeurs numériques
	# - remplacées par "" pour les chaînes de caractères
	for lineSplit in data:
		
		if lineSplit[0]!="NULL":
			codcli = lineSplit[0]
		else:
			codcli='0'

		if lineSplit[1]!="NULL":
			genrecli = lineSplit[1]
		else:
			genrecli=""

		if lineSplit[2]!="NULL":
			nomcli = lineSplit[2]
		else:
			nomcli=""

		if lineSplit[3]!="NULL":
			prenomcli = lineSplit[3]
		else:
			prenomcli=""

		if lineSplit[4]!="NULL":
			cpcli = lineSplit[4]
		else:
			cpcli=""

		if lineSplit[5]!="NULL":
			villecli = lineSplit[5]
		else:
			villecli=""

		if lineSplit[6]!="NULL":
			codcde = lineSplit[6]
		else:
			codcde = '0'
		
		# pour la date de la commande : vérification du format de la date
		if lineSplit[7]!="NULL" :
			try:
				pd.to_datetime(lineSplit[7])
				datcde =lineSplit[7]
			except:
				continue
		else:
			datecde = ""

		if lineSplit[8]!="NULL":
			timbrecli = lineSplit[8]
		else:
			timbrecli = '0'

		if lineSplit[9]!="NULL":
			timbrecde = lineSplit[9]
		else:
			timbrecde = '0'
		
		if lineSplit[10]!="NULL":
			Nbcolis = lineSplit[10]
		else:
			Nbcolis = '0'

		if lineSplit[11]!="NULL":
			cheqcli  = lineSplit[11]
		else:
			cheqcli  = '0'
		
		barchive=lineSplit[12]
		bstock=lineSplit[13]
		codobj=lineSplit[14]

		if lineSplit[15]!="NULL":
			qte = lineSplit[15]
		else:
			qte = '0'
		
		if lineSplit[16]!="NULL":
			Colis = lineSplit[16]
		else:
			Colis = '0'
		
		if lineSplit[17]!="NULL":
			libobj = lineSplit[17]
		else:
			libobj = ""

		if lineSplit[18]!="NULL":
			Tailleobj = lineSplit[18]
		else:
			Tailleobj = ""
		
		if lineSplit[19]!="NULL":
			Poidsobj = lineSplit[19]
		else:
			Poidsobj = '0'

		if lineSplit[20]!="NULL":
			points = lineSplit[20]
		else:
			points = '0'
		
		indispobj=lineSplit[21]
		
		if lineSplit[22]!="NULL":
			libcondit = lineSplit[22]
		else:
			libcondit = '0'
		
		prixcond=lineSplit[23]
		puobj=lineSplit[24]
	
		try:
			# Insertion des valeurs dans la table 'commande_goodies'
			table.put('%d'%numligne, {'commande:codcli': codcli,
							 'commande:genre':genrecli,'commande:nom': nomcli,
							 'commande:prenom':prenomcli,'commande:CP': cpcli, 
							 'commande:ville':villecli, 'commande:codcde' :codcde,
							 'commande:date':datcde, 'commande:timbrecli':timbrecli,
							 'commande:timbrecde':timbrecde, 'commande:Nbcolis':Nbcolis,
							 'commande:chequecli': cheqcli, 'commande:barchive':barchive,
							 'commande:bstock':bstock, 'commande:codeobj':codobj,
							 'commande:quantite': qte, 'commande:Colis':Colis,
							 'commande:libellecommande:':libobj, 
							 'commande:taillecommande': Tailleobj,'commande:Poidsobj':Poidsobj,
							 'commande:points': points, 'commande:indispobj': indispobj,
							 'commande:libcondit': libcondit,
							 'commande:prixcond': prixcond, 'commande:puobj': puobj							
							 })
		
		except ValueError:
			print("Something went wrong!")
			# error handling goes here; nothing is sent to HBase
			pass
		numligne+=1

# Vérification que la table a été créée et sélectionnée
print("La liste des tables sur HBASE est : \n")
print(connection.tables())
print("Nous avons choisi la table : \n")
print(table)

# Fermeture de la connexion
connection.close()
