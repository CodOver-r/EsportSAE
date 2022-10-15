from BDesport import *
from gestionBD import menuGestionDB


# Fonction qui permet d'ajouter une équipe dans la base de données
def insertByCliEquipe():
    nomEquipe = input("Nom de l'équipe : ")
    nbJoueur = int(input("Nombre de joueur : "))
    Logo = input("Logo de l'équipe (URL) : ")
    insertEquipe(nomEquipe, nbJoueur, Logo)

# Fonction qui permet d'ajouter un joueur dans la base de données
def insertByCliJoueur():
    numEquipe = input("Numéro de l'equipe : ")
    pseudo = input("Pseudo du joueur : ")
    dateNaissance = input("Date de naissance du joueur (JJ/MM/AAAA) : ")
    email = input("Email du joueur : ")
    dateNaissance = date2ISO(dateNaissance)
    insertJoueur(numEquipe, pseudo, dateNaissance, email)

# Fonction qui permet d'ajouter un match dans la base de données
def insertByCliMatchGame():
    numCompetition = input("Numéro de la compétition : ")
    scoreEquipe1 = int(input("Score de l'équipe 1 : "))
    scoreEquipe2 = int(input("Score de l'équipe 2 : "))
    numEquipe1 = input("Numéro de l'équipe 1 : ")
    numEquipe2 = input("Numéro de l'équipe 2 : ")
    Duree = input("Durée du match (HH:MM:SS) : ")
    insertMatchGame(numCompetition, scoreEquipe1, scoreEquipe2, numEquipe1, numEquipe2, Duree)


# Fonction qui permet d'ajouter une compétition dans la base de données
def insertByCliCompetition():
    nomCompetition = input("Nom de la compétition : ")
    dateDebut = input("Date de début de la compétition (JJ/MM/AAAA) : ")
    dateFin = input("Date de fin de la compétition (JJ/MM/AAAA) : ")
    Web = input("Site web de la compétition : ")
    lieu = input("Lieu de la compétition : ")
    Prix = input("Prix de la compétition : ")
    Jeu = input("Jeu de la compétition : ")
    dateDebut = date2ISO(dateDebut)
    dateFin = date2ISO(dateFin)
    insertCompetition(nomCompetition, dateDebut, dateFin, Web, lieu, Prix, Jeu)


# Fonction qui permet d'ajouter un classement dans la base de données
def insertByCliClassement():
    numCompetition = input("Numéro de la compétition : ")
    numEquipe = input("Numéro de l'équipe : ")
    Position = input("Position de l'équipe (1er, 2e, ...) : ")
    Score = input("Score de l'équipe (Final, Demi-Final... ou Point Obtenue en fonction du Jeu de la Compétition): ")
    Gain = input("Gain de la compétition : ")
    insertClassement(numCompetition, numEquipe, Position, Score, Gain)

# Fonction qui permet de supprimer une équipe dans la base de données
def deleteByCliEquipeByNum():
    numEquipe = input("Numéro de l'équipe : ")
    deleteEquipeByNum(numEquipe)

# Fonction qui permet de supprimer un joueur dans la base de données
def deleteByCliJoueurByNum():
    numJoueur = input("Numéro du joueur : ")
    deleteJoueurByNum(numJoueur)

# Fonction qui permet de supprimer une compétition dans la base de données
def deleteByCliCompetitionByNum():
    numCompetition = input("Numéro de la compétition : ")
    deleteCompetitionByNum(numCompetition)

# Fonction qui permet de supprimer un match dans la base de données
def deleteByCliMatchGameByNum():
    numMatch = input("Numéro du match : ")
    deleteMatchGameByNum(numMatch)

# Fonction qui permet de supprimer un classement dans la base de données
def deleteByCliClassementByNum():
    numClassement = input("Numéro du classement : ")
    deleteClassementByNum(numClassement)

# Fonction qui permet de modifier une équipe dans la base de données
def updateByCliEquipe():
    numEquipe = input("Numéro de l'équipe : ")
    nomEquipe = input("Nom de l'équipe : ")
    nbJoueur = int(input("Nombre de joueur : "))
    Logo = input("Logo de l'équipe : ")
    updateEquipe(numEquipe, nomEquipe, nbJoueur, Logo)

