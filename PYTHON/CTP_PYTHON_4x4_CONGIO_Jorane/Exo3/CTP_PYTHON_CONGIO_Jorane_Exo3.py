#!/usr/bin/env python3
#coding: utf-8

####################################################################################################################
## Auteur : Jorane Congio
## Date : 06/02/2017
## Titre : Ex3 CTP
## Consigne : Écrire dans le bon fichier de log en fonction de la ligne de log
####################################################################################################################

if __name__ == '__main__':
	
	# Ouverture du fichier de log en lecture
	f_log = open('log_sudo.txt', 'r')
	
	# On ouvre les fichiers de rapport
	f_install = open('install.txt', 'w')
	f_poff = open('poweroff.txt', 'w')
	f_restart = open('restart.txt', 'w')
	f_start = open('start.txt', 'w')
	f_stop = open('stop.txt', 'w')
	
	
	# On voit pour chaque ligne dans quel fichier on écrit
	for line in f_log:
		if 'install' in line:
			f_install.write(line)
		elif 'poweroff' in line:
			f_poff.write(line)
		elif 'restart' in line:
			f_restart.write(line)
		elif 'start' in line: # On aura pas les restart car c'est un elif
			f_start.write(line)
		elif 'stop' in line:
			f_stop.write(line)
	
		
	# On n'oublie pas de fermer les fichiers
	f_log.close()
	f_install.close()
	f_poff.close()
	f_restart.close()
	f_start.close()
	f_stop.close()
	
