# 💊 Module 08 : Initiation à l'Ingénierie de la Donnée et Environnements Python

Ce module apprend à isoler mes projets, gérer les dépendances et sécuriser les secrets. Ce sont des compétences fondamentales pour ne pas polluer son système ou faire fuiter des mots de passe sur GitHub.

## 🏗️ Exercice 00 : L'Environnement Virtuel (La Matrice)

**Le Concept :**
Un environnement virtuel (venv) est une bulle hermétique. Au lieu d'installer des paquets Python sur l'ensemble du système global de la machine (ce qui crée des conflits de versions entre les différents projets), on crée un dossier contenant son propre exécutable Python et son propre espace de stockage pour les bibliothèques.

**Les modules internes explorés :**

* sys : Le tableau de bord de l'interpréteur Python. `sys.prefix` permet de voir où Python s'exécute. `sys.executable` donne le chemin exact du binaire Python.
* os : Le pont avec le système d'exploitation. `os.environ` permet de lire les variables du terminal (comme `VIRTUAL_ENV`).
* site : L'inspecteur qui gère les chemins des dossiers `site-packages` (où sont installées les dépendances tierces).

**Commandes clés :**
```bash
# Créer l'environnement :
	python3 -m venv matrix_env

# Activer l'environnement :
	source matrix_env/bin/activate

# Désactiver l'environnement :
	deactivate
```

---

## 📦 Exercice 01 : Gestion des Dépendances (pip vs Poetry)

**Le Concept :**
Une fois dans notre bulle, on a besoin d'outils externes (pandas, numpy, matplotlib, etc.). Cet exercice a montré comment installer et tracer ces dépendances de manière reproductible pour que n'importe quel autre développeur puisse cloner et lancer le projet.

**1. L'approche Classique (pip) :**
Utilise un simple fichier texte (`requirements.txt`). C'est l'approche historique, simple et déclarative.
```bash
# Installer via pip :
	pip install -r requirements.txt

# Nettoyer un environnement pollué :
	pip uninstall -y -r requirements.txt
```

**2. L'approche Moderne (Poetry) :**
Utilise un fichier `pyproject.toml`. Poetry gère intelligemment les sous-dépendances et crée son propre environnement virtuel automatiquement. 
*(Note : l'option `package-mode = false` a été ajoutée car notre projet est un simple script, pas une bibliothèque vouée à être publiée).*
```bash
# Installer via Poetry :
	poetry install

# Exécuter un script via Poetry :
	poetry run python loading.py
```

**L'import défensif (Graceful Handling) :**
Il faut toujours anticiper le fait qu'une bibliothèque puisse manquer sur la machine de l'utilisateur. Au lieu de laisser le programme crasher, on gère l'erreur proprement :

```python
	try:
		import pandas as pd
	except ImportError:
		print("Erreur : pandas est manquant. Veuillez l'installer.")
		sys.exit(1)
```

---

## 🔐 Exercice 02 : Sécurité et Variables d'Environnement

**Le Concept :**
Ne **jamais** écrire de mots de passe, clés d'API ou configurations sensibles en dur dans le code source. On utilise le système des variables d'environnement.

**Le fonctionnement (.env) :**
1.  On crée un fichier `.env` contenant nos secrets locaux.
2.  On ajoute **immédiatement** la ligne `.env` dans notre `.gitignore` à la racine du projet.
3.  On crée un fichier `env.example` (avec de fausses données du type `API_KEY=YOUR_KEY_HERE`) qu'on push sur GitHub pour montrer la structure attendue aux autres développeurs.
4.  Dans le code, on utilise la bibliothèque `python-dotenv` pour charger ces variables.

**La règle d'or de l'Override (Surcharge) :**
Si une variable existe déjà dans le terminal de l'ordinateur, elle gagne **toujours** sur celle écrite dans le fichier `.env`. C'est vital pour le déploiement en production, où le serveur injectera ses propres variables sans utiliser de fichier local.

**Exemple d'override en ligne de commande :**
```bash
MATRIX_MODE=production ZION_ENDPOINT=http://zion.local python3 oracle.py
```