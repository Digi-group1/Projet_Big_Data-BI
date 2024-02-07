PROJET n°2 : HADOOP BIG DATA & Power BI
==========
Présentation et objectifs du projet 
-----------------------------------------
- Utilisation de Hadoop pour effectuer un map/reduce sur une base de données afin de filtrer les données pour analyse.
Les map/reduce sont écrits en Python.
- Utilsation de Happybase pour la création d'une base de données Hbase.
- Importation de cette base de données dans PowerBI pour production de tableaux de bord intéractifs.

Ce projet est constitué de trois lots à la demande du client, une fromagerie qui propose des cadeaux à sa clientèle en échange de points et/ou chèque et/ou timbres.
Cette société possède un Data Warehouse depuis 2004 au format csv (fichier source : dataw_fro03.csv). 
Ces données concernent la gestion des commandes de cadeaux sur 20 ans sur la France entière.

Environnements et configuration technique
------------------------------------------
Pour la réalisation de ce projet, nous disposons d'un environnement virtuel installé et configuré par Diginamic (Christophe G.). Cet environnement est composé de :
 - une machine virtuelle Linux sur laquelle sont installés Docker et le cluster Hadoop
 - une machine virtuelle Windows (Hidora) pour le développement et Power BI
<br>
Les technologies et logiciels utilisés sont :<br>
 - langage Python (version 3.5.4) et les librairies (ou modules) associées : Pandas, Matplotlib, Happybase, ...<br>
 - Visual Studio Code (en local)<br>
 - Hadoop pour le calcul distribué des map/reduce <br>
 - HBase pour le stockage de la base de données NoSQL (orientée colonnes)<br>
 - PuTTY pour la communication entre les environnements Windows et Linux<br>
 - Filezilla pour l'import de fichiers dans Hadoop<br>
 - Power BI pour la création des tableaux de bord interactifs<br>
 - ODBC : driver pour la connexion de Power BI à la base de données HBase<br>
 - Git et Github pour le rendu final et la gestion des versions<br>
 - Microsoft Teams et outils Office 365<br>


Lot 1 : Le client désire les statistiques suivantes
-------------------------------------------
<tr>
<td>1. Filtrer les données selon les critères suivants : </td><br>
 - Commandes passées entre 2006 et 2010 ;<br>
 - uniquement sur les départements 53, 61 et 28.
<br> 
<td>2. A partir du point 1 : Ressortir dans un tableau les 100 meilleures commandes avec la ville, la somme des quantités des articles commandés et la valeur de «timbrecde» pour chaque commande. La notion de meilleure commande désigne la somme des quantités la plus grande ainsi que le plus grand nombre de «timbrecde».</td>
<br> 
<td>3. Exporter le résultat dans un fichier Excel.</td>
</tr>


Lot 2 : Le client désire les statistiques suivantes
-------------------------------------------
<tr>
<td>1. Filtrer les données selon les critères suivants :</td><br>
 - Commandes passées entre 2011 et 2016 ;<br>
 - uniquement sur les départements 22, 49 et 53.
<br>
<td>2. A partir du point 1 : Ressortir de façon aléatoire 5% des 100 meilleures commandes avec la ville, la somme des quantités des articles sans «timbrecli» (c'est à dire timbrecli non renseigné ou à 0) avec la moyenne des quantités de chaque commande.</td>
<br>
<td>3. Exporter le résultat dans un fichier Excel et créer un graphique circulaire (PIE) par Ville en PDF</td><br>
</tr>


Lot 3 : Utiliser HBASE et Power BI
-------------------------------------------
<tr>
<td>1. Mettre en place une base NoSQL Hase pour stocker le contenu du fichier CSV.</td><br>
<td>2. Mettre en oeuvre un moteur de recherche avec Power BI pour interroger ce Data Warehouse.</td><br>
<td>3. Créer un/plusieurs tableau(x) de bord interactif(s) à partir de ces données.</td>
</tr>
