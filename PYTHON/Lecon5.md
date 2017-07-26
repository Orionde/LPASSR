# Leçon 5

### C'est quoi ?

Une liste c'est une suite ordonnée pouvant contenir n'importe quel type de données : des entiers, des flotants, des chaines de caractères, des objets...

### Quand utilise-t-on une liste ?
On peut utiliser une liste pour
- Regrouper des valeurs ayant un lien entre elles : liste des notes des étudiants, liste des températures sur le dernier mois, etc
- Regrouper des valeurs de types différents dans une seule variable : chaines de caractères, objets, nombres
- Garder des valeurs dans un ordre précis
- Ajouter ou retirer des éléments facilement

### Déclaration

Déclaration à l'initialisation :
```python
list_CPU = ['i7-6700K', 'Xeon-E5506', 'm3-7Y30', 'FX 8300', 'FX 4300']  # liste contenant des noms de CPU
```
Python sait que l'on a déclaré une liste car on a utilisé des crochets pour délimiter les éléments. Ici, on a une liste de chaînes de caractères.

Déclaration à l'initialisation en utilisant des variables :
```python
cpu1 = 'i7-6700K'
cpu2 = 'Xeon-E5506'
list_CPU = [cpu1, cpu2]  # On ne met pas d'apostrophes ou de guillements : on désigne des variables
```

Déclaration sans initialisation :
```python
list_CPU = list()  # On déclare explicitement un objet de type list
list_Temp = []  # Déclaration implicite (à éviter, juste montrée ici car souvent utilisée !)
```

Si on ne sait pas par avance ce que va contenir la liste mais qu'on sait qu'on va l'utiliser, il faut la déclarer sans l'initialiser. Ça peut par exemple être utile pour remplir une liste par rapport à un input de l'utilisateur ou un fichier.

## Manipulations sur les listes

### Désigner un élément d'une liste :
Pour désigner un élément, on utilise obligatoirement son indice. Les indice sont numérotés à partir de 0 !
```python
>>> print(list_CPU[0])  # On print le premier élément de la liste
Xeon-E5506

>>> if list_CPU[0] == list_CPU[5]:  # On compare deux valeurs de la liste
    # Instructions

>>> cpu1 = list_CPU[2]  # On assigne à une nouvelle variable une valeur de la liste
```
Attention : Python réattribue les indices dès qu'on fait une modification sur la liste. Si on supprime un élément, l'indice des éléments se trouvant après l'élément supprimé est modifié.



### Ajouter un élément :
```python
>>>cpu0 = 'm3-7Y30'  # Une variable de type string
>>>list_CPU = list()  # Ne pas oublier de déclarer la liste, on ne peut pas utiliser append sur une liste qu'on a pas définie !
>>>list_CPU.append('Pentium G3460')  # On ajoute une nouvelle string
>>>list_CPU.append(5)  # On ajoute un int
>>>list_CPU.append(cpu0)  # On ajoute une variable, obligatoirement définie en amont
```

Retirer un élément :
```python
>>>list_CPU.remove('i7-6700K')  # On enlève l'indice dont la valeur vaut 'i7-6700K'
>>>list_CPU.remove(5)  # On enlève l'indice dont la valeur vaut 5
# En revanche, on ne peut pas enlever d'après un nom de variable :
>>>list_CPU.remove(cpu0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
# Python ne comprend pas de quoi on parle :
```

## Cas d'utilisation
#### Déclarer et afficher
#### Transformer un fichier en liste
#### Somme des éléments
#### Moyenne des éléments
#### Vérifier si une liste contient un élément
#### Supprimer les doublons
#### Séparer une liste

## Erreurs courantes et leur résolution
1 - Utiliser le mauvais type de délimiteur au moment de la création de la liste : `a = ('a', 'b')`, `a = ['a', 'b']` et `a = {'a', 'b'}` ont une signification très différente.

2 - Oublier de déclarer la liste avant de faire des opérations dessus :
```python
>>> list_CPU.append('Pentium G3460')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'list_CPU' is not defined
```
