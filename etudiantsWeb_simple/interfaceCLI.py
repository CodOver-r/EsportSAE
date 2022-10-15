import os
from BDEtudiantUtils import dbToString, insertEtudiant

def blackHole():
    print ("Action non encore implémentée")
             
def printCollec() :
    """ affiche le contenu de la base """
    # se contente d'afficher la chaîne rendue par la fonction "dbToString()"
    print (dbToString())

def printParAge():
    """ affiche le contenu de la base, rangé par ordre d'âge """
    pass
        
def printPlusJeune():
    """ affiche le ou un des plus jeune de la base """
    pass
            
def addEtudiant():
    """ ajout d'un étudiant """
    prenom = input("Entrez le prénom de l'étudiant : ")
    nom = input("Entrez le nom de l'étudiant : ")
    jour = input("Maintenant sa date de Naissance , d'abord le jour : ")
    mois = input("le mois : ")
    annee = input("l'année : ")
    date = "{:04d}-{:02d}-{:02d}".format(int(annee), int(mois), int(jour))
    try :
        insertEtudiant( prenom, nom, date )
        printCollec()
    except Exception as e :
        print ("Erreur: ", e)
        
def removeEtudiantByNum():
    """ supprime un étudiant """
    pass

def loadFromCSV():
    # effectue la saisie du nom du fichier "csv" et
    # utilise la fonction "loadFromCSVFile()"
    pass

def afficheMenu(choixActions):
    print ("Choix possibles :")
    for ch  in choixActions:
        print ("{} : {}".format(choixActions.index(ch)+1, ch[0] ))
    print ("{} : {}".format( len(choixActions)+1 , "Quitter" ))
            
if __name__ == '__main__':
    print("Fichiers dans le répertoire courant : {}".format(os.listdir()))

    listeChoix = [ 
             ("Afficher",printCollec),
             ("Afficher la collection par ordre d'âge",printParAge),
             ("Afficher le (un des) plus jeune(s)", printPlusJeune),
             ("Insérer un étudiant", addEtudiant),
             ("Supprimer un étudiant (par son numéro)", removeEtudiantByNum),
             ("Charger un fichier (CSV)", loadFromCSV)
             ]
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
                print ("*** Choix non valide, recommencez!")
        except IndexError as e:
            print(e)
            print ('*** Choix non valide, recommencez!')
        except ValueError as e :
            print(e)
            print ('*** Entrez un entier SVP')
        print ("BYE!")
        
