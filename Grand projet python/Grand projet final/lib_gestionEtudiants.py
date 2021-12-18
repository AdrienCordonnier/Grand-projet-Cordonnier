# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv

def gestionEtudiants(id_,menu_choix,prenom,nom,gendre,email) :
    """
    Cette fonction a pour objectifd'ajouter, de modifier ou de supprimer
    un étudiant d'un fichier csv
    IN :id_,menu_choix,prenom,nom,sexe,email
    OUT :
    """
    def ajoutEtudiant(id_,prenom,nom,gendre,email) :
        """
        Cette fonction a pour objectif d'ajouter un etudiant dans la
        base de donnée des etudiants.
        IN : id_, prenom, nom, gendre, email
        OUT : aucun retour
        """
        donnees = [id_,gendre,nom,prenom,email]
        f = ouverture_fichier_csv("etudiants.csv")

        #création automatique de l'id
        for i in f[1:]:
            if i[0] == (id_):
                id_ = str(int(id_)+1)
        for i in f[1:]:
            #pour ne pas avoir de doublons
            if i[4] == email and i[2] == nom:
                from tkinter import messagebox
                messagebox.showerror('Erreur',
                                    'cet etudiant est deja dans la base de donnée')
                return
        donnees = [id_,gendre,nom,prenom,email]  
        f.append(donnees)
        #réécriture du fichier avec les nouvelles données 
        ecriture_fichier_csv([f[-1]],"etudiants.csv",'a')
        
        return
    
    def modificationEtudiant(id_,prenom,nom,gendre,email) :
        """
        Cette fonction a pour objectif de modifier les informations que
        l'on a sur un étudiant.
        IN : id_, prenom, nom, gendre, email
        OUT :aucun retour
        """
        f = ouverture_fichier_csv("etudiants.csv")
        a = 0

        #modification de l'étudiant au bon endroit dans le fichier
        for i in f[1:]:
            a = a + 1
            if i[0] == (id_):
                f[a] = [id_,gendre,nom,prenom,email]

        #réécriture du fichier avec les données modifiées 
        ecriture_fichier_csv(f,"etudiants.csv",'w')
        return
    
    def suppressionEtudiant(id_) :
        """
        Cette fonction a pour objectif de supprimer un etudiant de
        la base de donnée des etudiants.
        IN :id_
        OUT : aucun retour
        """
        f = ouverture_fichier_csv("etudiants.csv")
        a = 0

        #Suppression de la ligne correspondant a la note
        for i in f[1:]:
            a = a + 1
            if i[0] == id_:
                f.pop(a)

        #réécriture du fichier sans la note supprimée
        ecriture_fichier_csv(f,"etudiants.csv",'w')
        
        return
    
    def affichageEtudiant() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des
        informations administratives des etudiants.
        Soit : ID, prenom, nom, gendre, email
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier 
        ##################################################
        nomfichier = "etudiants.csv"
        data = ouverture_fichier_csv(nomfichier)



        print("***********************************************************************************************************")
        print("*                                          Gestion Scolaire                                               *")
        print("***********************************************************************************************************")
        print("*   ID   *       Gendre      *        Nom              *   Prenom            * Email adresse     *")
        print("***********************************************************************************************************")

        for i in range(1,len(data)) :
            print("* {:<8}  * {:<20}  * {:<20}  *  {:<11}  * {:>3} *" . format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))

        print("***********************************************************************************************************\n")

        
    ##################################################
    #Lancement de la fonction voulu en fonction de la variable menu_choix
    ##################################################
    while True:
        
        menu_choix = menu_choix
        if menu_choix == 1 :
            F = ouverture_fichier_csv("etudiants.csv")
            id_ = len(F)
            id_ = str(id_)
            
            #récupération des données
            prenom = prenom.capitalize()
            nom = nom.upper()
            gendre = str(gendre).upper()
            email = str(email).lower()
            
            #lancement de la fonction
            ajoutEtudiant(id_,prenom,nom,gendre,email)
            break


        if menu_choix == 2 :
            id_ = str(id_)

            #récupération des données
            prenom = prenom.capitalize()
            nom = nom.upper()
            gendre = str(gendre).upper()
            email = str(email).lower()

            #lancement de la fonction
            modificationEtudiant(id_,prenom,nom,gendre,email)
            break

        if menu_choix == 3 :
            #récupération des données
            id_ = str(id_)
            
            #lancement de la fonction
            suppressionEtudiant(id_)
            break

        if menu_choix == 4 :
            affichageEtudiant() 


        if menu_choix == 5 :
            return 
