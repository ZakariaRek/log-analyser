import os
import re
from collections import Counter
from datetime import datetime
import sys

# Add this at the top of your file to ensure proper Unicode handling
if sys.platform == 'win32':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleOutputCP(65001)  # Set console to UTF-8 mode

class LogAnalyzer:
    def __init__(self, log_file="log.txt"):
        self.log_file = log_file
        self.stats = {
            'ERROR': 0,
            'WARNING': 0,
            'INFO': 0,
            'total_lines': 0
        }
    
    def create_sample_log(self):
        """Crée un fichier log.txt d'exemple si il n'existe pas"""
        if not os.path.exists(self.log_file):
            sample_logs = [
                "2025-05-31 10:15:32 INFO - Application démarrée avec succès",
                "2025-05-31 10:16:01 INFO - Connexion utilisateur: admin",
                "2025-05-31 10:17:15 WARNING - Tentative de connexion échouée pour user123",
                "2025-05-31 10:18:22 ERROR - Impossible de se connecter à la base de données",
                "2025-05-31 10:19:45 INFO - Sauvegarde automatique effectuée",
                "2025-05-31 10:20:10 WARNING - Espace disque faible (85% utilisé)",
                "2025-05-31 10:21:33 ERROR - Timeout lors de l'appel API externe",
                "2025-05-31 10:22:18 INFO - Traitement du fichier données.csv terminé",
                "2025-05-31 10:23:47 ERROR - Erreur de validation des données utilisateur",
                "2025-05-31 10:24:56 WARNING - Cache Redis non disponible, utilisation du cache local"
            ]
            
            with open(self.log_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(sample_logs))
            print(f"✓ Fichier {self.log_file} créé avec des données d'exemple")
    
    def analyze_logs(self):
        """Analyse le fichier de logs et compte les différents niveaux"""
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            self.stats['total_lines'] = len(lines)
            
            for line in lines:
                line = line.strip()
                if 'ERROR' in line:
                    self.stats['ERROR'] += 1
                elif 'WARNING' in line:
                    self.stats['WARNING'] += 1
                elif 'INFO' in line:
                    self.stats['INFO'] += 1
            
            print(f"✓ Analyse terminée: {self.stats['total_lines']} lignes traitées")
            return True
            
        except FileNotFoundError:
            print(f"❌ Erreur: Le fichier {self.log_file} n'existe pas")
            return False
        except Exception as e:
            print(f"❌ Erreur lors de l'analyse: {e}")
            return False
    
    def generate_report(self, report_file="rapport.txt"):
        """Génère un rapport des statistiques"""
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write("=== RAPPORT D'ANALYSE DES LOGS ===\n")
                f.write(f"Généré le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Fichier analysé: {self.log_file}\n\n")
                
                f.write("STATISTIQUES:\n")
                f.write(f"- Total de lignes: {self.stats['total_lines']}\n")
                f.write(f"- Erreurs (ERROR): {self.stats['ERROR']}\n")
                f.write(f"- Avertissements (WARNING): {self.stats['WARNING']}\n")
                f.write(f"- Informations (INFO): {self.stats['INFO']}\n\n")
                
                # Calcul des pourcentages
                total_log_entries = self.stats['ERROR'] + self.stats['WARNING'] + self.stats['INFO']
                if total_log_entries > 0:
                    f.write("RÉPARTITION:\n")
                    f.write(f"- ERROR: {(self.stats['ERROR']/total_log_entries)*100:.1f}%\n")
                    f.write(f"- WARNING: {(self.stats['WARNING']/total_log_entries)*100:.1f}%\n")
                    f.write(f"- INFO: {(self.stats['INFO']/total_log_entries)*100:.1f}%\n")
            
            print(f"✓ Rapport généré: {report_file}")
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de la génération du rapport: {e}")
            return False
    
    def display_summary(self):
        """Affiche un résumé dans la console"""
        print("\n" + "="*50)
        print("           RÉSUMÉ D'ANALYSE")
        print("="*50)
        print(f"Fichier analysé: {self.log_file}")
        print(f"Total lignes: {self.stats['total_lines']}")
        print(f"ERROR: {self.stats['ERROR']}")
        print(f"WARNING: {self.stats['WARNING']}")
        print(f"INFO: {self.stats['INFO']}")
        print("="*50)

def main():
    """Fonction principale"""
    print("🔍 Log Analyzer CLI - Démarrage de l'analyse")
    print("-" * 40)
    
    # Initialisation de l'analyseur
    analyzer = LogAnalyzer()
    
    # Création du fichier d'exemple si nécessaire
    analyzer.create_sample_log()
    
    # Analyse des logs
    if analyzer.analyze_logs():
        # Génération du rapport
        analyzer.generate_report()
        
        # Affichage du résumé
        analyzer.display_summary()
        
        print("\n✅ Analyse terminée avec succès!")
    else:
        print("\n❌ Échec de l'analyse")

if __name__ == "__main__":
    main()