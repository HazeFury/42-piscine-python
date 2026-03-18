# 🧙‍♂️ Memento : Programmation Fonctionnelle & Décorateurs

Ce document résume les concepts clés abordés lors du module sur la Programmation Fonctionnelle (PF), les Fonctions d'Ordre Supérieur (HOF), les Closures, et la création de décorateurs en Python.

## 0. Le Paradigme de la Programmation Fonctionnelle

La programmation fonctionnelle (PF) n'est pas un outil ou une bibliothèque, c'est une **façon de penser** l'architecture de ton code. Contrairement à la Programmation Orientée Objet (POO) qui modélise le monde sous forme d'objets ayant un "état" (des attributs qui changent), la PF voit le code comme une série de transformations mathématiques. 

Pour qu'un code soit considéré comme "fonctionnel", il s'appuie généralement sur 3 grands piliers :

### 1. Les Fonctions Pures (Pure Functions)
C'est le Saint Graal de la PF. Une fonction est "pure" si elle respecte deux règles absolues :
* **Déterminisme :** Pour les mêmes arguments en entrée, elle retournera TOUJOURS exactement le même résultat. Elle ne dépend pas de l'heure qu'il est, de l'aléatoire, ou d'une base de données externe.
* **Aucun effet de bord (No Side Effects) :** Elle ne modifie absolument rien en dehors d'elle-même. Elle ne change pas de variables globales, n'écrit pas dans un fichier, et ne modifie pas les objets qu'on lui passe en paramètre.

```python
	# Approche Impure (à éviter en PF)
	historique = []
	def ajouter_sort_impur(sort):
		historique.append(sort) # Effet de bord : modifie une variable externe !

	# Approche Pure
	def ajouter_sort_pur(ancien_historique, nouveau_sort):
		# Retourne une nouvelle donnée sans toucher à l'originale
		return ancien_historique + [nouveau_sort]
```

### 2. L'Immuabilité (Immutability)
En programmation fonctionnelle, les données sont sacrées. Une fois qu'une variable est créée, elle ne doit **jamais** être modifiée. Si tu veux changer une donnée, tu ne l'écrases pas : tu en crées une nouvelle version avec la modification appliquée. Cela élimine 90% des bugs liés au partage de données entre plusieurs fonctions.

```python
	# Approche Classique (Mutabilité)
	stats = {"hp": 100, "mana": 50}
	stats["mana"] -= 10 # La donnée originale est détruite et remplacée

	# Approche Fonctionnelle (Immuabilité)
	stats_initiales = {"hp": 100, "mana": 50}
	# On crée un nouveau dictionnaire à partir de l'ancien
	nouvelles_stats = {**stats_initiales, "mana": 40}
```

### 3. Les Fonctions comme "Citoyens de Première Classe"
En Python (et dans les langages fonctionnels), une fonction n'est pas juste un bloc d'instructions figé. C'est une donnée comme une autre (au même titre qu'un Int, un String ou une Liste). 
Cela signifie qu'une fonction peut être assignée à une variable, passée en argument à une autre fonction (créant ainsi des Fonctions d'Ordre Supérieur), ou retournée par une autre fonction (créant ainsi des Closures et des Décorateurs). C'est ce pilier qui rend toute la magie de ce module possible !

## 4. Les Fonctions d'Ordre Supérieur (HOF)
* **Le concept :** C'est une fonction qui prend une autre fonction en paramètre, OU qui retourne une fonction.
* **L'intérêt :** Séparer la logique métier (le *quand* ou le *combien de fois*) du comportement (le *quoi*). C'est le principe de l'usine (*Factory Pattern*).
* **Exemples natifs :** `map()`, `filter()`, `sorted()`.

## 5. Le Lexical Scoping & Les Closures
* **Lexical Scoping (Portée Lexicale) :** Une fonction fige son contexte (la valeur de ses variables) en se basant sur l'endroit où elle est **écrite** dans le fichier, pas l'endroit où elle est **exécutée**. 
* **Closure (Fermeture) :** C'est la conséquence du scoping. C'est une fonction enfant qui part avec un "sac à dos" invisible contenant les variables de sa fonction parente, même après la fin de cette dernière.
* **Le mot-clé `nonlocal` :** L'ascenseur. Il sert à dire à Python de ne pas créer une variable locale, mais de monter d'un étage pour aller modifier la variable dans le sac à dos du parent.
* **L'intérêt :** Avoir une mémoire persistante et sécurisée (encapsulée) sans avoir à sortir l'artillerie lourde d'une Classe orientée objet.

```python
# Exemple de Closure avec nonlocal

def usine_a_compteur():
    count = 0
    def compteur():
        nonlocal count
        count += 1
        return count
    return compteur
```

## 6. Les Artefacts de `functools`
* **`reduce` (Le compresseur) :** Applique une fonction de proche en proche pour écraser une liste en une seule valeur. Parfait pour les cumuls, mais attention à la lisibilité.
* **`partial` (Le pré-remplisseur) :** Gèle certains arguments d'une fonction pour en créer une nouvelle, plus simple à appeler (très utile pour les *callbacks*).
* **`lru_cache` (La mémoire haute vitesse) :** Mémorise les résultats des appels précédents (Mémoïsation). Échange de la RAM contre de la puissance CPU. Ne marche qu'avec des arguments *hashables* (pas de listes !).
* **`singledispatch` (Le standardiste) :** Permet la surcharge de fonction. Redirige l'exécution vers des sous-fonctions différentes en analysant uniquement le **type du premier argument**. Respecte le principe d'architecture *Open/Closed*.

## 7. Les Décorateurs (Le boss final)
* **Le concept :** C'est juste du sucre syntaxique (`@`) pour une HOF. Ça prend une fonction, l'emballe dans une coquille (`wrapper`) pour ajouter un comportement avant/après, et retourne la coquille.
* **Les poupées russes (Inception) :** Si un décorateur prend un paramètre (ex: `@power_validator(50)`), il faut **3 niveaux** de fonctions imbriquées :
	1. L'usine (reçoit les paramètres du décorateur)
	2. Le décorateur (reçoit la fonction)
	3. Le wrapper (reçoit les arguments de la fonction)
* **`@wraps(func)` :** L'anti-usurpation d'identité. Il copie le nom (`__name__`) et la documentation (`__doc__`) de la fonction d'origine pour les coller sur le wrapper. Ça évite que l'extérieur du programme ne voie qu'une coquille vide.

```python
# Structure d'un décorateur paramétré
from functools import wraps

def mon_decorateur(param):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Logique métier avant l'appel
            result = func(*args, **kwargs)
            # Logique métier après l'appel
            return result
        return wrapper
    return decorator
```

## 8. La méthode Statique (`@staticmethod`)
* **Le concept :** Une méthode dans une classe qui ne prend ni `self` (l'objet), ni `cls` (la classe globale).
* **L'intérêt :** Purement organisationnel (Namespacing). On range une fonction utilitaire dans une classe pour que le code soit sémantiquement propre et logique, même si elle n'a pas besoin de l'état de l'objet pour fonctionner.