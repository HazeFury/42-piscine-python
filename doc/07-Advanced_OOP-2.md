# Module 07 - DataDeck : Advanced Object-Oriented Programming

Ce projet est une plongée au cœur de l'architecture logicielle avec Python. L'objectif n'est pas seulement de faire fonctionner un code, mais de concevoir un système robuste, extensible et maintenable en utilisant les principes avancés de la Programmation Orientée Objet (POO) et les Design Patterns.

---

## 🛠️ Exercice 0 : The Base Card (Classes Abstraites & Encapsulation)

**Notions abordées :**
Dans cet exercice, nous posons les fondations du jeu en créant une classe mère `Card` et une classe fille `CreatureCard`. L'outil principal utilisé est le module natif `abc` (Abstract Base Classes).

* **L'Encapsulation :** Grouper les données (nom, coût) et les comportements (méthodes) au sein d'une même entité logique.
* **Les Classes Abstraites :** Une classe abstraite est un "contrat". Elle ne peut pas être instanciée directement. Elle force toutes ses classes filles à posséder certaines méthodes grâce au décorateur `@abstractmethod`.

**💡 Think About : Pourquoi `Card` doit-elle être une classe abstraite plutôt qu'une classe normale ?**
> Si `Card` était une classe normale, un développeur pourrait instancier une "Carte" générique qui n'est ni un sort, ni une créature, ce qui n'a aucun sens dans les règles du jeu. De plus, rendre la méthode `play()` abstraite garantit (contrat strict) que n'importe quelle carte future développée pour le jeu possédera obligatoirement cette méthode, évitant ainsi des crashs imprévus lors de l'exécution.

**Exemple de syntaxe (Héritage) :**
```python
from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def play(self):
        pass
```

---

## 🃏 Exercice 1 : The Deck Builder (Polymorphisme)

**Notions abordées :**
Création des classes `SpellCard` et `ArtifactCard`, puis intégration dans un objet `Deck`. L'objectif est de manipuler des listes d'objets hétérogènes.

* **Le Polymorphisme :** C'est la capacité d'interagir avec des objets de classes différentes en utilisant exactement la même interface.
* **L'Introspection (Défensive) :** Utilisation de la fonction native `getattr(objet, "attribut", defaut)` pour vérifier dynamiquement si un objet possède une caractéristique sans faire planter le programme s'il ne l'a pas.

**💡 Think About : Comment le polymorphisme permet-il au Deck de fonctionner avec n'importe quel type de carte ?**
> Le Deck ne gère pas des "Sorts" ou des "Créatures", il gère uniquement des "Cards". Puisque toutes les cartes héritent de la classe abstraite `Card`, le Deck a la garantie absolue qu'elles possèdent toutes un attribut `cost` et une méthode `play()`. On peut donc boucler sur le Deck et appeler `card.play()` sans jamais se soucier du type concret de la carte piochée.

---

## ⚔️ Exercice 2 : The Ability System (Héritage Multiple & Interfaces)

**Notions abordées :**
Introduction de la carte hybride `EliteCard` qui hérite à la fois de `Card`, `Combatable`, et `Magical`.

* **Les Interfaces :** En Python, on simule les interfaces avec des classes abstraites vides (sans constructeur `__init__`, contenant uniquement des méthodes abstraites). Elles représentent une "capacité" (ex: la capacité de se battre).
* **L'Héritage Multiple :** Python autorise une classe à avoir plusieurs parents. Le MRO (Method Resolution Order) lit les parents de la gauche vers la droite pour résoudre les conflits potentiels.

**💡 Think About : Quels sont les avantages d'utiliser de multiples interfaces plutôt qu'une seule énorme classe mère ?**
> C'est le principe de "Ségrégation des Interfaces" (le 'I' de S.O.L.I.D). Si nous avions mis les méthodes `attack()` et `cast_spell()` directement dans la classe mère `Card`, un simple `Mana Crystal` (Artefact) aurait hérité d'une méthode d'attaque qui lui est totalement inutile. En séparant les capacités en petites interfaces (`Combatable`, `Magical`), on construit nos objets comme des Lego, en ne leur donnant que les capacités dont ils ont réellement besoin.

---

## 🧠 Exercice 3 : The Game Engine (Design Patterns & Injection de Dépendances)

**Notions abordées :**
Création du cerveau du jeu (`GameEngine`) en le rendant totalement indépendant de la création des cartes et de la logique de jeu.

* **Abstract Factory Pattern :** Déléguer l'instanciation des objets complexes à une classe "Usine" (`FantasyCardFactory`). Le moteur demande des cartes à l'usine sans connaître leurs statistiques exactes.
* **Strategy Pattern :** Encapsuler l'algorithme de prise de décision (IA) dans une classe dédiée (`AggressiveStrategy`).
* **Dependency Injection :** Le moteur ne crée pas lui-même son usine et son IA. On les lui "injecte" depuis l'extérieur (`main.py`) via la méthode `configure_engine()`.

**💡 Think About : Comment les patterns Factory et Strategy rendent-ils le GameEngine plus flexible ?**
> Le `GameEngine` est devenu "aveugle". Il sous-traite la fabrication à la Factory et la réflexion à la Strategy. Grâce à ce découplage, on peut totalement changer le thème du jeu (créer une `SciFiFactory`) ou l'intelligence de l'adversaire (créer une `DefensiveStrategy`) sans avoir à modifier une seule ligne du code interne du `GameEngine`. Le code est modulaire et facilement testable.

---

## 🏆 Exercice 4 : The Tournament Platform (Composition Avancée)

**Notions abordées :**
Mise en place d'une plateforme d'e-sport compétitive pour faire s'affronter les cartes et générer un classement (Leaderboard).

* **Composition d'Interfaces Avancée :** La classe `TournamentCard` est le test ultime. Elle combine les fondations du jeu (`Card`), les mécaniques de l'Exercice 2 (`Combatable`), et le nouveau système de score (`Rankable`).
* **Tri d'Objets par Attribut :** Utilisation des fonctions `lambda` anonymes pour trier des listes d'objets complexes.

**💡 Think About : Comment l'interface `Rankable` permet-elle à la plateforme de trier les cartes sans connaître leurs types spécifiques ?**
> La plateforme se fiche de savoir si la carte attaque avec une épée ou lance des boules de feu. Tout ce qui l'intéresse, c'est que la carte a signé le contrat `Rankable`. Ce contrat garantit la présence de la méthode `calculate_rating()`. La plateforme utilise simplement cette méthode comme clé de tri universelle pour établir son classement.

**Exemple de syntaxe (Tri avec Lambda) :**

```python
def get_leaderboard(self):
    # On trie la liste en se basant uniquement sur l'attribut rating de chaque objet 'c'
    return sorted(self.cards_list, key=lambda c: c.rating, reverse=True)
```