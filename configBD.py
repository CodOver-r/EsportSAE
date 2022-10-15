import pymysql

host = "localhost"  # Adresse du serveur
charset = "utf8"  # Encodage des caractères
user = "root"  # Nom d'utilisateur
passwd = ""  # Mot de passe
bd = "DBesport"  # Nom de la base de données

def dbConnect():
    db = pymysql.connect(host=host, user=user, passwd=passwd, charset=charset)
    cursor = db.cursor()
    return db, cursor

def dbConnectEsport():
    db = pymysql.connect(host=host, user=user, passwd=passwd, db=bd, charset=charset)
    cursor = db.cursor()
    return db, cursor

