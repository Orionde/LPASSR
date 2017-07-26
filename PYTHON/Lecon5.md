# Leçon 5 : les listes

### C'est quoi ?

Une liste est une suite ordonnée pouvant contenir n'importe quel type de données : des entiers, des flotants, des chaines de caractères, des objets... Une liste est un objet python avec beaucoup de méthodes utiles qui simplifient la vie.

### Quand utilise-t-on une liste ?
On peut utiliser une liste pour
- Regrouper des valeurs ayant un lien entre elles : liste des notes des étudiants, liste des températures sur le dernier mois, etc
- Regrouper des valeurs de types différents dans une seule variable : chaines de caractères, objets, nombres
- Garder des valeurs dans un ordre précis
- Ajouter ou retirer des éléments facilement

### Déclaration

Déclaration à l'initialisation :
```python
>>> list_CPU = ['i7-6700K', 'Xeon-E5506', 'm3-7Y30', 'FX 8300', 'FX 4300']  # liste contenant des noms de CPU
```
Python sait que l'on a déclaré une liste car on a utilisé des crochets pour délimiter les éléments. Ici, on a une liste de chaînes de caractères.

Déclaration à l'initialisation en utilisant des variables :
```python
>>> cpu1 = 'i7-6700K'
>>> cpu2 = 'Xeon-E5506'
>>> list_CPU = [cpu1, cpu2]  # On ne met pas d'apostrophes ou de guillements : on désigne des variables
```

Déclaration sans initialisation :
```python
>>> list_CPU = list()  # On déclare explicitement un objet de type list
>>> list_Temp = []  # Déclaration littérale. Potentiellement plus rapide suivant le code. Pour destiné à être maintenu, mieux vaut utiliser la forme explicite. Cela permettra à une personne n'étant pas familier avec python de comprendre le code plus facilement. 
```

Si on ne sait pas par avance ce que va contenir la liste mais qu'on sait qu'on va l'utiliser, il faut la déclarer sans l'initialiser. Ça peut par exemple être utile pour remplir une liste par rapport à un input de l'utilisateur ou un fichier.

## Désigner un élément d'une liste :
Pour désigner un élément, on utilise obligatoirement son indice. Les indice sont numérotés à partir de 0 !
```python
list_CPU = ['i7-6700K', 'Xeon-E5506', 'm3-7Y30', 'FX 8300', 'FX 4300']
# par indice
>>> print(list_CPU[0])  # On print le premier élément de la liste
i7-6700K

>>> if list_CPU[0] == list_CPU[5]:  # On compare deux valeurs de la liste
    # Instructions

>>> cpu1 = list_CPU[2]  # On assigne à une nouvelle variable une valeur de la liste
# par indice négatif 
>>> print(list_CPU[-1])  # On met un index négatif pour partir de la fin de la liste
FX 4300
>>> print(list_CPU[-2])
FX 830

# Désigner plusieurs éléments à la fois
>>> print(list_CPU[0:2]) # Afficher les indices compris entre 0 et 2 (0 inclu, 2 exclu). Interprétable par "Jusqu'au deuxième élément, qui a l'indice 1"
['i7-6700K', 'Xeon-E5506']
>>> print(list_CPU[:3]) # Afficher depuis le début jusqu'à l'indice 3 (indice 3 exclu)
['i7-6700K', 'Xeon-E5506', 'm3-7Y30']
>>> print(list_CPU[3:])  # Afficher à partir de l'indice 3 jusqu'à la fin de la liste
['FX 8300', 'FX 4300']
```
Attention : Python réattribue les indices dès qu'on fait une modification sur la liste. Si on supprime un élément, l'indice des éléments se trouvant après l'élément supprimé est modifié.

## Méthodes des listes
#### Ajouter un élément à la fin:
```python
>>> cpu0 = 'm3-7Y30'  # Une variable de type string
>>> list_CPU = list()  # Ne pas oublier de déclarer la liste, on ne peut pas utiliser append sur une liste qu'on a pas définie !
>>> list_CPU.append('Pentium G3460')  # On ajoute une nouvelle string
>>> list_CPU.append('i7-6700K')
>>> list_CPU.append(5)  # On ajoute un int
>>> list_CPU.append(cpu0)  # On ajoute une variable, obligatoirement définie en amont
```

