
import random
import hashlib
import smtplib

"""
Argument: Taille (Taille du mot de passe)

Génération du Mot de passe avec des [A-Za-z0-9] et des caractères spéciaux avec une taille fixe

Retourne: passwd 
"""
def mdp(taille):

	element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/$%&.:?!"
	passwd = ""
	 
	for i in range(taille): 
		passwd = passwd + element[random.randint(
												0, 
												len(element)-1)]
	return passwd
"""
Argument: Le mot de passe
gen_hash > hash en SHA1 le mot de passe
Retourne: Le hash du mot de passe pris en argument
"""

def gen_hash(mot_de_passe):
	mdp_sha1 = hashlib.sha1(mot_de_passe.encode())
	mdp_hash = mdp_sha1.hexdigest()
	
	return mdp_hash

"""
Argument : mot de passe
Envoye un mail a l'utilisateur

"""
	
def envoye_mdp(password):
	fromaddr = 'fabrice.edgard@gmail.com'
	toaddrs  = 'akiyuki.kai@gmail.com'
	msg = 'Ton mot de passe est:'+str(password)


	# Credentials (if needed)
	username = 'fabrice.edgard@gmail.com'
	mdp = 'chopper50B'
	
	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	print("1")
	#server.set_debuglevel(1)
	server.starttls()
	print("2")
	server.login(username,mdp)
	
	print("3")
	server.sendmail(fromaddr, toaddrs, msg)
	print("4")
	server.quit()
	print("5")
	#return problems


password=mdp(10)
print(password)

print(gen_hash(password))

print(gen_hash(password))

envoye_mdp(password)




