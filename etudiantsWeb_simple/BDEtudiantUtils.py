import os
from configDB import dbConnect

##  La collection est stockee dans une base de donnée, dont le format est fixé :
##  Pas de tentative de rendre le code générique, pour éviter de donner un corrigé trop complexe.
## 
##  Néanmoins le maximum a été encapsulé dans des parties spécifiques pour faciliter
##  les modifications éventuelles.
##
##  La connection est effectuée à chaque fois...:-(
# les fonctions suivantes permettent de créer des requêtes "SQL" avec des valeurs variables

_requetes = {
    "create" : """ CREATE TABLE etudiant (
                numEtudiant INTEGER PRIMARY KEY AUTOINCREMENT,
                prenom NOT NULL,
                nom NOT NULL,
                dateNaissance NOT NULL default '2000-01-01') ; """,
    "getAll" : "select * from etudiant order by nom, prenom;",
    "getAllParAge" : "select * from etudiant order by dateNaissance desc;",
    "insert" : "insert into etudiant (prenom,nom,dateNaissance) values ('{}','{}','{}');",
     }

def mkInsertRequest(prenom, nom, anniversaire) :
    s= _requetes["insert"].format(prenom.capitalize(),nom.upper(),anniversaire)
    return s

def execute(req) :
    _dbEtudiant, _cursorEtudiant = dbConnect(False)
    res = _cursorEtudiant.execute(req)
    if "select" in req :
        res = _cursorEtudiant.fetchall()
    else :
        _dbEtudiant.commit()
    return res

def executeReq(req) :
    _dbEtudiant, _cursorEtudiant = dbConnect(False)
    cr = _cursorEtudiant.execute(req)
    res = _cursorEtudiant.fetchall()
    _dbEtudiant.commit()
    return cr,res

def getEtudiants():
    """ getEtudiants() -> liste de tuples "Etudiant"
    Rend le contenu de la base sous forme d'une liste de tuples """
    req = _requetes["getAll"]
    etudiants = []
    for t in execute(req) :
        etudiants.append(t)
    return etudiants

def getEtudiantsStr():
    """ getEtudiantsStr() -> liste de chaînes
    Rend le contenu de la base sous forme d'une liste de chaînes """
    req = _requetes["getAll"]
    etudiants = []
    for t in execute(req) :
        etudiants.append(etudToString(t))
    return etudiants

# les 2 fonctions suivantes permettent de convertir des dates du format ISO (format stocké dans la base)
#    au format "habituel" (jj/mm/aaaa) pour affichage, ou pour écriture dans les fichiers texte
def isoDate2String(date):
    """ fonction de conversion d'une date-chaîne au format ISO (yyyy-mm-jj)
            au format "habituel" (jj/mm/aaaa) 
    """
    d = date.split('-')
    s= d[2]+"/"+ d[1]+"/"+d[0]
    return s
    
def date2ISO(date):
    """ fonction de conversion d'une date-chaîne au format "habituel" (jj/mm/aaaa)
            au format  ISO (yyyy-mm-jj)
    """
    d = date.split('/')
    s = d[2]+"-"+ d[1]+"-"+d[0]
    return s

# les fonctions suivantes opèrent sur les "etudiants"
def etudToString(etud):
    """ Rend le tuple sous forme d'une chaîne de caractères """
    anniv = etud[3].strftime("%d/%m/%Y")
    return "n°{} : {} {} né(e) le {}".format(etud[0], etud[1], etud[2], anniv)

def etudToCSV(etud):
    """ Rend le tuple sous forme d'une chaîne de caractères, format csv"""
    anniv = etud[3].strftime("%d/%m/%Y")
    return "{};{};{};{};".format(etud[0], etud[1], etud[2], anniv)

# les fonctions suivantes opèrent sur la collection
def dbToString():
    """ Rend le contenu de la base sous forme d'une chaîne de caractères """
    s= ''
    for etud in getEtudiants():
        s = s + etudToString(etud) + "\n"
    return s

def dbToFile():
    """ strToFile() -> str
    rend une chaîne au format "csv"
    """
    s = ''
    for etud in getEtudiants() :
        s = s + etudToCSV(etud) + '\n'
    return s

def reset():
    """ Remise à zéro de la table """
    req = _requetes["reset"]
    execute(req)

def getParAge():
    """ Rend le contenu de la base sous forme d'une liste de tuples, rangés par ordre d'âge """
    req = _requetes["getAllParAge"]
    return execute(req)
        
def getPlusJeune():
    """ Rend une ou une des étudiant le ou la plus jeune """
    req = _requetes["getAllParAge"]
    return execute(req)[0]

def insertEtudiant( prenom : str, nom : str, dateNaissance : str)-> None :
    """ Insertion d'un étudiant dans la collection"""
    req = mkInsertRequest(prenom.capitalize(),nom.upper(),dateNaissance)
    execute(req)

def deleteEtudiant( prenom, nom):
    """ Suppression d'un étudiant dans la collection"""
    p = prenom.capitalize()
    n = nom.upper()
    reqVerif = mkGetByNomRequest(p, n)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkDeleteRequest(p, n)
    execute(req)

def deleteEtudiantByNum(num):
    """ Suppression d'un étudiant dans la collection"""
    reqVerif = mkGetByNumRequest(num)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkDeleteByNumRequest(num)
    execute(req)

def loadFromCSVFile(path : str) -> None:
    """ Permet de charger une base à partir d'un fichier texte "CSV" """
    import csv
    with open(path, newline='\n',encoding='utf-8') as csvFile :
        lignesEtud = csv.reader(csvFile,delimiter=';')
        for champs in lignesEtud :
            if len(champs) < 3 :
                print ("ligne incorrecte : <{}>, ignorée".format(champs))
                continue
            prenom = champs[0].capitalize()
            nom = champs[1].upper()
            date = date2ISO(champs[2])
            insertEtudiant(prenom,nom,date)

if __name__ == '__main__':
    print("Fichiers dans le répertoire courant : {}".format(os.listdir()))
    choix = input("Par défaut : SGBDR MySQL, localhost perso : tapez 'entrée' pour continuer : ")
    while choix != '' :
        print("Pas d'autres choix implémentés pour l'instant!")
        choix = input("Par défaut : SGBDR MySQL, localhost perso : tapez 'entrée' pour continuer : ")
        
    print ("====== ")
    print (dbToString())
    input("Une touche pour finir")
        
