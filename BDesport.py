from operator import eq
from unittest import result
from numpy import append
from configBD import dbConnectEsport


"----------------------------------------------------------------------------------------------------------------------"

""" Gestion de la base de donnée """

def execute(req) :
    """ Execute une requête SQL """
    db,cursor = dbConnectEsport()
    cursor.execute(req)
    db.commit()
    db.close()
    return cursor.fetchall()

"----------------------------------------------------------------------------------------------------------------------"

""" Requêtes SQL Insertion """


def insertEquipe( nomEquipe : str, nbJoueur : int, Logo : str):
    """ Insertion d'une equipe dans la base de donnée"""
    execute("""INSERT INTO Equipe (nomEquipe, nbJoueur, Logo) VALUES ("{}",{},"{}")""".format(nomEquipe,nbJoueur,Logo))

def insertJoueur(numEquipe : int , pseudo : str, dateNaissance : str, email : str):
    """ Insertion d'un joueur dans la base de donnée"""
    execute("""INSERT INTO Joueur (numEquipe, pseudo, dateNaissance, email) VALUES ({},"{}","{}","{}")""".format(numEquipe,pseudo,dateNaissance,email))

def insertMatchGame( numCompetition : int, scoreEquipe1 : int, scoreEquipe2 : int, numEquipe1 : str, numEquipe2 : str,Duree : str):
    """ Insertion d'un match dans la base de donnée"""
    execute("""INSERT INTO MatchGame (numCompetition, scoreEquipe1, scoreEquipe2, numEquipe1, numEquipe2, Duree) VALUES ("{}","{}","{}","{}","{}","{}")""".format(numCompetition,scoreEquipe1,scoreEquipe2,numEquipe1,numEquipe2,Duree))
    
def insertCompetition( nomCompetition : str, dateDebut : str, dateFin : str, Web : str, lieu : str, Prix : str , Jeu : str):
    """ Insertion d'une competition dans la base de donnée"""
    execute("""INSERT INTO Competition (nomCompetition, dateDebut, dateFin, Web, lieu, Prix, Jeu) VALUES ("{}","{}","{}","{}","{}","{}","{}")""".format(nomCompetition,dateDebut,dateFin,Web,lieu,Prix,Jeu))

def insertClassement( numCompetition : int, numEquipe : int, Position : str, Score : str, Gain : int):
    """ Insertion d'un classement dans la base de donnée"""
    execute("""INSERT INTO Classement (numCompetition, numEquipe, Position, Score, Gain) VALUES ("{}","{}","{}","{}","{}")""".format(numCompetition,numEquipe,Position,Score,Gain))

"----------------------------------------------------------------------------------------------------------------------"

""" Requêtes SQL Suppression """


def deleteEquipeByNum(numEquipe : int):
    """ Supprime une equipe de la base de donnée """
    execute("DELETE FROM Equipe WHERE numEquipe = {}".format(numEquipe))

def deleteJoueurByNum(numJoueur : int):
    """ Supprime un joueur de la base de donnée """
    execute("DELETE FROM Joueur WHERE numJoueur = {}".format(numJoueur))

def deleteMatchGameByNum(numMatch : int):
    """ Supprime un match de la base de donnée """
    execute("DELETE FROM MatchGame WHERE numMatch = {}".format(numMatch))

def deleteCompetitionByNum(numCompetition : str):
    """ Supprime une competition de la base de donnée """
    execute("DELETE FROM Competition WHERE numCompetition = {}".format(numCompetition))

def deleteClassementByNum(numClassement : int):
    """ Supprime un classement de la base de donnée """
    execute("DELETE FROM Classement WHERE numClassement = {}".format(numClassement))

def deleteCompetitionWithClassementAndMatch(numCompetition : int):
    """ Permet de supprimer une competition avec ses classements et matchs associés """
    execute("DELETE FROM Classement WHERE numCompetition = {}".format(numCompetition))
    execute("DELETE FROM MatchGame WHERE numCompetition = {}".format(numCompetition))
    execute("DELETE FROM Competition WHERE numCompetition = {}".format(numCompetition))
    
