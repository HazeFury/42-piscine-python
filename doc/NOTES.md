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

### ex4

- En Python, on lève une ValueError quand une fonction reçoit un argument qui a le bon type (ici un int pour l'eau), mais une valeur inappropriée (15 au lieu de 10 max). C'est sémantiquement la bonne erreur native à utiliser.

- La puissance de as e : Puisqu'on lève toujours la même erreur (ValueError), comment faire la différence à la réception ? C'est là que le message personnalisé entre en jeu. Quand tu fais raise ValueError("Mon message"), l'objet erreur embarque ce texte. Dans le except ValueError as e:, la variable e contient ce texte. On a juste à faire print(f"Error: {e}") et le bon message s'affiche automatiquement !

- L'ordre des conditions : On vérifie de haut en bas. Au premier raise rencontré, la fonction check_plant_health s'arrête net. C'est comme un return, le code en dessous ne sera jamais lu. C'est pour ça qu'on n'a pas besoin de mettre des else partout.

### ex5

**"How do all these error handling techniques work together to make a robust garden program?"**

C'est la complémentarité qui fait la force de ce code :

- Le raise te permet d'être proactif. Tu n'attends pas que Python plante avec un obscur TypeError ; tu stoppes l'action toi-même dès que tu vois un nom de plante vide ou trop d'eau.

- Le try/except te rend résilient. Au lieu que l'erreur ne fasse exploser l'application entière (et supprime potentiellement les données non sauvegardées), l'erreur est "absorbée", un message est affiché, et le programme passe à la suite sans broncher.

- Le finally te rend propre. Même si une erreur insurmontable survient pendant l'arrosage, tu as la garantie mathématique que le robinet virtuel sera fermé, évitant une fuite de mémoire (ou d'eau !).

**"What makes a program reliable when things go wrong?"**

Un programme fiable en C vérifie chaque retour de fonction (if (res == -1)). Un programme fiable en Python laisse le code s'exprimer de manière fluide, mais place des filets de sécurité sémantiques (except ValueError, except GardenError). En séparant la logique nominale (le bloc try) de la logique d'erreur (les blocs except), le code devient beaucoup plus lisible. La fiabilité vient de la prévisibilité : tu sais exactement où les erreurs prévues vont atterrir.