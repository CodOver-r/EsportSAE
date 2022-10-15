import os
import pymysql, sqlite3

# les fonctions suivantes réalisent une petite interface avec la BD
def dbConnect(sqlite3=False,fich="etudiants.db",base="etudiants"):
    if sqlite3 :
        db = sqlite3.connect(fich)
    else :
        db = pymysql.connect(host="localhost", charset="utf8", user="root", passwd="",db=base)
    return (db,db.cursor())