"----------------------------------------------------------------------------------------------------------------------"

""" Requêtes SQL Update """


def updateEquipe(numEquipe : int, nomEquipe : str, nbJoueur : int, Logo : str):
    """ Permet de modifier une equipe dans la base de donnée """
    execute("""UPDATE Equipe SET nomEquipe = "{}", nbJoueur = "{}", Logo = "{}" WHERE numEquipe = {}""".format(nomEquipe,nbJoueur,Logo,numEquipe))

def updateJoueur(numJoueur : int,numEquipe : int, pseudo : str, dateNaissance : str, email : str) :
    """ Permet de modifier un joueur dans la base de donnée """
    execute("""UPDATE Joueur SET pseudo = "{}", dateNaissance = "{}", email = "{}", numEquipe = "{}" WHERE numJoueur = {}""".format(pseudo,dateNaissance,email,numEquipe,numJoueur))

def updateMatchGame(numMatch : int, numCompetition : str,  numEquipe1 : str, numEquipe2 : str,scoreEquipe1 : int, scoreEquipe2 : int, Duree : str):
    """ Permet de modifier un match dans la base de donnée """
    execute("""UPDATE MatchGame SET numCompetition = "{}", scoreEquipe1 = "{}", scoreEquipe2 = "{}", numEquipe1 = "{}", numEquipe2 = "{}", Duree = "{}" WHERE numMatch = {}""".format(numCompetition,scoreEquipe1,scoreEquipe2,numEquipe1,numEquipe2,Duree,numMatch))

def updateCompetition(numCompetition : int, nomCompetition : str, dateDebut : str, dateFin : str, Web : str, lieu : str, Prix : str, Jeu : str):
    """ Permet de modifier une competition dans la base de donnée """
    execute("""UPDATE Competition SET nomCompetition = "{}", dateDebut = "{}", dateFin = "{}", Web = "{}", lieu = "{}", Prix = "{}", Jeu = "{}" WHERE numCompetition = {}""".format(nomCompetition,dateDebut,dateFin,Web,lieu,Prix,Jeu,numCompetition))

def updateClassement(numClassement : int, numCompetition : int, numEquipe : int, Position : str, score : str, Gain : int):
    """ Permet de modifier un classement dans la base de donnée """
    execute("""UPDATE Classement SET numCompetition = "{}", numEquipe = "{}", Position = "{}", Score = "{}", Gain = "{}" WHERE numClassement = {}""".format(numCompetition,numEquipe,Position,score,Gain,numClassement))

"----------------------------------------------------------------------------------------------------------------------"

""" Requêtes SQL Select """


def selectEquipe() -> list:
    """ Permet de afficher une equipe dans la base de donnée """
    return execute("SELECT * FROM Equipe")

def selectEquipeByNum(numEquipe : int) -> list:
    """ Permet de selectionner une equipe dans la base de donnée """
    return execute("SELECT * FROM Equipe WHERE numEquipe = {}".format(numEquipe))



def selectJoueur() -> list:
    """ Permet de afficher un joueur dans la base de donnée """
    return execute("SELECT * FROM Joueur")

def selectMatchGame() -> list:
    """ Permet de afficher un match dans la base de donnée """
    return execute("SELECT * FROM MatchGame")

def selectCompetition() -> list:
    """ Permet de afficher une competition dans la base de donnée """
    return execute("SELECT * FROM Competition")

def selectClassement() -> list:
    """ Permet de afficher un classement dans la base de donnée """
    return execute("SELECT * FROM Classement")

def selectJoueurByEquipe(numEquipe : str) -> list:
    """ Permet de selectionner les joueurs d'une equipe dans la base de donnée """
    return execute("SELECT * FROM Joueur WHERE numEquipe = {}".format(numEquipe))

def selectMatchGameByCompetition(numCompetition : str) -> list:
    """ Permet de selectionner les match d'une competition dans la base de donnée """
    return execute("SELECT * FROM MatchGame WHERE numCompetition = {}".format(numCompetition))

def selectClassementByCompetition(numCompetition : int) -> list:
    """ Permet de selectionner les classements d'une competition dans la base de donnée """
    return execute("SELECT * FROM Classement WHERE numCompetition = {}".format(numCompetition))

