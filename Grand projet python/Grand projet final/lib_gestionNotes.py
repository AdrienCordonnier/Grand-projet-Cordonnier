# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv

def gestionNotes(id_,menu_choix,annee,matiere,note) :
    """
    Cette fonction a pour objectif de gérer les notes contenues dans un fichier csv.
    IN : 
    OUT :
    """
    def ajoutNote(id_,id1,annee,matiere,note):
        """
        Cette fonction a pour objectif d'ajouter une note dans un fichier csv
        IN :id de l'étudiant, id de la note, année, matiere, note
        OUT :
        """
        
        #ouverture du fichier "notes.csv"
        notes = [id1,annee,id_,matiere,note]
        f = ouverture_fichier_csv("notes.csv")

        #code pour avoir la note entre 0 et 20
        if float(note) > 20 or float(note) < 0:
            from tkinter import messagebox
            messagebox.showerror('Erreur',
                                'la note doit être comprise entre 0 et 20')
            return
        
        #création de l'id de la note
        for i in f[1:]:
            if i[0] == (id1):
                id1 = str(int(id1)+1)
        for i in f[1:]:
            
            #Boucle pour ne pas avoir de doublons dans le fichier
            if i[2] == id_ and i[3] == matiere and annee == i[1] and note == i[4]:
                from tkinter import messagebox
                messagebox.showerror('Erreur',
                                    'cette note est deja dans la base de donnée')
                return
        notes = [id1,annee,id_,matiere,note]
        
        #réécriture du fichier avec la nouvelle note
        f.append(notes)
        ecriture_fichier_csv([f[-1]],"notes.csv",'a')
        return
    
    def modificationNote(id_,note):
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        
        #ouverture du fichier "notes.csv"
        f = ouverture_fichier_csv("notes.csv")
        a = 0
        id1=0
        
        #code pour avoir la note entre 0 et 20
        if float(note) > 20 or float(note) < 0:
            from tkinter import messagebox
            messagebox.showerror('Erreur',
                                'la note doit être comprise entre 0 et 20')
            return
        #modification de la note au bon endroit
        for i in f[1:]:
            a = a + 1
            if i[0] == id_ :
                f[a][4] = note
            id1 = id1 + 1
            
        #réécriture du fichier avec la note modifiée
        ecriture_fichier_csv(f,"notes.csv",'w')
        return
    
    def suppressionNote(id_):
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        #ouverture du fichier "notes.csv"
        f = ouverture_fichier_csv("notes.csv")
        a = 1
        
        #suppression de la note
        for i in f[1:]:
            a = a + 1
            if i[0] == id_ :
                f.pop(a-1)
                break
            
        #réécriture du fichier sans la note supprimée
        ecriture_fichier_csv(f,"notes.csv",'w')
        return
    
    def affichageNote() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des informations
        notes des etudiants.
        Cette fonction n'est pas utilisée dans le programme final.
        Soit : ID, Matiere, Note
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier 
        ##################################################
        nomfichier = "notes.csv"
        data = ouverture_fichier_csv(nomfichier)



        print("***********************************************************************************************************")
        print("*                                          Gestion Scolaire                                               *")
        print("***********************************************************************************************************")
        print("*   ID Etudiant                       *       Matiere                           *        Note             *")
        print("***********************************************************************************************************")

        for i in range(1,len(data)) :
            print("* {:<40}  * {:<40}  * {:>3} *" . format(data[i][2], data[i][3], data[i][4]))

        print("***********************************************************************************************************\n")

        
    ##################################################
    #Lancement de la bonne fonction selon la variable du bouton sélectionné
    ##################################################
    while True:
        menu_choix = menu_choix

        if menu_choix == 1 :
            F = ouverture_fichier_csv("notes.csv")
            
            #récuperation des données
            id1 = len(F)-5
            id1 = str(id1)
            id_ = str(id_)
            annee = str(annee)
            matiere = matiere.capitalize()
            note = str(float(note))

            #Lancement de la fonction 
            ajoutNote(id_,id1,annee,matiere,note)
            break
        
        if menu_choix == 2 :
            #récupération des données 
            id_ = str(id_)
            annee = str(annee)
            matiere = matiere.capitalize()
            note = str(float(note))
            #lancement de la fonction
            modificationNote(id_,note)
            break
        
        if menu_choix == 3 :
            #récuperation des données
            id_ = str(id_)
            annee = str(annee)
            matiere = matiere.capitalize()
            note = note
            #lancement de la fonction
            suppressionNote(id_)
            break
        
        if menu_choix == 4 :
            affichageNote() 


        if menu_choix == 5 :
            return 

