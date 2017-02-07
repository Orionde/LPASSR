#!/usr/bin/env python3
#coding: utf-8

####################################################################################################################
## Auteur : Jorane Congio
## Date : 06/02/2017
## Titre : Ex2 CTP
## Consigne : Écrire dans un fichier de log les lignes de 'Failed password' tout en évitant les doublons
####################################################################################################################

if __name__ == '__main__':
	# Ouverture du fichier de log en lecture
	f_log = open('log_ssh.txt', 'r')
	
	# Ouverture du rapport en mode écriture
	f_out = open('Failed_Password_ssh.txt', 'w')
	
	# Liste contenant tous les sshd
	list_sshd = list() 
	
	
	nb_lignes_rapport =  0
	
	# On regarde si on a un failed passwd et si on a pas déjà écrit pour ce sshd
	for line in f_log:
		if 'Failed password' in line:
			sub_str = line.split()
			if sub_str[8] not in list_sshd:
				
				# Ajouter à la liste pour pas l'écrire deux fois
				list_sshd.append(sub_str[8])
				
				# On crée un liste avec uniquement ce qui nous intéresse
				tmp_list = sub_str[0:4] + sub_str[11:17] 
				
				# Puis en la transforme en chaine pour l'écrire (ajout espace !)				
				f_out.write(' '.join(tmp_list) + '\n')
				
				# Augmenter le compteur de lignes
				nb_lignes_rapport += 1
				
	# On n'oublie pas de fermer les fichiers
	f_log.close()
	f_out.close()
	
	print("Nombre de lignes écrites dans le rapport :", nb_lignes_rapport)
