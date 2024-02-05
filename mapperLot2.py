#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys
import logging
import csv

# Configuration pour Hadoop
logging.basicConfig(filename='debug.log',level=logging.DEBUG)
logging.debug("Entering mapperLot2.py")
# Listes des tris à faire, sur les départements et les années
output_data=[]
dep_liste=['22','49','53']
annee_liste=['2011','2012','2013','2014','2015','2016']

data = csv.reader(sys.stdin)
# Parcourir chaque ligne et extraire les données utiles au problème
for lineSplit in data:
	logging.debug("Inside for loop " + str(lineSplit))
	dpt=lineSplit[4][:2]
	ville=lineSplit[5]
	numCde=lineSplit[6]
	qte=lineSplit[15]
	annee=lineSplit[7][:4]
	timbreCli=lineSplit[8]
	
# Export des données qui collent aux filtres (départements, années et timbreCli) dans la table output
if annee in annee_liste and dpt in dep_liste and (timbreCli == "NULL" or timbreCli == "0"):
	print(numCde+"\t"+ville+"\t"+qte+"\t"+timbreCli)