# Fonction qui permet de modifier un joueur dans la base de données
def updateByCliJoueur():
    numJoueur = input("Numéro du joueur : ")
    numEquipe = input("Numéro de l'equipe : ")
    pseudo = input("Pseudo du joueur : ")
    dateNaissance = input("Date de naissance du joueur (JJ/MM/AAAA) : ")
    email = input("Email du joueur : ")
    dateNaissance = date2ISO(dateNaissance)
    updateJoueur(numJoueur, numEquipe, pseudo, dateNaissance, email)
# Fonction qui permet de modifier une compétition dans la base de données
def updateByCliCompetition():
    numCompetition = input("Numéro de la compétition : ")
    nomCompetition = input("Nom de la compétition : ")
    dateDebut = input("Date de début de la compétition (JJ/MM/AAAA) : ")
    dateFin = input("Date de fin de la compétition (JJ/MM/AAAA) : ")
    Web = input("Site web de la compétition : ")
    lieu = input("Lieu de la compétition : ")
    Prix = input("Prix de la compétition : ")
    Jeu = input("Jeu de la compétition : ")
    dateDebut = date2ISO(dateDebut)
    dateFin = date2ISO(dateFin)
    updateCompetition(numCompetition, nomCompetition, dateDebut, dateFin, Web, lieu, Prix, Jeu)

# Fonction qui permet de modifier un match dans la base de données
def updateByCliMatchGame():
    numMatch = input("Numéro du match : ")
    numCompetition = input("Numéro de la compétition : ")
    scoreEquipe1 = int(input("Score de l'équipe 1 : "))
    scoreEquipe2 = int(input("Score de l'équipe 2 : "))
    numEquipe1 = input("Numéro de l'équipe 1 : ")
    numEquipe2 = input("Numéro de l'équipe 2 : ")
    Duree = input("Durée du match (HH:MM:SS) : ")
    updateMatchGame(numMatch, numCompetition, scoreEquipe1, scoreEquipe2, numEquipe1, numEquipe2, Duree)

# Fonction qui permet de modifier un classement dans la base de données
def updateByCliClassement():
    numClassement = input("Numéro du classement : ")
    numCompetition = input("Numéro de la compétition : ")
    numEquipe = input("Numéro de l'équipe : ")
    Position = input("Position de l'équipe (1er, 2e, ...) : ")
    Score = input("Score de l'équipe (Final, Demi-Final... ou Point Obtenue en fonction du Jeu de la Compétition): ")
    Gain = input("Gain de la compétition : ")
    updateClassement(numClassement, numCompetition, numEquipe, Position, Score, Gain)

# Fonction qui permet d'afficher les équipes dans la base de données
def selectByCliEquipe():
    print("Numéro équipe | Nom équipe | Nombre joueur | Logo")
    var = selectEquipe()
    for i in var:
        print(i[0], "|", i[1], "|", i[2], "|", i[3])

# Fonction qui permet d'afficher les joueurs dans la base de données
def selectByCliJoueur():
    print("Numéro joueur | Numéro équipe | Pseudo | Date naissance | Email")
    var = selectJoueur()
    for i in var:
        print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4])

# Fonction qui permet d'afficher les compétitions dans la base de données
def selectByCliCompetition():
    print("Numéro compétition | Nom compétition | Début compétition | Fin compétition | Site web | Lieu | Prix | Jeu ")
    var = selectCompetition()
    for i in var:
        print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "|", i[5], "|", i[6], "|", i[7])
    
# Fonction qui permet d'afficher les matchs dans la base de données
def selectByCliMatchGame():
    print("Numéro match | Numéro compétition | Score équipe 1 | Score équipe 2 | Num équipe 1 | Num équipe 2 | Durée ")
    var = selectMatchGame()
    for i in var:
        print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "|", i[5], "|", i[6])

# Fonction qui permet d'afficher les classements dans la base de données
def selectByCliClassement():
    print("Numéro classement | Numéro compétition | Numéro équipe | Position équipe | Score équipe | Gain ")
    var = selectClassement()
    for i in var:
        print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "|", i[5])

# Fonction qui permet d'afficher les joueurs d'une équipe
def selectByCliJoueurByEquipe():
    numEquipe = input("Numéro de l'équipe : ")
    print("Numéro joueur | Numéro équipe | Pseudo joueur | Date de naissance| Email")
    var = selectJoueurByEquipe(numEquipe)
    for i in var:
        print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4])

