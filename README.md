# Log Analyzer CLI

**Auteur**: Rekhla Zakaria  
**Version**: 1.0.0  
**Date**: Mai 2025

## Description

Log Analyzer CLI est un outil en ligne de commande développé en Python qui permet d'analyser des fichiers de logs et de générer des statistiques détaillées. L'application compte automatiquement les occurrences des différents niveaux de logs (ERROR, WARNING, INFO) et produit un rapport complet.

## Fonctionnalités

- ✅ Lecture et analyse de fichiers de logs
- ✅ Comptage automatique des niveaux ERROR, WARNING, INFO
- ✅ Génération d'un rapport détaillé (`rapport.txt`)
- ✅ Création automatique d'un fichier de logs d'exemple
- ✅ Affichage des statistiques dans la console
- ✅ Calcul des pourcentages de répartition

## Prérequis

- Python 3.6 ou supérieur
- Aucune dépendance externe requise (utilise uniquement la bibliothèque standard Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/[votre-username]/log-analyzer.git
cd log-analyzer
```

2. Le script est prêt à être utilisé sans installation supplémentaire.

## Utilisation

### Utilisation basique

```bash
python log_analyzer.py
```

### Avec un fichier de logs personnalisé

Le script recherche par défaut un fichier `log.txt` dans le répertoire courant. Si ce fichier n'existe pas, il en crée un automatiquement avec des données d'exemple.

### Sortie

L'application génère :
- Un rapport détaillé dans `rapport.txt`
- Un résumé affiché dans la console
- Des statistiques complètes avec pourcentages

## Structure du projet

```
log-analyzer/
├── log_analyzer.py      # Script principal
├── README.md           # Documentation
├── log.txt            # Fichier de logs (généré automatiquement)
└── rapport.txt        # Rapport généré (créé après exécution)
```

## Exemple de sortie

```
🔍 Log Analyzer CLI - Démarrage de l'analyse
----------------------------------------
✓ Fichier log.txt créé avec des données d'exemple
✓ Analyse terminée: 10 lignes traitées
✓ Rapport généré: rapport.txt

==================================================
           RÉSUMÉ D'ANALYSE
==================================================
Fichier analysé: log.txt
Total lignes: 10
ERROR: 3
WARNING: 3
INFO: 4
==================================================

✅ Analyse terminée avec succès!
```

## Format du fichier de logs

Le script supporte les logs au format standard :
```
YYYY-MM-DD HH:MM:SS LEVEL - Message
```

Exemple :
```
2025-05-31 10:15:32 INFO - Application démarrée avec succès
2025-05-31 10:18:22 ERROR - Impossible de se connecter à la base de données
```

## Développement

### Branches

- `main` : Branch principale stable
- `dev` : Branch de développement pour les nouvelles fonctionnalités

### Contribuer

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## Licence

Ce projet est développé dans le cadre du cours Master ISI/S2 2025.

## Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub.