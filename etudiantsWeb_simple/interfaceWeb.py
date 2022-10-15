import cherrypy, os, os.path

from mako.template import Template
from mako.lookup import TemplateLookup
from BDEtudiantUtils import getEtudiantsStr, insertEtudiant, getParAge

mylookup = TemplateLookup(directories=['res/templates'], input_encoding='utf-8', module_directory='res/tmp/mako_modules')

class InterfaceWebEtudiants(object):    
    ###### Page d'accueil #############
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()

    @cherrypy.expose
    def todo(self):
        mytemplate = mylookup.get_template("todo.html")
        return mytemplate.render()
    
    ###### Pages d'affichages ###########        
    @cherrypy.expose
    def affParOrdre(self):
        mytemplate = mylookup.get_template("aff_index.html")
        return mytemplate.render(mesEtud=getEtudiantsStr())

    @cherrypy.expose
    def affParAge(self):
        mytemplate = mylookup.get_template("aff_parAge.html")        
        return mytemplate.render(mesEtud=getParAge())

    ###### Pages d'insertion ###########        
    @cherrypy.expose
    def insertPage(self):        
        mytemplate = mylookup.get_template("insert.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs", type="info")

    @cherrypy.expose
    def insertDone(self, prenom=None, nom=None, bday=None):
        # le test suivant est rendu inutile par l'utilisation de javascript dans formulaire bootstrap
        if prenom and nom and bday :
            print(bday, " -:- ", type(bday))
            try:
                insertEtudiant(prenom, nom, bday)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("insert.html")        
        return mytemplate.render(message=message, type=typ)
    
if __name__ == '__main__':
    rootPath = os.path.abspath(os.getcwd())
    print("la racine du site est :\n\t{}\n\tcontient : {}".format(rootPath,os.listdir()))
    cherrypy.quickstart(InterfaceWebEtudiants(), '/', 'config.txt')
