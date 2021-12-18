import tkinter as tk
import lib_gestionEtudiants as ge
from lib_gestionEtudiants import gestionEtudiants
from lib_gestionNotes import gestionNotes
from tkinter import ttk
import lib_commun as lib
from tkinter import messagebox
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv

def clear(txt1,txt2,txt3,txt4):
    """cette fonction permet de supprimer les entrées de l'interface
    graphique pour la gestion des étudiants.
    
    Elle prend en parametre les entrées à supprimer"""
    
    txt1.delete(0,tk.END)
    txt2.delete(0,tk.END)
    txt3.delete(0,tk.END)
    txt4.delete(0,tk.END)
    
def clear1(txt1,txt2,txt3,txt4):
    """cette fonction permet de supprimer les entrées de l'interface
    graphique pour la gestion des notes.
    
    Elle prend en parametre les entrées à supprimer"""
    
    txt1.delete(0,tk.END)
    txt4.delete(0,tk.END)
    
def create_new_window():
    new_window = tk.Toplevel(app)
    
    
def tableau(frame):
    """cette fonction permet l'affichage du tableau des étudiants.

    Elle prend en parametre la fenetre dans laquelle doit etre affiché
    le tableau"""
    #Ajout du nombre de colonnes
    columns = ('#1', '#2', '#3', '#4', '#5')

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                    font=('Arial', 10))
    style.configure("mystyle.Treeview.Heading",
                    font=('Calibri Light', 12))
    tree = ttk.Treeview(frame,columns=columns, show='headings',
                        style="mystyle.Treeview",height = 20)

    #Ajout du nom et de la taille des colonnes
    tree.heading('#1', text='ID')
    tree.column('#1',minwidth=0,width=100) 
    tree.heading('#2', text='Sexe')
    tree.column('#2',minwidth=0,width=100)
    tree.heading('#3', text='Nom')
    tree.column('#3',minwidth=0,width=180)
    tree.heading('#4', text='Prénom')
    tree.column('#4',minwidth=0,width=150)
    tree.heading('#5', text='Email')
    tree.column('#5',minwidth=0,width=250)

    #Formation du tableau
    f = lib.ouverture_fichier_csv("etudiants.csv")
    
    for contact in f[1:]:
        tree.insert('', tk.END, values=contact)
        
    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']

    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.grid(row=0, column=0, sticky='s')

    #Ajout de la scrollbar
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')


def tableau2(frame):
    """cette fonction permet l'affichage du tableau des notes.

    Elle prend en parametre la fenetre dans laquelle doit etre
    affiché le tableau"""

    #Ajout des colonnes
    columns = ('#1', '#2', '#3', '#4', '#5')

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                    font=('Arial', 10))
    style.configure("mystyle.Treeview.Heading",
                    font=('Calibri Light', 12))
    tree = ttk.Treeview(frame,columns=columns, show='headings',
                        style="mystyle.Treeview",height = 20)

    #Ajout du nom et de la taille des colonnes 
    tree.heading('#1', text='ID')
    tree.column('#1',minwidth=0,width=100) 
    tree.heading('#2', text='Année')
    tree.column('#2',minwidth=0,width=100)
    tree.heading('#3', text='Id étudiant')
    tree.column('#3',minwidth=0,width=180)
    tree.heading('#4', text='Matière')
    tree.column('#4',minwidth=0,width=150)
    tree.heading('#5', text='Note')
    tree.column('#5',minwidth=0,width=250)

    #formation du tableau
    f = lib.ouverture_fichier_csv("notes.csv")
    
    for contact in f[1:]:
        tree.insert('', tk.END, values=contact)


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']

    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.grid(row=0, column=0, sticky='s')

    #Ajout de la scrollbar
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL,
                              command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    
########################################################################
#Fonctions qui permettent de lancer la bonne fonction de la gestion d'étudiants
#(supprimer, ajouter ou modifier)
########################################################################
    
def menu_choix1(nom, prenom, gendre, email,id_,var):
    menu_choix=1
    nom = nom.get()
    var = var.get()
    prenom = prenom.get()
    email = email.get()
    id_ = id_.get()
    gestionEtudiants(id_,menu_choix,prenom,nom,gendre,email)

