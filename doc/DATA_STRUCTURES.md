# 🐍 Guide Complet des Structures de Données en Python

Ce document est un aide-mémoire pour comprendre et choisir la bonne structure de données en Python.

---

## 1. Les Listes (`list`) : Le couteau suisse

C'est la structure la plus utilisée. C'est une séquence ordonnée et mutable (modifiable).

* **Équivalent JS :** Array `[]`
* **Équivalent C :** Un tableau dynamique (mais qui peut contenir des types mélangés).

**Syntaxe & Utilisation :**

```python
# Création
fruits = ["pomme", "banane", "orange"]

# Accès (L'index commence à 0)
print(fruits[0])  # pomme
print(fruits[-1]) # orange (l'index négatif part de la fin, super utile !)

# Modification
fruits.append("poire") # Ajoute à la fin (équivalent de .push() en JS)
fruits[1] = "kiwi"     # Remplace banane

# Slicing (Découpage) - Le super-pouvoir de Python
print(fruits[1:3]) # ['kiwi', 'orange'] (de l'index 1 inclus à 3 exclu)
```

**Typage (Type Hinting) :**
```python
# Liste contenant uniquement des entiers
scores: list[int] = [10, 20, 30]

# Liste hétérogène (déconseillé mais possible)
mix: list[str | int] = ["A", 1, "B", 2] 
```

**Quand l'utiliser ?**
* Quand l'ordre compte.
* Quand tu as besoin de modifier, ajouter ou supprimer des éléments.
* 👉 *C'est ton choix par défaut pour une collection d'items.*

---

## 2. Les Tuples (`tuple`) : La liste blindée

C'est une séquence ordonnée mais immuable (non modifiable). Une fois créé, on ne touche plus !

* **Équivalent JS :** N'existe pas vraiment. On pourrait dire un `Object.freeze(['a', 'b'])`, mais c'est tiré par les cheveux.
* **Équivalent C :** Un tableau `const`.

**Syntaxe & Utilisation :**

```python
# Création (ce sont les virgules qui font le tuple, les parenthèses sontoptionnelles mais recommandées)
coords = (10, 20)

# Accès
print(coords[0]) # 10

# Modification -> INTERDIT
# coords[0] = 5  # <-- Erreur : TypeError: 'tuple' object does not supportitem assignment

# Unpacking (Déballage) - Très utilisé
x, y = coords 
print(x) # 10
```

**Typage :**

```python
# Tuple de taille fixe avec types précis
user_info: tuple[str, int] = ("Marco", 30)

# Tuple de taille variable (tous du même type)
data: tuple[int, ...] = (1, 2, 3, 4, 5, 6)
```

**Quand l'utiliser ?**
* Pour des données qui ne doivent pas changer (constantes, configuration).
* Pour retourner plusieurs valeurs depuis une fonction (`return a, b`).
* 👉 *C'est plus léger en mémoire que les listes et plus rapide.*

---

## 3. Les Sets (`set`) : Le club VIP (pas de doublons)

C'est une collection non ordonnée d'éléments uniques.

* **Équivalent JS :** `Set` (introduit en ES6).
* **Maths :** Les ensembles.

**Syntaxe & Utilisation :**

```python
# Création
emails = {"a@a.com", "b@b.com", "a@a.com"} # Le doublon est automatiquement supprimé !

print(emails) # {'a@a.com', 'b@b.com'} (Attention : L'ordre n'est pas garanti)

# Opérations puissantes (Théorie des ensembles)
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b) # Intersection : {3}
print(a | b) # Union : {1, 2, 3, 4, 5}
print(a - b) # Différence : {1, 2}
```

**Typage :**

```python
unique_ids: set[int] = {101, 102, 103}
```

**Quand l'utiliser ?**
* Quand tu veux éliminer les doublons d'une liste (`list(set(ma_liste))`).
* Quand tu dois vérifier si un élément est présent très rapidement (`if x in mon_set`). 
* 👉 *C'est beaucoup plus rapide (Complexité O(1)) que de chercher dans une liste (O(n)).*

---

## 4. Les Dictionnaires (`dict`) : La base de données de poche

C'est une collection de paires **Clé: Valeur**. Depuis Python 3.7, ils gardent l'ordre d'insertion.

* **Équivalent JS :** L'Objet `{ clé: valeur }` ou `Map`.
* **Concept :** Une table de hachage (Hash Map).

**Syntaxe & Utilisation :**

```python
# Création
student = {
    "name": "Marco",
    "school": "42",
    "level": 5
}

# Accès
print(student["name"]) # "Marco"

# Modification / Ajout
student["level"] = 6
student["city"] = "Lyon" # Ajoute la clé car elle n'existe pas encore

# Itération (Boucler dessus)
for key, value in student.items():
    print(f"{key}: {value}")
```

**Typage :**

```python
# Clé en String, Valeur en Int
inventory: dict[str, int] = {"pomme": 10, "épée": 1}

# Dictionnaire complexe (équivalent d'un JSON)
data: dict[str, any] = {"id": 1, "metadata": [1, 2]}
```

**Quand l'utiliser ?**
* Quand tu dois associer des valeurs de manière sémantique (ex: ID -> Utilisateur).
* 👉 *C'est la structure reine pour manipuler des données type JSON.*

---

## 🧠 Le Guide de Choix (Cheat Sheet)

Pose-toi ces questions dans l'ordre face à un problème :

1.  **Ai-je besoin de paires Clé/Valeur ?**
    * OUI -> **Dictionnaire (`dict`)**
    * NON -> Question suivante.
2.  **L'ordre est-il important ?**
    * NON -> **Set (`set`)** (Surtout si tu veux garantir l'unicité).
    * OUI -> Question suivante.
3.  **Dois-je pouvoir modifier le contenu après création ?**
    * OUI -> **Liste (`list`)**
    * NON -> **Tuple (`tuple`)**

---

## 📊 Résumé en tableau



| Structure | Syntaxe | Ordonné ? | Mutable ? | Doublons ? | Usage Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | `[1, 2]` | ✅ Oui | ✅ Oui | ✅ Oui | Collection standard |
| **Tuple** | `(1, 2)` | ✅ Oui | ❌ Non | ✅ Oui | Données fixes / Coordonnées |
| **Set** | `{1, 2}` | ❌ Non | ✅ Oui | ❌ Non | Unicité / Opérations mathématiques |
| **Dict** | `{'a': 1}` | ✅ Oui* | ✅ Oui | ❌ Clés uniques | Association clé-valeur |

*(Oui pour l'ordre des dicts depuis Python 3.7+)*