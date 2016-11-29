# coding: utf-8
from random import randint


def feedback(nb_a_trouver, nb_entre, coups_restants, coups) :
	print("Nombre à trouver : ", nb_a_trouver)
	if coups_restants > 1 and nb_entre != nb_a_trouver :
		print("Le nombre a trouver est plus petit" \
			if nb_entre > nb_a_trouver else \
			"Le nombre a trouver est plus grand")
		return 0
	elif nb_entre == nb_a_trouver :
		print("Bravo ! Tu as trouvé en ", coups, "coups !" \
			if coups_restants > 1 else \
			"Bravo, tu as gagné au dernier tour ! ")
		return 1
	else : 
		print("Perdu, le nombre cherché était ", nb_a_trouver)
		return -1
	
## Programme principal
nb_coups = int(input("Entrez le nombre de coups dont vous disposerez pour trouver la réponse : "))
valeur_max_random = int(input("Entrez la valeur maximum du nombre à trouver : "))

nb_a_trouver = randint(0, valeur_max_random)

print("Nombre à trouver : ", nb_a_trouver) # Debug

coups = 1
statut_jeu = 0
while statut_jeu == 0:	
	nb_entre = int(input("Entrez un nombre entre 0 et 100 : "))
	statut_jeu = feedback(nb_a_trouver, nb_entre, nb_coups, coups)			
	nb_coups -= 1
	coups += 1

#temps_max_repondre = 60 # Temps en secondes