def menu_choix2(nom, prenom, gendre, email,id_,var):
    #récupération des données
    
    menu_choix=2
    nom = nom.get()
    prenom = prenom.get()
    email = email.get()
    id_ = id_.get()
    var = var.get()

    #lancement de la fonction avec les nouvelles données
    
    gestionEtudiants(id_,menu_choix,prenom,nom,gendre,email)

def menu_choix3(nom, prenom, gendre, email,id_,var):
    #récupération des données
    
    menu_choix=3
    nom = nom.get()
    prenom = prenom.get()
    email = email.get()
    id_ = id_.get()
    
    #lancement de la fonction avec les nouvelles données 
    
    gestionEtudiants(id_,menu_choix,prenom,nom,gendre,email)
    f = ouverture_fichier_csv("notes.csv")
    a = 1
    b = 0

    #suppression des notes de l'étudiant supprimé
    
    for i in f[1:]:
        a = a + 1
        if i[2] == id_ :
            b = b + 1
            f.pop(a-b)
            
    ecriture_fichier_csv(f,"notes.csv",'w')
    return

########################################################################
#Fonctions qui permettent de lancer la bonne fonction de la gestion de notes
#(supprimer, ajouter ou modifier)
########################################################################

def menu_choix1_2(id_,annee,matiere,note,var):
    #récupération des nouvelles données
    
    menu_choix=1
    annee = annee.get()
    var = var.get()
    matiere = matiere.get()
    note = note.get()
    id_ = id_.get()

    #lancement de la fonction avec les nouvelles données
    
    gestionNotes(id_,menu_choix,annee,matiere,note)

def menu_choix2_2(id_,annee,matiere,note,var):
    #récupération des nouvelles données
    
    menu_choix=2
    annee = annee.get()
    var = var.get()
    matiere = matiere.get()
    note = note.get()
    id_ = id_.get()

    #lancement de la fonction avec les nouvelles données
    
    gestionNotes(id_,menu_choix,annee,matiere,note)

def menu_choix3_2(id_,annee,matiere,note,var):
    #récupération des nouvelles données
    
    menu_choix=3
    annee = annee.get()
    var = var.get()
    matiere = matiere.get()
    note = note.get()
    id_ = id_.get()

    #lancement de la fonction avec les nouvelles données
    
    gestionNotes(id_,menu_choix,annee,matiere,note)

def quitter(frame):
    """cette fonction permet de quitter la fenetre graphique
    elle prend en parametre la fenetre que l'on souhaite fermer"""
    
    msg = tk.messagebox.askquestion("Quitter"
                                    ,"Voulez-vous vraiment quitter ?")
    if msg == 'yes':
        frame.destroy()

###############################################################################
#Boutons qui permettent de lancer les bonnes fonctions de la gestion de scolarité
###############################################################################

def valider(nom, prenom, gendre, email,id_,var,frame):
    """cette fonction permet de faire fonctionner le bouton "valider" et
    lancer les bonnes fonctions en fonction des variables.
    
    Elle prend en entrée les nouvelles variables que l'utiliseur entre
    dans l'interface graphique ainsi que la variable du bouton"""

    if (var.get() == 1):
        menu_choix1(nom, prenom, gendre, email,id_,var)
        tableau(frame)
        
    elif (var.get() == 2):
        menu_choix2(nom, prenom, gendre, email,id_,var)
        tableau(frame)
        
    elif (var.get() == 3):
        menu_choix3(nom, prenom, gendre, email,id_,var)
        tableau(frame)
        clear(nom, prenom,email,id_)
    else:
        
        return

def valider1(id_, annee, matiere, note,var,frame):
    """cette fonction permet de faire fonctionner le bouton "valider" et
    lancer les bonnes fonctions en fonction des variables.
    
    Elle prend en entrée les nouvelles variables que l'utiliseur entre
    dans l'interface graphique ainsi que la variable du bouton"""

    if (var.get() == 1):
        menu_choix1_2(id_,annee,matiere,note,var)
        tableau2(frame)

    elif (var.get() == 2):
        menu_choix2_2(id_,annee,matiere,note,var)
        tableau2(frame)
        clear1(id_,annee,matiere,note)
    elif (var.get() == 3):
        menu_choix3_2(id_,annee,matiere,note,var)
        tableau2(frame)
        clear1(id_,annee,matiere,note)
    else:
        
        return
    
