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
