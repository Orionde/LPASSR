#!/usr/bin/env python3
#coding: utf-8

####################################################################################################################
## Auteur : Jorane Congio
## Date : 06/02/2017
## Titre : Ex4 CTP
## Consigne : Faire un compte rendu d'un fichier de log de la manière la plus utile possible
####################################################################################################################

def uniq(f_log):
# Retourner une liste à partir du fichier sans les doublons de lignes
	list_uniq = list()
	for line in f_log:
		# On conserve les lignes uniques
		if line not in list_uniq:
			list_uniq.append(line)
	return list_uniq
	
# 	
def split_log(li):
# Retourne la liste des lignes des logs de splunk
	list_splunk = list()
	
	for s in list_uniq:
		if 'splunk' in s:
			list_splunk.append(s)
		
	return list_splunk
	
def write_in_file(titre, liste, f_anomalie):
# On écrit la liste dans le fichier en mettant un espace après
	f_anomalie.write(titre)
	for s in liste:
		if 'Peer Connection Initiated' in s:
			f_anomalie.write('\n')
		f_anomalie.write(s)
	
if __name__ == '__main__':
	
	# Ouverture du fichier de log en lecture
	f_log = open('openvpn_log.txt', 'r')
	
	# On ouvre le fichier de rapport
	f_anomalie = open('anomalies_VPN.txt', 'w')
	
	# On récupère la liste des lignes sans doublons
	list_uniq = uniq(f_log)
	
	# On split pour avoir deux listes (en fonction du système de log)
	list_splunk = split_log(list_uniq)
			
	# On écrit nos listes dans le fichier
	write_in_file("** Erreurs relevées par splunk : **\n", list_splunk, f_anomalie)
	
	
	# On n'oublie pas de fermer les fichiers
	f_log.close()
	f_anomalie.close()
	
	
	"""
	À la base je voulais grouper les logs par session tout en enlevant les doublons des deux systèmes de logs différents.
	J'ai cependant rencontré les problèmes suivants :
		- Rien n'identifie la session VPN dans les logs (pas d'ID de session)
		- C'est toujours le même utilisateur qui se connecte au même serveur
		- Les deux systèmes de log marquent une heure différente de quleques secondes pour des événements s'étant sans doute produit simultanément
		
	Il est donc très difficile de comprendre qu'est-ce qui se rapporte à quoi.
	
	J'ai donc choisi de choisir le système ayant le plus de verbosité (splunk), essayant de grouper en mettant un espace après les lignes contenant 'Peer Connection Initiated'.
	"""
