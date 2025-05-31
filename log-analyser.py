#!/usr/bin/env python3
"""
Log Analyzer CLI - Version Dev
Analyse les fichiers de logs et génère des statistiques avec interface colorée
"""

import os
import re
from collections import Counter
from datetime import datetime

class Colors:
    """Classe pour les couleurs ANSI"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

class LogAnalyzer:
    def __init__(self, log_file="log.txt"):
        self.log_file = log_file
        self.stats = {
            'ERROR': 0,
            'WARNING': 0,
            'INFO': 0,
            'DEBUG': 0,
            'total_lines': 0
        }
        self.error_messages = []
        self.warning_messages = []
    
    def log_message(self, message, level="INFO"):
        """Affiche un message coloré selon le niveau"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        if level == "ERROR":
            print(f"{Colors.RED}[{timestamp}] ❌ {message}{Colors.END}")
        elif level == "WARNING":
            print(f"{Colors.YELLOW}[{timestamp}] ⚠️  {message}{Colors.END}")
        elif level == "SUCCESS":
            print(f"{Colors.GREEN}[{timestamp}] ✅ {message}{Colors.END}")
        elif level == "INFO":
            print(f"{Colors.CYAN}[{timestamp}] ℹ️  {message}{Colors.END}")
        else:
            print(f"[{timestamp}] {message}")
    
    def create_sample_log(self):
        """Crée un fichier log.txt d'exemple si il n'existe pas"""
        if not os.path.exists(self.log_file):
            sample_logs = [
                "2025-05-31 10:15:32 INFO - Application démarrée avec succès",
                "2025-05-31 10:16:01 INFO - Connexion utilisateur: admin",
                "2025-05-31 10:16:30 DEBUG - Chargement de la configuration",
                "2025-05-31 10:17:15 WARNING - Tentative de connexion échouée pour user123",
                "2025-05-31 10:18:22 ERROR - Impossible de se connecter à la base de données",
                "2025-05-31 10:19:45 INFO - Sauvegarde automatique effectuée",
                "2025-05-31 10:20:10 WARNING - Espace disque faible (85% utilisé)",
                "2025-05-31 10:21:33 ERROR - Timeout lors de l'appel API externe",
                "2025-05-31 10:22:18 INFO - Traitement du fichier données.csv terminé",
                "2025-05-31 10:22:45 DEBUG - Nettoyage du cache temporaire",
                "2025-05-31 10:23:47 ERROR - Erreur de validation des données utilisateur",
                "2025-05-31 10:24:56 WARNING - Cache Redis non disponible, utilisation du cache local",
                "2025-05-31 10:25:30 DEBUG - Fin du processus de nettoyage"
            ]
            
            with open(self.log_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(sample_logs))
            self.log_message(f"Fichier {self.log_file} créé avec des données d'exemple", "SUCCESS")
    
    def analyze_logs(self):
        """Analyse le fichier de logs et compte les différents niveaux"""
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            self.stats['total_lines'] = len(lines)
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if 'ERROR' in line:
                    self.stats['ERROR'] += 1
                    self.error_messages.append(f"Ligne {line_num}: {line}")
                elif 'WARNING' in line:
                    self.stats['WARNING'] += 1
                    self.warning_messages.append(f"Ligne {line_num}: {line}")
                elif 'INFO' in line:
                    self.stats['INFO'] += 1
                elif 'DEBUG' in line:
                    self.stats['DEBUG'] += 1
            
            self.log_message(f"Analyse terminée: {self.stats['total_lines']} lignes traitées", "SUCCESS")
            return True
            
        except FileNotFoundError:
            self.log_message(f"Le fichier {self.log_file} n'existe pas", "ERROR")
            return False
        except Exception as e:
            self.log_message(f"Erreur lors de l'analyse: {e}", "ERROR")
            return False
    
    def generate_report(self, report_file="rapport.txt"):
        """Génère un rapport détaillé des statistiques"""
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write("=== RAPPORT D'ANALYSE DES LOGS - VERSION DEV ===\n")
                f.write(f"Généré le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Fichier analysé: {self.log_file}\n\n")
                
                f.write("STATISTIQUES GÉNÉRALES:\n")
                f.write(f"- Total de lignes: {self.stats['total_lines']}\n")
                f.write(f"- Erreurs (ERROR): {self.stats['ERROR']}\n")
                f.write(f"- Avertissements (WARNING): {self.stats['WARNING']}\n")
                f.write(f"- Informations (INFO): {self.stats['INFO']}\n")
                f.write(f"- Debug (DEBUG): {self.stats['DEBUG']}\n\n")
                
                # Calcul des pourcentages
                total_log_entries = sum([self.stats[level] for level in ['ERROR', 'WARNING', 'INFO', 'DEBUG']])
                if total_log_entries > 0:
                    f.write("RÉPARTITION EN POURCENTAGES:\n")
                    for level in ['ERROR', 'WARNING', 'INFO', 'DEBUG']:
                        percentage = (self.stats[level]/total_log_entries)*100
                        f.write(f"- {level}: {percentage:.1f}%\n")
                    f.write("\n")
                
                # Détail des erreurs
                if self.error_messages:
                    f.write("DÉTAIL DES ERREURS:\n")
                    for error in self.error_messages:
                        f.write(f"  {error}\n")
                    f.write("\n")
                
                # Détail des avertissements
                if self.warning_messages:
                    f.write("DÉTAIL DES AVERTISSEMENTS:\n")
                    for warning in self.warning_messages:
                        f.write(f"  {warning}\n")
                
                # Analyse de santé
                f.write("\nANALYSE DE SANTÉ:\n")
                error_rate = (self.stats['ERROR'] / total_log_entries * 100) if total_log_entries > 0 else 0
                if error_rate > 20:
                    f.write("🔴 CRITIQUE: Taux d'erreur élevé (>20%)\n")
                elif error_rate > 10:
                    f.write("🟡 ATTENTION: Taux d'erreur modéré (>10%)\n")
                else:
                    f.write("🟢 BON: Taux d'erreur acceptable (<10%)\n")
            
            self.log_message(f"Rapport généré: {report_file}", "SUCCESS")
            return True
            
        except Exception as e:
            self.log_message(f"Erreur lors de la génération du rapport: {e}", "ERROR")
            return False
    
    def display_summary(self):
        """Affiche un résumé coloré dans la console"""
        print(f"\n{Colors.BOLD}{Colors.PURPLE}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.PURPLE}           RÉSUMÉ D'ANALYSE - VERSION DEV{Colors.END}")
        print(f"{Colors.BOLD}{Colors.PURPLE}{'='*60}{Colors.END}")
        
        print(f"{Colors.CYAN}Fichier analysé: {Colors.WHITE}{self.log_file}{Colors.END}")
        print(f"{Colors.CYAN}Total lignes: {Colors.WHITE}{self.stats['total_lines']}{Colors.END}")
        
        # Affichage coloré des statistiques
        print(f"{Colors.RED}ERROR: {self.stats['ERROR']}{Colors.END}")
        print(f"{Colors.YELLOW}WARNING: {self.stats['WARNING']}{Colors.END}")
        print(f"{Colors.GREEN}INFO: {self.stats['INFO']}{Colors.END}")
        print(f"{Colors.BLUE}DEBUG: {self.stats['DEBUG']}{Colors.END}")
        
        # Indicateur de santé
        total_logs = sum([self.stats[level] for level in ['ERROR', 'WARNING', 'INFO', 'DEBUG']])
        if total_logs > 0:
            error_rate = (self.stats['ERROR'] / total_logs * 100)
            print(f"\n{Colors.BOLD}Taux d'erreur: {error_rate:.1f}%{Colors.END}")
            
            if error_rate > 20:
                print(f"{Colors.RED}🔴 État: CRITIQUE{Colors.END}")
            elif error_rate > 10:
                print(f"{Colors.YELLOW}🟡 État: ATTENTION{Colors.END}")
            else:
                print(f"{Colors.GREEN}🟢 État: BON{Colors.END}")
        
        print(f"{Colors.BOLD}{Colors.PURPLE}{'='*60}{Colors.END}")

def main():
    """Fonction principale"""
    print(f"{Colors.BOLD}{Colors.CYAN}🔍 Log Analyzer CLI - Version Dev{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}🎨 Interface colorée activée{Colors.END}")
    print(f"{Colors.PURPLE}{'-' * 50}{Colors.END}")
    
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
        
        analyzer.log_message("Analyse terminée avec succès!", "SUCCESS")
    else:
        analyzer.log_message("Échec de l'analyse", "ERROR")

if __name__ == "__main__":
    main()