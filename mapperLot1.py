#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys
import pandas as pd
import logging
import csv

#Configuration pour Hadoop
logging.basicConfig(filename='debug.log',level=logging.DEBUG)
logging.debug("Entering mapperLot1.py")
#Listes des tris à faire, sur les départements et les années
output_data=[]
dep_liste=['53','61','28']
annee_liste=['2006','2007','2008','2009','2010']

# Ouverture du fichier CSV pour récupérer les données
data = csv.reader(sys.stdin)
# Parcourir chaque ligne et extraction des données utiles au problème
for lineSplit in data:
	logging.debug("Inside for loop " + str(lineSplit))
	
	dpt=lineSplit[4][:2]
	ville=lineSplit[5]
	numCde=lineSplit[6]
	timbreCde=lineSplit[9]
	qte=lineSplit[15]
	annee=lineSplit[7][:4]
		
	# Export des données qui collent aux filtres (départements et années) dans la table output
	if annee in annee_liste and dpt in dep_liste:
		print(numCde+"\t"+dpt+"\t"+ville+"\t"+annee+"\t"+timbreCde+"\t"+qte+"\t")

