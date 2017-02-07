#!/usr/bin/env python3
#coding: utf-8


####################################################################################################################
## Auteur : Jorane Congio
## Date : 06/02/2017
## Titre : Ex1 CTP
## Consigne : Écrire sur le terminal les lignes contenant Failed password et indiquer les nombre de lignes écrites
####################################################################################################################

# Programme principal
if __name__ == '__main__':
	f_log = open('log_ssh.txt', 'r')
	
	# S'incrémente à chaque tour de boucle
	nb_lignes_error =  0
	
	for line in f_log:
		# Si la ligne contient 'Failed password'
		if 'Failed password' in line:
			nb_lignes_error += 1
			print(line)
	
	print("Nombre d'erreurs de mot de passe :", nb_lignes_error)
		# On n'oublie pas de fermer les fichiers

	f_log.close()
