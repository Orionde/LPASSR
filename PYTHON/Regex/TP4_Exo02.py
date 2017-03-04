#!/usr/bin/env python3
# coding: utf-8

#############################################################
## Auteurs : Jorane Congio, Fabrice Edgard
## Date : 24/01/2017
## Titre : Expressions regulieres
## Consigne :  Produire un compte rendu de toutes les lignes
##   matchant des expressions regulieres d'un fichier donne
#############################################################

import re

def get_list_file():
## Retourne le contenu du fichier d'entrée sous forme de liste
	fichier = open('RegExpTP4_Ex2.txt', 'r')
	list_lignes = list()
	for line in fichier:
		list_lignes.append(line)
	return list_lignes
	fichier.close()


def afficheTitre(titre):
## Affiche la chaine de caractères passée en paramètre
##  dans le fichier de sortie en l'encadrant avec des étoiles
	fichier = open('SortieRegExpTP4_Ex2.txt', 'a')
	fichier.write('*' * len(titre) + '\n')
	fichier.write(titre + '\n')
	fichier.write('*' * len(titre) + '\n')
	fichier.close()

def afficheLignes(regex, lignes):
## Affiche les expressions qui matchent avec la regex
##  dans le fichier de sortie
	fichier = open('SortieRegExpTP4_Ex2.txt', 'a')
	compteur_lignes = 0
	for l in lignes:
		if re.search(regex, l):
			fichier.write(l)
			compteur_lignes += 1
	fichier.write('***** ' + str(compteur_lignes) + ' lignes trouvees *****\n\n')
	fichier.close()

## Programme principal
if __name__ == '__main__':
	
	afficheTitre("PYTHON : Fichier de sortie de l'exercice 2 du TP4") # Écrire nom rapport dans fichier sortie
	list_lines = get_list_file() # Récupérer une liste des lignes du fichier
	list_reg = [\ # Liste de tuples : expression régulière <-> titre
		('[A-Z0-9]', '1.a : lignes contenant des chiffres ou des majuscules'), \
		('\.', '1.b : lignes contenant des points'), \
		('\.\.\.', '1.c : lignes conentant trois points'), \
		('\s[0-9A-Fa-f]+\s|^[0-9A-Fa-f]+\s', '1.d lignes contenant des nombres hexadecimaux separes par des blancs'), \
		('[a-z0-9]{12}', '1.e : lignes contenant un mot d\'au moins 12 caracteres alphanumeriques'), \
		('^([^a]*a){5}[^a]*$', '1.f : lignes contenant exactement 5 lettres a (pas necessairement successives)'), \
		('\[|\]', '1.g : lignes contenant des crochets ( ] ou [ )'), \
		('^[a ]+$', '1.h : lignes ne contenant que des lettres a et des espaces'), \
		('(\d+\.){3}\d', '1.i : lignes contenant quelque chose qui ressemble a une adresse IP'), \
		('^[\n]$', '2.a : lignes vides'), \
		('^[ ]+$', '2.b : lignes blanches'), \
		('.', '2.c : lignes non vides'), \
		('^[^a]+$', '3.a : lignes qui ne contiennent pas de a'), \
		('^[^ ]+$', '3.b : lignes qui ne contiennent pas d\'espaces'), \
		('^[^\d]*$', '3.c : lignes qui ne contiennent pas de chiffres decimaux'), \
		('^(\d\d ){4}\d', '4 : lignes qui debutent par un numero de telephone au format 00 00 00 00 00'), \
		('^(\d\d[ \.-]){4}', '5 :  idem 4 mais on peut avoir . ou - a la place des espaces'), \
		('^(\(0\)|0)\d(( |-|.)\d\d){4}', '6 : idem 5 mais le 0 peut être entoure de parentheses'), \
		('(0|\(0\))(( |.| |-)\d\d\d){3}$', '7 : terminent par un tel au format 0 123 456 789, espaces, - ou . et (0)')
	]
	
	# On parcourt la liste 
	for reg, titre in list_reg:
		afficheTitre(titre) # On affiche le titre de la regex dans le fichier de sortie
		afficheLignes(reg, list_lines) # On traite les lignes de la liste 
			# et on écrit dans le rapport celles qui matchent avec la regex

