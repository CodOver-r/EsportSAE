from BDesport import execute,selectEquipe,selectJoueur,selectCompetition,selectMatchGame,selectClassement
from configBD import dbConnect
import csv

db,cursor= dbConnect()

def loadFromCSV(path : str):
    """ fonction de chargement des données dans la base de données  """
    try : 
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if row[0] == "Equipe":
                    execute(""" INSERT INTO Equipe (NumEquipe, nomEquipe, NbJoueur, Logo) VALUES ({}, '{}', {}, '{}') """.format(row[1],row[2],row[3],row[4]))
                elif row[0] == "Joueur":
                    execute(""" INSERT INTO Joueur (NumJoueur, NumEquipe, Pseudo, DateNaissance, Email) VALUES ({}, {}, '{}', '{}', '{}') """.format(row[1],row[2],row[3],row[4],row[5]))
                elif row[0] == "Competition":
                    execute(""" INSERT INTO Competition (NumCompetition, nomCompetition, DateDebut, DateFin, Web, Lieu, Prix, Jeu) VALUES ({}, '{}', '{}', '{}', '{}', '{}', {}, '{}') """.format(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
                elif row[0] == "Match":
                    execute(""" INSERT INTO MatchGame (NumMatch, NumCompetition, NumEquipe1, NumEquipe2, ScoreEquipe1, ScoreEquipe2, Duree) VALUES ({}, {}, {}, {}, {}, {}, '{}') """.format(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
                elif row[0] == "Classement":
                    execute(""" INSERT INTO Classement (NumClassement, NumCompetition, NumEquipe, Position, Score, Gain) VALUES ({}, {}, {}, "{}", "{}", '{}') """.format(row[1],row[2],row[3],row[4],row[5],row[6]))
    except FileNotFoundError :
        print("Fichier non trouvé")

    except Exception as e :
        print("Erreur !",e)

    print("Données chargées")
            
def saveToCSV(path : str):
    """ fonction de sauvegarde des données dans un fichier csv """
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["_Equipe","NumEquipe", "Nom", "Nombre de joueur", "Logo"])
        for row in selectEquipe():
            row = rowCSV("Equipe", row)
            writer.writerow(row)
        writer.writerow(["_Joueur","NumJoueur", "Numéro d'équipe", "Pseudo", "Date de naissance", "Email"])
        for row in selectJoueur():
            row = rowCSV("Joueur", row)
            writer.writerow(row)
        writer.writerow(["_Competition","NumCompetition ", "Nom", "Date de début", "Date de fin", "Web", "Lieu", "Prix", "Jeu"])
        for row in selectCompetition():
            row = rowCSV("Competition", row)
            writer.writerow(row)
        writer.writerow(["_Match","NumMatch", "Numéro de compétition", "Numéro d'équipe 1", "Numéro d'équipe 2", "Score équipe 1", "Score équipe 2", "Durée"])
        for row in selectMatchGame():
            row = rowCSV("Match", row)
            writer.writerow(row)
        writer.writerow(["_Classement","NumClassement", "Numéro de compétition", "Numéro d'équipe", "Position", "Score", "Gain"])
        for row in selectClassement():
            row = rowCSV("Classement", row)
            writer.writerow(row)

def rowCSV(table : str, row : tuple) :
    """ Fonction d'ajout d'un mot clé dans le fichier csv """
    table = tuple(table.split(","))
    row = table + row
    return row  

def createDB() :
    try : 
        print("Création de la base de données")
        cursor.execute("CREATE DATABASE DBesport")
        print("Base de données créée")
        cursor.execute("USE DBesport")
        print("Base de données sélectionnée")
        cursor.execute("""CREATE TABLE Equipe (
        `numEquipe` int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `nomEquipe` varchar(64) NOT NULL,
        `nbJoueur` int(10) NOT NULL,
        `Logo` varchar(255) NOT NULL)""")

        print("Table Equipe créée")

        cursor.execute("""CREATE TABLE Joueur (
        `numJoueur` int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `numEquipe` int(10) NOT NULL,
        `pseudo` varchar(64) NOT NULL,
        `DateNaissance` date NOT NULL,
        `Email` varchar(64) NOT NULL)""")

        print("Table Joueur créée")

        cursor.execute( """CREATE TABLE MatchGame (
        `numMatch` int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `numCompetition` int(10) NOT NULL,
        `numEquipe1` int(10) NOT NULL,
        `numEquipe2` int(10) NOT NULL,
        `ScoreEquipe1` int(8) NOT NULL,
        `ScoreEquipe2` int(8) NOT NULL,
        `Duree` time NOT NULL)""")

        print("Table MatchGame créée")

        cursor.execute("""CREATE TABLE  Competition (
        `numCompetition` int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `nomCompetition` varchar(64) NOT NULL,
        `dateDebut` date NOT NULL,
        `dateFin` date NOT NULL,
        `Web` varchar(255) NOT NULL,
        `Lieu` varchar(64) NOT NULL,
        `Prix` int(10) NOT NULL,
        `Jeu` varchar(64) NOT NULL)""")

        print("Table Competition créée")

        cursor.execute("""CREATE TABLE Classement (
        `numClassement` int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `numCompetition` int(10) NOT NULL ,
        `numEquipe` int(10) NOT NULL ,
        `Position` varchar(64) NOT NULL,
        `Score` varchar(64) NOT NULL,
        `Gain` int(10) NOT NULL)""")

        execute("ALTER TABLE `Classement` ADD INDEX(`numEquipe`);")
        execute("ALTER TABLE `Classement` ADD INDEX(`numCompetition`);")
        execute("ALTER TABLE `MatchGame` ADD INDEX(`numCompetition`);")
        execute("ALTER TABLE `MatchGame` ADD INDEX(`numEquipe1`);")
        execute("ALTER TABLE `MatchGame` ADD INDEX(`numEquipe2`);")
        
        print("Table Classement créée")
        db.close()

        print("Création de la base de données vide réussie")
    except Exception as e :
        print("Erreur lors de la création de la base de données")
        print(e)

def deleteDB() :
    """ Supprime la base de donnée """
    try :
        cursor.execute("DROP DATABASE DBesport")
        print("Base de données supprimée")
    except Exception as e :
        print("Base de données non trouvée")

def menuGestionDB():

    """ fonction de gestion de la base de données """

    print("------------------------------------------------")
    print("Gestion de la base de données")
    print("------------------------------------------------")
    print("1 - Créer la base de données")
    print("2 - Supprimer la base de données")
    print("3 - Charger les données depuis un fichier ")
    print("4 - Sauvegarder les données dans un fichier csv")
    print("5 - Remise à zéro de la base de données")
    print("6 - Quitter")
    print("------------------------------------------------")
    choix = int(input("Choix : "))
    print("")
    if choix == 1:
        createDB()
        menuGestionDB()
    elif choix == 2:
        deleteDB()
        menuGestionDB()
    elif choix == 3:
        loadFromCSV(input("Nom du fichier : "))
        menuGestionDB()
    elif choix == 4:
        saveToCSV(input("Nom du fichier csv : ")+".csv")
        menuGestionDB()
    elif choix == 5:
        deleteDB()
        createDB()
        menuGestionDB()
    elif choix == 6:
        print("Au revoir !")
    else:
        print("Choix invalide !")
        menuGestionDB()

if __name__ == "__main__" :

    """ fonction de gestion de la base de données """
    menuGestionDB()