#############################################################################
#Activation ou désactivation des boutons et entrées de l'interface graphique
#############################################################################

def activation_btn(a,b,c,d,e,f,g,h,i,j,k,l,var):
    """cette fonction permet d'activer ou de désactiver les différents
    boutons de l'interface de la gestion d'étudiant et labels de
    l'interface graphique selon l'option de gestion qi est sélectionnée.
    
    Elle prend en argument les labels ou entrées sont on veut changer
    l'état et la variable du bouton sélectionné"""
    
    if (var.get() == 1):
        a.configure(fg="grey")
        b.configure(state="disabled")
        c.configure(fg="#010000")
        d.configure(state="normal")
        e.configure(fg="#010000")
        f.configure(state="normal")
        g.configure(fg="#010000")
        h.configure(state="normal")
        i.configure(fg="#010000")
        j.configure(state="normal")
        k.configure(state="normal")
        l.configure(fg='#a0feff')
    elif (var.get() == 2):
        a.configure(fg="#010000")
        b.configure(state="normal")
        c.configure(fg="#010000")
        d.configure(state="normal")
        e.configure(fg="#010000")
        f.configure(state="normal")
        g.configure(fg="#010000")
        h.configure(state="normal")
        i.configure(fg="#010000")
        j.configure(state="normal")
        k.configure(state="normal")
        l.configure(fg='#a0feff')
    else:
        a.configure(fg="#010000")
        b.configure(state="normal")
        c.configure(fg="grey")
        d.configure(state="disabled")
        e.configure(fg="grey")
        f.configure(state="disabled")
        g.configure(fg="grey")
        h.configure(state="disabled")
        i.configure(fg="grey")
        j.configure(state="disabled")
        k.configure(state="disabled")
        l.configure(fg='#a0feff')

def activation_btn1(a,b,c,d,e,f,g,h,i,var):
    """cette fonction permet d'activer ou de désactiver les différents
    boutons de l'interface de la gestion d'étudiant et labels de
    l'interface graphique selon l'option de gestion qi est sélectionnée.
    
    Elle prend en argument les labels ou entrées sont on veut changer
    l'état et la variable du bouton sélectionné"""
    
    if (var.get() == 1):
        a.configure(text="id de l'étudiant :",fg="#010000")
        a.place(relx=0.04, rely=0.15, relwidth=0.33, relheight=0.05)
        b.place(relx=0.45, rely=0.15, relwidth=0.45, relheight=0.05)
        b.configure(state="normal")
        c.configure(fg="#010000")
        d.configure(state="normal")
        e.configure(fg="#010000")
        f.configure(state="normal")
        g.configure(fg="#010000")
        h.configure(state="normal")
        i.configure(fg='#a0feff')
    elif (var.get() == 2):
        a.configure(text="id de la note :",fg="#010000")
        a.place(relx=0.04, rely=0.15, relwidth=0.3, relheight=0.05)
        b.place(relx=0.45, rely=0.15, relwidth=0.45, relheight=0.05)
        b.configure(state="normal")
        c.configure(fg="grey")
        d.configure(state="disabled")
        e.configure(fg="grey")
        f.configure(state="disabled")
        g.configure(fg="#010000")
        h.configure(state="normal")
        i.configure(fg='#a0feff')
    else:
        a.configure(text="id de la note :",fg="#010000")
        a.place(relx=0.04, rely=0.15, relwidth=0.3, relheight=0.05)
        b.place(relx=0.45, rely=0.15, relwidth=0.45, relheight=0.05)
        b.configure(state="normal")
        c.configure(fg="grey")
        d.configure(state="disabled")
        e.configure(fg="grey")
        f.configure(state="disabled")
        g.configure(fg="grey")
        h.configure(state="disabled")
        i.configure(fg='#a0feff')
