
import argparse


def supprime_user(login):
	print(login)
	
def modifier_groupe_user(login,new_groupe):
	print(login,new_groupe)

def modifier_nom_user(login):
	print(login)
	
def import_csv_file(fichier):
	print(fichier)	

parser = argparse.ArgumentParser(description='A remplir', prog='Projet python')

parser.add_argument('-s','--supprimer', metavar='login', nargs='+',
                    help='Supprime un ou plusieurs utilisateur de la base')
                    
                    
parser.add_argument('-mn','--modifier_nom', nargs='+' ,metavar=('login'), 
                    help='Remplace le nom')

parser.add_argument('-mg','--modifier_groupe', metavar=('login','groupe'),  nargs=2,
                    help='Remplace le groupe')


parser.add_argument('-i','--import_csv', metavar='fichiercsv', nargs='+',
                    help='Importer un fichier.csv dans la base')



args = parser.parse_args()

if args.supprimer:

	supprime_user(args.supprimer[0])
	
elif args.modifier_groupe:

	modifier_groupe_user(args.modifier_groupe[0],args.modifier_groupe[1])
elif args .modifier_nom:
	modifier_nom_user(args.modifier_nom[0])
	
elif args.import_csv:
	import_csv_file(args.supprimer[0])
