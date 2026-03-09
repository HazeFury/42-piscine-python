# Récapitulatif : Module 05 - Code Nexus (Polymorphic Data Streams)

Ce module marque la transition entre le code procédural et l'architecture logicielle d'entreprise (Data Engineering, pipelines ETL). L'objectif global était de concevoir des systèmes capables d'ingérer et de traiter des flux de données hétérogènes de manière robuste et évolutive.

---

## 1. L'Héritage et la délégation avec super()

**Notion :** L'héritage permet à une classe enfant (Child) de récupérer tous les attributs et méthodes d'une classe mère (Parent). La fonction super() permet d'appeler explicitement une méthode de la classe mère depuis l'enfant.

**Justification :** Éviter la duplication de code (principe DRY : Don't Repeat Yourself). On centralise la logique commune dans le parent (comme l'initialisation d'un ID ou d'un compteur) et l'enfant se contente de gérer ses propres spécificités.

**Exemple :**
```python
class DataStream:
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_count = 0

class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        # Délégation au parent pour gérer l'ID et le compteur
        super().__init__(stream_id)
        self.temp_total = 0.0
```

---

## 2. La Surcharge de Méthodes (Method Overriding)

**Notion :** C'est le fait de redéfinir dans une classe enfant une méthode qui existe déjà dans la classe mère, en gardant exactement la même signature (mêmes paramètres, même type de retour).

**Justification :** C'est la mécanique qui permet la spécialisation. Le parent dit "Je sais traiter une donnée", et l'enfant surcharge la méthode pour dire "Moi, je sais traiter spécifiquement une donnée de type JSON".

---

## 3. Le Polymorphisme (Subtype Polymorphism)

**Notion :** "Poly" (plusieurs) + "Morph" (formes). C'est la capacité d'un système à traiter des objets de classes différentes de la même manière, tant qu'ils partagent la même interface (le même nom de méthode). La devise du module : Même interface, comportement différent.

**Justification :** Rendre le code infiniment évolutif (Scalability). Au lieu de faire d'immenses chaînes de if / elif pour vérifier le type d'une donnée, on boucle sur des objets et on appelle aveuglément leur méthode de traitement. Si on ajoute un nouveau type de capteur demain, on n'a pas besoin de modifier la boucle principale.

**Exemple :**

    # Polymorphisme en action : la boucle ignore la classe exacte des objets
    for stream in streams_list:
        # stream peut être un SensorStream, EventStream, etc.
        stream.process_batch(data)

---

## 4. Les Classes Abstraites (ABC) et les Contrats

**Notion :** Une Abstract Base Class (ABC) est une classe fantôme qui ne peut pas être instanciée. Couplée au décorateur @abstractmethod, elle sert de moule strict.

**Justification :** Sécuriser l'architecture. Une méthode abstraite crée un contrat inviolable : toute classe enfant DOIT obligatoirement recoder cette méthode, sinon le programme refuse de se lancer. C'est la garantie que le polymorphisme fonctionnera sans crasher.

---

## 5. Le "Duck Typing" et le module Protocol

**Notion :** "Si ça marche comme un canard et que ça cancane comme un canard, c'est un canard". Avec la classe Protocol, on crée une interface basée sur le comportement, pas sur la généalogie. L'objet n'a pas besoin d'hériter de quoi que ce soit.

**Justification :** Le couplage ultra-faible. Cela permet d'intégrer des classes totalement indépendantes (voire des librairies externes) dans notre système, à la seule condition qu'elles possèdent la méthode requise (comme la méthode process dans l'exercice 2).

**Exemple :**
```python
from typing import Protocol, Any

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...
```

---

## 6. Composition vs Héritage

**Notion :** 
- L'Héritage définit une relation "EST UN" (Un SensorStream EST UN DataStream).
- La Composition définit une relation "A UN" (Le NexusManager A DES ProcessingPipelines).

**Justification :** La règle d'or de l'architecture est de préférer la composition à l'héritage. Elle permet d'assembler des "briques Lego" indépendantes. Un manager qui contient une liste de pipelines peut facilement ajouter ou retirer des pipelines à la volée, ce qui rend le système beaucoup plus dynamique et modulaire qu'une hiérarchie d'héritage rigide.

---

## 7. Typage Avancé et "Type Guards" (MyPy)

**Notion :** L'utilisation intensive du module typing (Any, List, Dict, Union, Optional) pour documenter et sécuriser les flux de données. Un "Type Guard" est une vérification logique (comme isinstance) qui prouve au linter (comme MyPy) que le type d'une variable a changé.

**Justification :** En Data Engineering, on manipule souvent de la donnée brute inconnue (Any). Le typage strict couplé aux Type Guards empêche les erreurs de manipulation et rend le code auto-documenté. 

**Exemple :**

```python
def process(self, data: Any) -> dict:
    # TYPE GUARD : Transforme le 'Any' en 'dict' pour la suite du code
    if not isinstance(data, dict):
        raise TypeError("Expected a dictionary")
        
    data["status"] = "processed"
    return data
```
