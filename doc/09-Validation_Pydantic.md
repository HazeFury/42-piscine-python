# 🌌 Module 09 : Cosmic Data - L'art de la Validation avec Pydantic

L'objectif principal était de maîtriser **Pydantic (v2)**, la bibliothèque de référence en Python pour le parsing et la validation stricte de données .

## 🧠 Le Concept Clé : Parsing vs Validation

Pydantic agit comme un "sas de sécurité". Sa philosophie par défaut est tolérante en entrée mais stricte en sortie :
* **Parsing :** Si Pydantic attend un entier (`int`) et reçoit la chaîne `"42"`, il va silencieusement la convertir en `42`. Idem pour une chaîne de date ISO qu'il transforme en objet `datetime`.
* **Validation :** Il ne lève une erreur (`ValidationError`) que s'il est techniquement impossible de convertir la donnée, ou si elle enfreint une règle mathématique ou métier qu'on lui a définie.

---

## 🛰️ Exercice 0 : Les Fondations (Space Station)

**Objectif :** Créer un modèle basique avec des contraintes sur chaque variable.

**Les outils :**
* `BaseModel` : La classe mère dont tous nos modèles doivent hériter.
* `Field(...)` : Permet d'ajouter des règles spécifiques (min, max, taille) sur un champ isolé .

**Exemple d'implémentation :**
```python
from pydantic import BaseModel, Field

class SpaceStation(BaseModel):
	# Contrainte de longueur de texte
	name: str = Field(min_length=1, max_length=50)
	# Contrainte mathématique (Greater/Less or Equal)
	crew_size: int = Field(ge=1, le=20)
	# Valeur par défaut
	is_operational: bool = Field(default=True)
```

---

## 👽 Exercice 1 : La Logique Métier (Alien Contact Logs)

**Objectif :** Verrouiller les choix possibles et créer des règles croisées (qui impliquent plusieurs variables en même temps).

**Les outils :**
* `Enum` : Pour créer une liste stricte de choix autorisés (ex: radio, visual, physical, telepathic).
* `@model_validator(mode='after')` : Un décorateur de Pydantic v2 (remplaçant l'ancien `@validator`) qui permet d'exécuter du code Python *après* que les champs basiques ont été validés.

**Exemple d'implémentation :**

```python
from enum import Enum
from pydantic import BaseModel, model_validator

class ContactType(str, Enum):
	RADIO = "radio"
	TELEPATHIC = "telepathic"

class AlienContact(BaseModel):
	contact_type: ContactType
	witness_count: int

	@model_validator(mode='after')
	def check_rules(self) -> 'AlienContact':
		# Si c'est télépathique, il faut au moins 3 témoins
		if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
			raise ValueError("Telepathic contact requires at least 3 witnesses")
			
		# Ne jamais oublier de retourner l'objet !
		return self
```

---

## 🚀 Exercice 2 : Les Modèles Imbriqués (Space Crew Management)

**Objectif :** Maîtriser les relations complexes et l'architecture en arbre (Nested Models).

**Le fonctionnement :** Pydantic gère la validation de manière récursive. Si on intègre une liste d'objets `CrewMember` à l'intérieur d'un modèle parent `SpaceMission`, Pydantic validera d'abord chaque membre un par un de manière isolée . Si un seul membre échoue à sa propre validation, c'est la mission spatiale toute entière qui est rejetée et lève une erreur.

**Exemple d'implémentation :**

```python
from typing import List
from pydantic import BaseModel

class CrewMember(BaseModel):
	name: str
	age: int

class SpaceMission(BaseModel):
	mission_name: str
	# Imbrication : Une liste contenant nos modèles enfants
	crew: List[CrewMember]
```

---

## 💡 Astuces de Survie (Spécial 42)

1. **Le conflit avec mypy :** Pydantic utilise une architecture complexe que `mypy` en mode strict a du mal à lire. Pour passer l'évaluation du linter, il faut parfois utiliser `# type: ignore` sur l'héritage `(BaseModel)` et sur le décorateur `@model_validator`.
2. **Le formatage de l'output :** Toujours extraire les messages d'erreurs proprement via `e.errors()` dans un bloc `except ValidationError as e:` pour éviter d'afficher la trace complète illisible et coller aux attentes du sujet.
3. **Le Forward Reference :** Quand on type le retour de la fonction `@model_validator`, la classe n'est pas encore totalement créée. Il faut donc écrire le type entre guillemets (ex: `-> 'SpaceMission'`).