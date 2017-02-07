# BDD

### Intro
Au début[1960], on avait les bases sur des fichiers texte. PC pas puissants, il fallait optimiser l'accès et on avait pas non plus des requêtes de malade. Les accès étaient séquentiels, pas relationnels.

[1970] : premières bases de données réseau. Ensemble de fichiers reliés par des pointeurs, langage d'interrogation par
navigation.

[1980] Bases de données relationnelles, relation entre un ensemble de données. 

Relationnel : éviter la redondance de données. Centraliser et organiser les données. 

Ce qui est sympa avec la bdd : on pose une question sans avoir une connaissance précise du contenu de la base, en ayant juste
le modèle. Pas besoin d'être un spécialiste de base de donnée pour pouvoir faire une requête.

Tous les SGBP utilisent au moins le SQL, ce qui permet de poser des questions sans s'embêter la vie.

Le SGBD stocke la question, pas le résultat (met en cache). Du coup si modifié ne sort pas une valeur fausse car changée entre
temps. Chaque enregistrement a un hash pour voir tout de suite s'il a été modifié ou non.

Optimise les requêtes pour une réponse plus rapide. 

Bonne gestion des accès concurrents, cohérence conservée. Pas possible de consulter et éditer même donnée en même temps.

Gestion des utilisateurs / droits sur la base. mdp, privilèges d'accès différents selon utilisateurs / Groupes.

Les SGBD principaux :

Oracle, IBM, Microsof, MySQL/MariaDB, PostgreSQL

Oracle : + fonctionnalités

MySQL : - fn que Oracle, gratuit

MariaDB : ĉ oracle gratuit -> meilleurs cluster, plus grande commu.

PostgreSQL : bcp utilisé ds domaines pointus, un peu plus complexe à mettre en oeuvre. Petite commu donc moins de chance de
trouver des failles.

Les SGBD personnels :
	LibreOffice, Filemaker, Interbase, Microsoft Access -> JAMAIS utiliser pour des trucs pro. --> Pas fait pour. Pas sécurisé, sauvegarde pas terribles etc.

	
## MySQL
#### Installation:
```bash
sudo apt-get update
sudo apt-get install apache2 mysql-client mysql-server php5 php5-mysql
vi /etc/mysql/my.cnf # Remplacer bind address par 0.0.0.0 pour pas s'embêter

```
Tester php :
```bash
echo '<?php phpinfo(); ?>' > /var/www/html/info.php
```
Puis tester sur navigateur :  http://localhost:8080/info.php

#### Commandes MySQL

Se co à la bdd :

```
mysql -u username -h host -p
```

Voir les bases :
```
SHOW DATABASES;
```

Créer un utilisateur :
```
CREATE USER 'username'@'host' IDENTIFIED BY 'passwd';
```


Créer une table:
```
CREATE DATABASE table;
```

Supprimer une table :
```
DROP DATABASE table;
```


Changer de table:
```
USE table;
```


Montrer les utilisateurs :
```
SELECT host, user, password FROM mysql.user;
```


Sécuriser la BDD :
- changer mdp root
- empêcher co à distance en root (root uniquement depuis localhost)
- supprimer la/les BDD test


```
mysql_secure_installation
```

#### Récupérer mdp root
1 - stopper mysql :
```bash
service mysql stop
```

2 - le relancer via ça :
```
mysqld_safe --skip-grant-tables &
```
3 - changer mdp root :
```
mysql -u root
use mysql;
UPDATE USER	SET PASSWORD=('password') WHERE USER='root'
flush privileges;
quit
```

4 - redemarrer en mode normal :
```
service mysql stop
service mysql start
```

## Superviser bases
Installer mytop :
```
sudo apt-get install mytop
```

Observer une base en particulier :
```
mytop --prompt -d nom_base
```

## Sauvegarder base

Sauvegarde à chaud :
```bash
mysqldump --user=root --all-databases -p > save.sql.gz
```

Restauration :
```
mysql -u user -p
use database base;
source /chemin/vers/save.sql
```
ou
```bash
mysql -u myuser -p < /chemin/vers/save.sql
```

## Migration MySQL vers MariaDB
Installer mariadb :
```bash
apt-get install python-software-properties
apt-get install mariadb-server
```
Et tout est ok, il va juste demander un nouveau mdp root

## PostgreSQL

Se mettre en mode postgres :
```bash
su - postgres
```

Créer une base sans se co à la bdd:
```bash
su - postgres
createdb table
```

Exécuter une opération sans se connecter à la base :
```
su - postgres
psql -d temp -c "request"
```

Se connecter à une base :
```bash
su - postgres
psql nomtable
```

## NoSQL
Pas une base de donnée relationnelle

Bonne perf
On peut faire du clé/valeur
orienté colonnes : ressemble à du relationnel 
orientées document : stocké sous forme de données noeud et de relation

Pas forcément plus performant que du relationnel, dépend des cas.
SQL : uniquement vertical scaling (on peut juste augmenter la capacité du serveur qui fait tourner la base)
Sympa : on peut faire de l'horizontal scaling : disperser la BDD entre plusieurs serveurs. On distribue le contenu ET le traitement. Presque obligatoire quand on arrive sur des bases géantes.

Problème : pas de vérif d'intégrité, pas de transactions répides sur des objets de faible valeur et nombreux.

A priori : ne pas stocker des trucs trop importants dessus. Difficile à organiser correctement.

## Analyse de log

Penser à tester graylog : gratuit et largement suffisant pour des usage de base.

## Outil de test de charge NoSQL
https://github.com/brianfrankcooper/YCSB/wiki