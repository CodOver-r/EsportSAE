import cherrypy, os, os.path

from mako.template import Template
from mako.lookup import TemplateLookup
from BDesport import *
from gestionBD import createDB,deleteDB,loadFromCSV
mylookup = TemplateLookup(directories=['res/template'], input_encoding='utf-8', output_encoding='utf-8')

class InterfaceWebEsport(object):    


    ###### Page d'accueil #############
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()

    ###### Pages d'affichages ###########        

    @cherrypy.expose
    def EquipeAffichage(self):
        mytemplate = mylookup.get_template("EquipeAffichage.html")
        return mytemplate.render(AffichageEquipes=selectEquipe())

    @cherrypy.expose
    def TournoiAffichage(self):
        mytemplate = mylookup.get_template("TournoiAffichage.html")
        return mytemplate.render(AffichageTournois=selectCompetition())

    @cherrypy.expose
    def JoueursAffichage(self):
        mytemplate = mylookup.get_template("JoueurAffichage.html")
        return mytemplate.render(AffichageJoueurs=afficheJoueurWithEquipe())

    ###### Pages d'insertion ###########        

    @cherrypy.expose
    def EquipeInsert(self):
        mytemplate = mylookup.get_template("EquipeInsert.html")
        return mytemplate.render()

    @cherrypy.expose
    def EquipeInsertREQ(self,Nom,nbJoueur,Logo):
        insertEquipe(Nom,nbJoueur,Logo)
        mytemplate = mylookup.get_template("EquipeInsert.html")
        return mytemplate.render(EquipeInsertREQ=1)


    @cherrypy.expose
    def TournoiInsert(self):
        mytemplate = mylookup.get_template("TournoiInsert.html")
        return mytemplate.render()

    @cherrypy.expose
    def TournoiInsertREQ(self,Nom,DateDebut,DateFin,Web,Lieu,Prix,Jeu):
        insertCompetition(Nom,DateDebut,DateFin,Web,Lieu,Prix,Jeu)
        mytemplate = mylookup.get_template("TournoiInsert.html")
        return mytemplate.render(TournoiInsertREQ=1)

    @cherrypy.expose
    def JoueursInsert(self):
        mytemplate = mylookup.get_template("JoueurInsert.html")
        return mytemplate.render()

    @cherrypy.expose
    def JoueurInsertREQ(self,numEquipe,Nom,Prenom,DateNaissance):
        insertJoueur(numEquipe,Nom,Prenom,DateNaissance)
        mytemplate = mylookup.get_template("JoueurInsert.html")
        return mytemplate.render(JoueurInsertREQ=1)
    

    """Page de modification"""

    @cherrypy.expose
    def EquipeEdit(self,idEquipe):
        mytemplate = mylookup.get_template("EquipeEdit.html")
        return mytemplate.render(AffichageEquipes=selectEquipeByNum(idEquipe))

    @cherrypy.expose
    def EquipeEditREQ(self,idEquipe,Nom,nbJoueur,Logo):
        updateEquipe(idEquipe,Nom,nbJoueur,Logo)
        mytemplate = mylookup.get_template("EquipeEdit.html")
        return mytemplate.render(EquipeEditREQ=1,AffichageEquipes=selectEquipeByNum(idEquipe))

    @cherrypy.expose
    def JoueurEdit(self,idJoueur):
        mytemplate = mylookup.get_template("JoueurEdit.html")
        return mytemplate.render(AffichageJoueurs=selectJoueurByNum(idJoueur))

    @cherrypy.expose
    def JoueurEditREQ(self,idJoueur,numEquipe,Pseudo,Email,DateNaissance):
        updateJoueur(idJoueur,numEquipe,Pseudo,DateNaissance,Email)
        mytemplate = mylookup.get_template("JoueurEdit.html")
        return mytemplate.render(JoueurEditREQ=1,AffichageJoueurs=selectJoueurByNum(idJoueur))

    @cherrypy.expose
    def TournoiEdit(self,idTournoi):
        mytemplate = mylookup.get_template("TournoiEdit.html")
        return mytemplate.render(AffichageTournoi=selectCompetitionByNum(idTournoi))

    @cherrypy.expose
    def TournoiEditREQ(self,idTournoi,Nom,DateDebut,DateFin,Web,Lieu,Prix,Jeu):
        updateCompetition(idTournoi,Nom,DateDebut,DateFin,Web,Lieu,Prix,Jeu)
        mytemplate = mylookup.get_template("TournoiEdit.html")
        return mytemplate.render(TournoiEditREQ=1,AffichageTournoi=selectCompetitionByNum(idTournoi))

    @cherrypy.expose
    def MatchUpdate(self,id):
        mytemplate = mylookup.get_template("MatchEdit.html")
        return mytemplate.render(AffichageMatch=selectMatchByNum(id))

    @cherrypy.expose
    def MatchEditREQ(self,idMatch,idTournoi,idEquipe1,idEquipe2,ScoreEquipe1,ScoreEquipe2,DateMatch):
        updateMatchGame(idMatch,idTournoi,idEquipe1,idEquipe2,ScoreEquipe1,ScoreEquipe2,DateMatch)
        mytemplate = mylookup.get_template("MatchEdit.html")
        return mytemplate.render(MatchUpdateREQ=1,AffichageMatch=selectMatchByNum(idMatch))

    @cherrypy.expose
    def ClassementUpdate(self,id):
        mytemplate = mylookup.get_template("ClassementEdit.html")
        return mytemplate.render(AffichageClassement=selectClassementByNum(id))

    @cherrypy.expose
    def ClassementEditREQ(self,idClassement,idTournoi,idEquipe,Position,Point,Gain):
        updateClassement(idClassement,idTournoi,idEquipe,Position,Point,Gain)
        mytemplate = mylookup.get_template("ClassementEdit.html")
        return mytemplate.render(ClassementEditREQ=1,AffichageClassement=selectClassementByNum(idClassement))

    """Page de suppression """

    @cherrypy.expose
    def EquipeDelete(self,idEquipe):
        mytemplate = mylookup.get_template("EquipeAffichage.html")
        print(idEquipe)
        deleteEquipeByNum(idEquipe[0:])
        return mytemplate.render(AffichageEquipes=selectEquipe())

    @cherrypy.expose
    def JoueurDelete(self,idJoueur):
        mytemplate = mylookup.get_template("JoueurAffichage.html")
        print(idJoueur)
        deleteJoueurByNum(idJoueur[0:])
        return mytemplate.render(AffichageJoueurs=selectJoueur())

    @cherrypy.expose
    def JoueurDeleteDetail(self,idJoueur,idEquipe):
        mytemplate = mylookup.get_template("EquipeDetail.html")
        deleteJoueurByNum(idJoueur[0:])
        return mytemplate.render(AffichageEquipes=selectEquipeByNum(idEquipe[0:]),AffichageJoueurs=selectJoueurByEquipe(idEquipe[0:]))

    @cherrypy.expose
    def TournoiDelete(self,idTournoi):
        mytemplate = mylookup.get_template("TournoiAffichage.html")
        deleteCompetitionWithClassementAndMatch(idTournoi[0:])
        return mytemplate.render(AffichageTournois=selectCompetition())

    @cherrypy.expose
    def MatchDelete(self,idMatch,idTournoi):
        mytemplate = mylookup.get_template("TournoiDetail.html")
        deleteMatchGameByNum(idMatch[0:])
        return mytemplate.render(AffichageTournois=selectCompetitionByNum(idTournoi),AffichageEquipe=selectEquipeByTournoi(idTournoi),AffichageClassement=afficheClassementByTournoiWithEquipeName(idTournoi),AffichageMatch=afficheMatchByTournoiWithEquipeName(idTournoi))

    @cherrypy.expose
    def ClassementDelete(self,idClassement,idTournoi):
        mytemplate = mylookup.get_template("TournoiDetail.html")
        deleteClassementByNum(idClassement[0:])
        return mytemplate.render(AffichageTournois=selectCompetitionByNum(idTournoi),AffichageEquipe=selectEquipeByTournoi(idTournoi),AffichageClassement=afficheClassementByTournoiWithEquipeName(idTournoi),AffichageMatch=afficheMatchByTournoiWithEquipeName(idTournoi))

    """Page de detail"""

    @cherrypy.expose
    def TournoiDetail(self,idTournoi):
        mytemplate = mylookup.get_template("TournoiDetail.html")
        return mytemplate.render(AffichageTournois=selectCompetitionByNum(idTournoi),AffichageEquipe=selectEquipeByTournoi(idTournoi),AffichageClassement=afficheClassementByTournoiWithEquipeName(idTournoi),AffichageMatch=afficheMatchByTournoiWithEquipeName(idTournoi))

    @cherrypy.expose   
    def EquipeDetail(self,idEquipe):
        mytemplate = mylookup.get_template("EquipeDetail.html")
        return mytemplate.render(AffichageEquipes=selectEquipeByNum(idEquipe[0:]),AffichageJoueurs=selectJoueurByEquipe(idEquipe[0:]))


    """Admin"""

    @cherrypy.expose
    def Reset(self):
        mytemplate = mylookup.get_template("index.html")
        deleteDB()
        createDB()
        loadFromCSV("BaseEsportData.csv")
        return mytemplate.render()



if __name__ == '__main__':
    rootPath = os.path.abspath(os.getcwd())
    print("la racine du site est :\n\t{}\n\tcontient : {}".format(rootPath,os.listdir()))
    cherrypy.quickstart(InterfaceWebEsport(), '/', 'config.txt')