# Fonction qui permet d'afficher les matchs d'une compétition
def selectByCliMatchGameByCompetition():
    numCompetition = input("Numéro de la compétition : ")
    print("Numéro match | Numéro compétition | Score équipe 1 | Score équipe 2 | Num équipe 1 | Num équipe 2 | Durée")
    var = selectMatchGameByCompetition(numCompetition)
    for i in var:
        print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "|", i[5], "|", i[6])

# Fonction qui permet d'afficher les classements d'une compétition
def selectByCliClassementByCompetition():
    numCompetition = input("Numéro de la compétition : ")
    print("Numéro classement | Numéro compétition | Numéro équipe | Position équipe | Score équipe | Gain")
    var = selectClassementByCompetition(numCompetition)
    for i in var:
        print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "|", i[5])
    
def date2ISO(date):

    """ fonction de conversion d'une date-chaîne au format "habituel" (jj/mm/aaaa)
            au format  ISO (yyyy-mm-jj)
    """
    d = date.split('/')
    s = d[2]+"-"+ d[1]+"-"+d[0]
    return s

def afficheMenu(choixActions):
    print ("Choix possibles :")
    for ch  in choixActions:
        print ("{} : {}".format(choixActions.index(ch)+1, ch[0] ))
    print ("{} : {}".format( len(choixActions)+1 , "Quitter" ))
       
def MenuInsertion():
    listeChoix = [
        ("Insertion d'une équipe", insertByCliEquipe),
        ("Insertion d'un joueur", insertByCliJoueur),
        ("Insertion d'une compétition", insertByCliCompetition),
        ("Insertion d'un match", insertByCliMatchGame),
        ("Insertion d'un classement", insertByCliClassement),
    ]
    AffichageMenuCLI(listeChoix)

def MenuDeletion():
    listeChoix = [
        ("Suppression d'une équipe", deleteByCliEquipeByNum),
        ("Suppression d'un joueur", deleteByCliJoueurByNum),
        ("Suppression d'une compétition", deleteByCliCompetitionByNum),
        ("Suppression d'un match", deleteByCliMatchGameByNum),
        ("Suppression d'un classement", deleteByCliClassementByNum)]
    AffichageMenuCLI(listeChoix)

def MenuAffichage():
    listeChoix = [
        ("Affichage des équipes", selectByCliEquipe),
        ("Affichage des joueurs", selectByCliJoueur),
        ("Affichage des compétitions", selectByCliCompetition),
        ("Affichage des matchs", selectByCliMatchGame),
        ("Affichage des classements", selectByCliClassement),
        ("Affichage des joueurs d'une équipe", selectByCliJoueurByEquipe),
        ("Affichage des matchs d'une compétition", selectByCliMatchGameByCompetition),
        ("Affichage des classements d'une compétition", selectByCliClassementByCompetition)]
    AffichageMenuCLI(listeChoix)

def MenuModification():
    listeChoix = [
        ("Modification d'une équipe", updateByCliEquipe),
        ("Modification d'un joueur", updateByCliJoueur),
        ("Modification d'une compétition", updateByCliCompetition),
        ("Modification d'un match", updateByCliMatchGame),
        ("Modification d'un classement", updateByCliClassement),]
    AffichageMenuCLI(listeChoix)

        
def AffichageMenuCLI(listeChoix):
        while True :
            afficheMenu(listeChoix)
            try :
                choix = int(input("Votre Choix ? : "))
                if ( choix == len(listeChoix) + 1 ):
                        break
                elif 1 <= choix and choix <= len(listeChoix):
                    label, fct = listeChoix[choix-1] # recuperer adresse fct associee
                    fct()
                else :
                    print ("Choix non valide !")
            except IndexError :
                print ('Choix non valide !')
            except ValueError :
                print ('Entrez un entier !')

if __name__ == "__main__":
    listeChoix = [
        ("Ajouter une donnée", MenuInsertion),
        ("Supprimer une donnée", MenuDeletion),
        ("Afficher une donnée", MenuAffichage),
        ("Modifier une donnée", MenuModification),
        ("Gestion de la base de données", menuGestionDB)]
    AffichageMenuCLI(listeChoix)
    print ("Au revoir!")