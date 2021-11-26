# Script_TLCA

La plateforme TLCA permet l'importation en batch de résultats d'évaluation pour un ensemble d'étudiants. Ce mécanisme d'importation peut servir pour récupérer les résultats d'un quizz Moodle. Néanmoins, les deux plateformes utilisant des formats différents, il est nécessaire d'utiliser un script pour traduire d'un format à un autre. Vous trouverez en pièces jointes trois fichiers :

   Un fichier CSV (anonymisé) venant de Moodle contenant les résultats d'un quizz. Le quizz donne lieu à une validation de la compétence si et seulement ci l'étudiant a obtenu 75% au moins. Attention : Il y a parfois deux tentatives par étudiant, il ne faut garder que la meilleure.
    
   Un premier fichier XLSX (anonymisé également) généré par TLCA, appelé "tlca-in.xlsx", qui est partiellement rempli. Ce dernier doit être complété en indiquant :
        Une croix (x minuscule) dans la colonne Select si l'étudiant a terminé le quizz
        Si l'étudiant a obtenu plus min. 75% : une croix (x minuscule) dans la colonne correspondant à la ou les compétence(s) gagnée(s)
        La date à laquelle le quizz a été passé (chaîne de caractère au format 2020-10-29 16:00)
        Un commentaire textuel reprenant le pourcentage obtenu.
      
   Un second fichier appelé "tlca-out.xlsx" qui vous donne un exemple de fichier tlca rempli selon les consignes ci-dessus.


Le challenge est donc d'écrire un script qui prend au moins 4 paramètres sur la ligne de commande, et génère le fichier à importer dans TLCA :
Le nom du fichier CSV Moodle
Le nom du fichier XLSX TLCA vide
Le nom du fichier XLSX TLCA à remplir
Les identifiants des compétence à valider (pour choisir les bonnes colonnes du XLSX)

# Compétences 

Cette évaluation évalue les compétences suivantes :

+2DEV-202 – Ecrire un script en Python en suivant les bonnes pratiques de programmation
 Les paramètres du programme sont récupérés depuis la ligne de commande, qui possède un menu d'aide
 Les dates sont correctement gérées (format d'entrée et de sortie) à l'aide de la librairie datetime
 Le point d'entrée du script est identifié par if __name__ == "__main__", et l'étudiant peut expliquer l'utilité de cette construction
 Le script gère correctement le cas de deux étudiants avec le même nom de famille
 Le script gère correctement le cas de deux étudiants avec le même prénom
 Dans le cas où un étudiant a réussi deux fois la même épreuve, la meilleure note est retenue
 Le script gère correctement le choix de la compétence, même s'il y a plusieurs colonnes de compétences dans le fichier de sortie
 Le code est propre, aussi simplifié que possible et respecte la PEP8
 L'étudiant est capable de faire une petite modification de son script à la demande de l'enseignant lors de la défense
Vous pouvez aller plus loin pour être également évalué(e) sur les compétences suivantes :

+1DEV-241 – Réaliser une application OO sur base d'une spécification détaillée
 L'étudiant utilise des mécanismes OO dans le cadre du script
 La gestion des erreurs se fait sur base d'exceptions correctement gérées pour fournir un retour utilisateur pertinent
 
+1DEV-203 – Utiliser les fonctionnalités avancées de Python