def selectCompetitionByNum(numCompetition : str) -> list:
    """ Permet de selectionner une competition dans la base de donnée """
    return execute("SELECT * FROM Competition WHERE numCompetition = {}".format(numCompetition))

def selectEquipeByTournoi(numCompetition : str) -> list:
    """ Permet de selectionner les equipes d'une competition dans la base de donnée """
    return execute("SELECT numEquipe,nomEquipe FROM Equipe WHERE numEquipe IN (SELECT numEquipe FROM Classement WHERE numCompetition = {})".format(numCompetition))

def selectMatchByNum(numMatch : int) -> list:
    """ Permet de selectionner un match dans la base de donnée """
    return execute("SELECT * FROM MatchGame WHERE numMatch = {}".format(numMatch))

def selectClassementByNum(numClassement : int) -> list:
    """ Permet de selectionner un classement dans la base de donnée """
    return execute("SELECT * FROM Classement WHERE numClassement = {}".format(numClassement))

def selectJoueurByNum(numJoueur : int) -> list:
    """ Permet de selectionner un joueur dans la base de donnée """
    return execute("SELECT * FROM Joueur WHERE numJoueur = {}".format(numJoueur))
"----------------------------------------------------------------------------------------------------------------------"

""" Requêtes SQL Jointure """

def afficheJoueurWithEquipe():
    """ Permet d'afficher les joueurs avec le nom de l'equipe et si le joueur n'a pas d'equipe, affiche "Aucune equipe" """
    resultat = execute("""SELECT Joueur.numJoueur, Joueur.pseudo, Equipe.nomEquipe, Joueur.email, Joueur.dateNaissance FROM Joueur LEFT JOIN Equipe ON Joueur.numEquipe = Equipe.numEquipe""")
    return resultat
    

def afficheClassementByTournoiWithEquipeName(numCompetition : str) -> list:
    """ Permet d'afficher les classements d'une competition avec le nom de l'equipes """
    return execute("""SELECT Classement.numClassement, Equipe.nomEquipe, Classement.Position, Classement.Score, Classement.Gain FROM Classement INNER JOIN Equipe ON Classement.numEquipe = Equipe.numEquipe WHERE Classement.numCompetition = {}""".format(numCompetition))

""" Requêtes SQL Selection Complexe """

def afficheMatchByTournoiWithEquipeName(numCompetition : str) -> list:
    """ Permet d'afficher les matchs d'une competition avec le nom de l'equipes """
    match = execute("SELECT * FROM MatchGame WHERE numCompetition = {}".format(numCompetition))
    resultat = []
    total = []
    tout = []
    for i in match :
        total = []
        resultat = []
        matchId = execute("SELECT numMatch FROM MatchGame WHERE numMatch = {}".format(i[0]))
        equipe1 = execute("SELECT nomEquipe,Logo FROM Equipe WHERE numEquipe = {}".format(i[2]))
        equipe2 = execute("SELECT nomEquipe,Logo FROM Equipe WHERE numEquipe = {}".format(i[3]))
        score1 = execute("SELECT scoreEquipe1 FROM MatchGame WHERE numMatch = {}".format(matchId[0][0]))
        score2 = execute("SELECT scoreEquipe2 FROM MatchGame WHERE numMatch = {}".format(matchId[0][0]))
        duree = execute("SELECT Duree FROM MatchGame WHERE numMatch = {}".format(matchId[0][0]))
        total = append(matchId,total)
        total = append(equipe2,total)
        total = append(equipe1,total)
        total = append(score2,total)
        total = append(score1,total)
        total = append(duree,total)
        resultat.append(total)
        tout = tout + resultat
    return tout

def convertDureeToSQL(duree):
    duree = duree.split(":")
    duree = duree[0] + ":" + duree[1] + ":" + duree[2]
    return duree
    

print(afficheJoueurWithEquipe())

# updateMatchGame(idMatch,idTournoi,ScoreEquipe1,ScoreEquipe2,idEquipe1,idEquipe2,DateMatch)