#### Retirer un élément :
```python
>>> cpu0 = 'm3-7Y30'
>>> list_CPU = ['Pentium G3460', 'i7-6700K', 5, cpu0]  # Initialisation de la liste
>>> list_CPU.remove('i7-6700K')  # On enlève l'indice dont la valeur vaut 'i7-6700K'
>>> list_CPU.remove(5)  # On enlève l'indice dont la valeur vaut 5

# En revanche, on ne peut pas enlever d'après un nom de variable :
>>> list_CPU.remove(cpu0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list

# Python ne comprend pas de quoi on parle : il a remplacé le nom de la variable par son contenu. La liste ne conserve pas de traces de la provenance des valeurs qu'elle contient. Elle ne connait que leur type et leur valeur.
>>> print(list_CPU)
['m3-7Y30', 'Pentium G3460']  # En affichant la liste on voit bien que le nom de la variable cpu0 a été remplacé par son contenu 'm3-7Y30'. Les suppressions effectuées via la valeur de l'indice ont bien été effectuées.
```
####  Insérer un élément à une position précise
```python
>>> list_jours = ["Lundi", "Mardi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
>>> list_jours.insert(2,"Mercredi") # Position puis indice
>>> print(list_jours)
["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
```
#### Etendre
```python
>>> list_jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
>>> list_jours.extend(["Samedi", "Dimanche"]) # Attention ! C'est bien une liste en paramètre de la méthode !
>>> print(list_jours)
["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
```
#### Enlever le dernier élément
```python
>>> list_jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
>>> dernier_jour = list_jours.pop()
>>> print list_jours
["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
>>> print(dernier_jour)
Dimanche
```
#### Trier
Ne pas s'amuser à sort des listes mixes avec python, ou du moins pas sans savoir ce qu'on fait ;)
```python
>>> list_jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
>>> list_jours.sort()
>>> print(list_jours)
['Dimanche', 'Jeudi', 'Lundi', 'Mardi', 'Mercredi', 'Samedi', 'Vendredi'] # Trié par ordre alphabétique
```
#### Trouver le minimum et le maximum
```python
>>> list_temp = [25, 30, 12, 22, 34]
>>> print(min(list_temp))
12
>>> print(max(list_temp))
34
```
#### Inverser l'ordre de la liste :
```python
>>> list_temp = ['a', 'b', 'c', 'd']
>>> list_temp.reverse()
>>> print(list_temp)
['d', 'c', 'b', 'a']
```
### Concaténer
Les listes ne sont pas modifiées
```python
>>> L1 = [12, 15, 16, 11, 19, 17]
>>> L2 = [13, 20, 32]
>>> print(L1+L2)
[12, 15, 16, 11, 19, 17, 13, 20, 32]
>>> print(L1)
[12, 15, 16, 11, 19, 17]
>>> print(L2)
[13, 20, 32]
```
### Connaitre l'indice d'une valeur
La méthode index permet de retourner l'indice d'un élément de la liste :
```python
list_CPU = ['i7-6700K', 'Xeon-E5506', 'm3-7Y30', 'FX 8300', 'FX 4300']
>>> print list_CPU.index('m3-7Y30'):
2
```

## Cas d'utilisation
#### Afficher une liste via une boucle for
```python
list_CPU = ['i7-6700K', 'Xeon-E5506', 'm3-7Y30', 'FX 8300', 'FX 4300']
>>> for l in list_CPU:
>>>     print(l)
i7-6700K
Xeon-E5506
m3-7Y30
FX 8300
FX 4300

# Les valeurs sont affichées les unes en dessous des autres. Si tu ne comprends pas pourquoi va faire un tour du côté de la leçon sur les print et celle sur les for :p
```
#### Transformer un fichier en liste
```python
list_CPU = ['i7-6700K', 'Xeon-E5506', 'm3-7Y30', 'FX 8300', 'FX 4300']
>>> with open('CPU_list', 'r') as f_cpu:
>>>     for l in list_CPU:
>>>         f_cpu.write(l)
# Pas besoin de close le fichier grâce au with open. En revanche, ne pas oublier l'indentation : dès qu'on en sort la variable f_cpu est automatiquement détruite par Python.
```
#### Somme et moyenne des éléments
```python
>>> list_temp = [25, 30, 12, 22, 34]
>>> somme = 0
>>> for l in list_temp:
>>>     somme += l
>>> print somme
123
>>> moyenne = somme / len(list_temp) # len est une fonction retournant le nombre d'éléments
>>> print(moyenne)
24
```
#### Vérifier si une liste contient un élément
Le mot clé in. Python ne se complique pas la vie ;)
```python
list_CPU = ['i7-6700K', 'Xeon-E5506', 'm3-7Y30', 'FX 8300', 'FX 4300']
>>> if 'i7-6700K' in list_CPU:
>>>   print("Trouvé !")
Trouvé !  # Affiche trouvé car l'élément est dans la liste
```
On peut aussi faire comme ça, mais c'est moins moins joli.
```python
list_CPU = ['i7-6700K', 'Xeon-E5506', 'm3-7Y30', 'FX 8300', 'FX 4300']
>>> for i in list_CPU:
>>>     if i == 'i7-6700K':
>>>         print("Trouvé !")
Trouvé !  # Affiche trouvé car l'élément est dans la liste
```
#### Supprimer les doublons
Idée de cet algo : on crée une liste temporaire tmp. On parcourt la liste d'origine en vérifiant pour chaque élément s'il ne se trouve pas déjà dans la liste temporaire. Une fois la boucle finie, on remplace la liste d'origine par la liste sans doublons.
```python
>>> list_temp = [25, 30, 12, 22, 34, 22, 35, 30]
>>> tmp = list()
>>> for i in list_temp:
>>>     if i not in tmp:
>>>         tmp.append(i)
>>> print(tmp)
[25, 30, 12, 22, 34, 35]
>>> list_temp = tmp
>>> print list_temp

>>> del tmp # Dans un souci d'optimisation on peut supprimer la variable temporaire pour ne pas surcharger la mémoire
```

## Erreurs courantes et leur résolution
1 - Utiliser le mauvais type de délimiteur au moment de la création de la liste : `a = ('a', 'b')`, `a = ['a', 'b']` et `a = {'a', 'b'}` ont une signification très différente.

2 - Oublier de déclarer la liste avant de faire des opérations dessus :
```python
>>> list_CPU.append('Pentium G3460')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'list_CPU' is not defined
```
