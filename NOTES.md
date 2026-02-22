# Observations et notions clés sur chaque exercices

## Module 02

### ex1

La capture multiple avec un Tuple

```python
except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
```
C'est la réponse à la question "Think about" du sujet. Pour attraper plusieurs erreurs en même temps avec le même traitement, il faut obligatoirement les mettre dans un tuple (entre parenthèses). Si tu ne mets pas les parenthèses, Python pensera que le deuxième mot est l'alias de l'erreur (comme le as e), ce qui fera crasher ton code.


**Pourquoi Python a-t-il autant de types d'erreurs ?**

La *granularité de la gestion*.

Si tu essaies d'ouvrir un fichier JSON, de le lire, et de chercher une valeur dedans :

Si ça lève un FileNotFoundError : Tu peux afficher "Veuillez créer le fichier de sauvegarde".

Si ça lève un KeyError : Tu peux afficher "Le fichier de sauvegarde est corrompu, il manque la donnée X".
Avoir des erreurs spécifiques permet à ton programme de s'auto-réparer ou d'orienter l'utilisateur précisément, au lieu de juste dire "Erreur fatale".

### ex2

**Quand créer ses propres erreurs au lieu d'utiliser celles de Python ?**

Imagine que tu utilises un simple ValueError quand ton réservoir d'eau est vide. Plus tard dans ton code, tu fais un try/except ValueError pour gérer ça.

Mais que se passe-t-il si, à l'intérieur de ce bloc, une fonction plante parce qu'elle a essayé de faire int("tomate") ? Cela lèvera aussi un ValueError. Ton programme croira que le réservoir est vide alors qu'il y a eu un problème de conversion de texte !

Créer WaterError te garantit que si tu attrapes cette erreur, c'est 100% lié à l'eau. C'est ce qu'on appelle la sémantique : le code s'explique de lui-même. Venant du C, vois ça un peu comme des codes d'erreur d'un enum très précis, plutôt que de toujours renvoyer -1.

**Comment l'héritage aide-t-il à organiser les erreurs ?**

C'est la partie la plus puissante, démontrée par la boucle for de mon code.
Puisque PlantError est une GardenError (héritage), tu as désormais deux niveaux de contrôle :

Le contrôle fin : Tu utilises except WaterError: si tu as une solution précise en tête (ex: déclencher la pompe à eau de secours).

Le contrôle global : Tu utilises except GardenError: si tu veux juste dire "Il y a un problème dans le jardin, j'arrête tout et j'envoie un SMS au jardinier", sans te soucier de savoir si c'est la tomate qui fane ou l'eau qui manque. Et surtout, en utilisant except GardenError:, tu laisses "passer" les vraies erreurs système (comme un MemoryError) pour qu'elles fassent crasher le programme normalement au lieu de les étouffer par erreur.

### ex3

-  Les f-strings masquent les erreurs de type en forçant la conversion en texte.

- Le mot-clé raise est ton meilleur ami pour contrôler le flux de tes exceptions.

- Le bloc finally sert de femme/homme de ménage : il ferme les fichiers, coupe les connexions réseau, éteint les systèmes. Mais il ne prend jamais de décision sur la suite du programme (pas de return, pas de break, pas de continue).