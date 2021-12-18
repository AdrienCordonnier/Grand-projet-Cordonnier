from fonctions import *

def sexe(var):
    """cette fonction permet de changer le sexe de l'étudiant
    par l'activation du bouton de l'interface graphique
    Il prend en entrée la variable du bouton sélectionné"""
    
    global gendre
    
    if (var.get() == 1):
        gendre = "F"
    else:
        gendre = "M"
        
###################################################################
#différentes variables utilisées
###################################################################

gendre = "M"
id_=0
prenom=""
nom=""
email=""
frame2=0
###################################################################
#Gestion de l'interface graphique
###################################################################
def main():
    global app
    app = tk.Tk()
    app.title("Gestion étudiants")
    app.geometry("1200x600-200-150")
    app.configure(bg = '#a0feff')

    label_gs = tk.Label(app,text="Gestion de scolarité",font=("Broadway", 35),
                        fg="red", bg="#a0feff",relief = 'ridge')
    label_gs.place(relx=0.25, rely=0.15,relwidth = 0.5 ,relheight = 0.12 )

    #création des boutons
    
    btn_gestion_etudiants = tk.Button(app, text="Gestion étudiants",
                                      font=("Calibri Light", 17),
                                      bg="#06a4fd",fg="#010000",
                                      command=lambda:main2())
    btn_gestion_etudiants.place(relx=0.15, rely=0.55, relwidth=0.3,
                                relheight=0.1)
    
    btn_gestion_notes = tk.Button(app, text="Gestion notes",
                                  font=("Calibri Light", 17),
                                  bg="#06a4fd",fg="#010000",
                                  command=lambda:main3())
    btn_gestion_notes.place(relx=0.55, rely=0.55, relwidth=0.3, relheight=0.1)

    btn_quitter = tk.Button(app, text="Quitter", font=("Calibri Light", 17),
                            bg="#06a4fd",fg="#010000",
                            command=lambda:quitter(app))
    btn_quitter.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.1)


def main2():
    var = 0
    var2 = 0
    global frame2
    app1 = tk.Toplevel(app)
    app1.title("gestion scolaire")
    app1.geometry("1200x600-200-150")

    Frame = tk.Frame(app1, bg="#a0feff")
    Frame.place(relwidth=1, relheight=1)

    frame2 = tk.Frame(Frame, bg="#a0feff", borderwidth=0, relief=tk.GROOVE)
    frame2.place(relx=0.3, rely=0.2, relwidth=0.69, relheight=0.78)

    frame = tk.Frame(Frame, bg="#a0feff", borderwidth=5, relief=tk.GROOVE)
    frame.place(relx=0.01, rely=0.03, relwidth=0.27, relheight=0.95)

    label_gestion = tk.Label(Frame,text="Gestion de scolarité",
                             font=("Brush Script MT", 35), fg="red",
                             bg="#a0feff")
    label_gestion.place(relx=0.50, rely=0.02 )

    label_etudiant = tk.Label(frame,text="Etudiant",font=("Brush Script MT", 30),
                              fg="red", bg="#a0feff")
    label_etudiant.place(relx=0.3, rely=0.02 )
    
    var = tk.IntVar()
    var2 = tk.IntVar()
    
    ##########################################################################
    #Ajout des boutons et zones de texte
    ##########################################################################
    
    label_id = tk.Label(frame, text="id :", bg="#a0feff",
                        font=('Calibri Light', 12),fg="grey")
    label_id.place(relx=0.04, rely=0.15, relwidth=0.18, relheight=0.05)
    id_ = tk.Entry(frame)
    id_.place(relx=0.3, rely=0.15, relwidth=0.6, relheight=0.05)
    id_.configure(state="disabled")
    
    label_nom = tk.Label(frame, text="Nom :", bg="#a0feff",
                         font=('Calibri Light', 12),fg="grey")
    label_nom.place(relx=0.04, rely=0.25, relwidth=0.18, relheight=0.05)
    nom = tk.Entry(frame)
    nom.place(relx=0.3, rely=0.25, relwidth=0.6, relheight=0.05)
    nom.configure(state="disabled")
    
    label_prenom = tk.Label(frame, text="Prénom :", bg="#a0feff",
                            font=('Calibri Light', 12),fg="grey")
    label_prenom.place(relx=0.04, rely=0.35, relwidth=0.2, relheight=0.05)
    prenom = (tk.Entry(frame))
    prenom.place(relx=0.3, rely=0.35, relwidth=0.6, relheight=0.05)
    prenom.configure(state="disabled")
    
    label_email = tk.Label(frame, text="Email :", bg="#a0feff",
                           font=('Calibri Light', 12),fg="grey")
    label_email.place(relx=0.04, rely=0.45, relwidth=0.18, relheight=0.05)
    textEntry1 = tk.StringVar()
    textEntry1.set("@ipsa.fr")
    email = tk.Entry(frame,textvariable = textEntry1)
    email.place(relx=0.3, rely=0.45, relwidth=0.6, relheight=0.05)
    email.configure(state="disabled")
    
    label_gendre = tk.Label(frame, text="Sexe :", bg="#a0feff",
                            font=('Calibri Light', 12),fg="grey")
    label_gendre.place(relx=0.04, rely=0.55, relwidth=0.18, relheight=0.05)

    case1 = tk.Radiobutton(frame, text="F", variable=var, value=1,
                           font=('Calibri Light', 12), bg="#a0feff",fg="#010000",
                           command=lambda:sexe(var),state="disabled")
    case1.place(relx=0.3, rely=0.55, relwidth=0.2, relheight=0.05)
    case2 = tk.Radiobutton(frame, text="M", variable=var, value=2,
                           font=('Calibri Light', 12), bg="#a0feff",fg="#010000",
                           command=lambda:sexe(var),state="disabled")                     
    case2.place(relx=0.55, rely=0.55, relwidth=0.2, relheight=0.05)

    label_attention = tk.Label(frame, text="Sélectionnez d'abord une option !",
                               bg="#a0feff", font=('Calibri Light ', 12,'bold'),
                               fg="red")
    label_attention.place(relx=0.02, rely=0.60, relwidth=0.96, relheight=0.05)
    
    btn_ajouter = tk.Radiobutton(frame, text="Ajouter", variable=var2, value=1,
                                 font=("Calibri Light", 12), bg="#a0feff",
                                 fg="#010000",
                                 command=lambda:activation_btn(label_id,id_,
                                                               label_nom,nom,
                                                               label_prenom,
                                                               prenom,
                                                               label_email,
                                                               email,
                                                               label_gendre
                                                               ,case1,case2,
                                                               label_attention,
                                                               var2))
    btn_ajouter.place(relx=0.1, rely=0.65, relwidth=0.3, relheight=0.05)
        
    btn_modifier = tk.Radiobutton(frame, text="Modifier", variable=var2,
                                  value=2,
                                  font=("Calibri Light", 12), bg="#a0feff",
                                  fg="#010000",
                                  command=lambda:activation_btn(label_id,id_,
                                                                label_nom,nom,
                                                                label_prenom,
                                                                prenom,
                                                                label_email,
                                                                email,
                                                                label_gendre,
                                                                case1,case2,
                                                                label_attention
                                                                ,var2))
    btn_modifier.place(relx=0.5, rely=0.65, relwidth=0.3, relheight=0.05)

    btn_supprimer = tk.Radiobutton(frame, text="Supprimer", variable=var2,
                                   value=3, font=("Calibri Light", 12),
                                   bg="#a0feff",fg="#010000",
                                   command=lambda:activation_btn(label_id,id_,
                                                                 label_nom,nom,
                                                                 label_prenom,
                                                                 prenom,
                                                                 label_email,
                                                                 email,
                                                                 label_gendre,
                                                                 case1,case2,
                                                                 label_attention
                                                                 ,var2))
    btn_supprimer.place(relx=0.1, rely=0.75, relwidth=0.3, relheight=0.05)

    btn_valider = tk.Button(frame, text="Valider",
                            font=("Calibri Light", 12,'bold'),
                            bg="#a0feff",fg="#00CC66",
                            command=lambda:valider(nom, prenom, gendre, email,
                                                   id_,var2,frame2))
    btn_valider.place(relx=0.1, rely=0.85, relwidth=0.3, relheight=0.05)
    
    btn_reset = tk.Button(frame, text="effacer",
                          font=("Calibri Light", 12), fg="red", bg="#a0feff",
                          command=lambda:clear(nom, prenom,email,id_))
    btn_reset.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.05)

    ##########################################################################
    #Affichage des données
    ##########################################################################
    tableau(frame2)
    

    app.mainloop()

def main3():
    var = 0
    var2 = 0
    global frame2
    app1 = tk.Toplevel(app)
    app1.title("gestion scolaire")
    app1.geometry("1200x600-200-150")
    
    Frame = tk.Frame(app1, bg="#a0feff")
    Frame.place(relwidth=1, relheight=1)

    frame2 = tk.Frame(Frame, bg="#a0feff", borderwidth=0, relief=tk.GROOVE)
    frame2.place(relx=0.3, rely=0.2, relwidth=0.69, relheight=0.78)

    frame = tk.Frame(Frame, bg="#a0feff", borderwidth=5, relief=tk.GROOVE)
    frame.place(relx=0.01, rely=0.03, relwidth=0.27, relheight=0.95)

    label_gestion = tk.Label(Frame,text="Gestion de notes",
                             font=("Brush Script MT", 35),
                             fg="red", bg="#a0feff")
    label_gestion.place(relx=0.50, rely=0.02 )

    label_etudiant = tk.Label(frame,text="Etudiant",
                              font=("Brush Script MT", 30),
                              fg="red", bg="#a0feff")
    label_etudiant.place(relx=0.3, rely=0.02 )
    
    var = tk.IntVar()
    var2 = tk.IntVar()
    
    ##########################################################################
    #Ajout des boutons et zones de texte
    ##########################################################################
    
    label_id = tk.Label(frame, text="id :", bg="#a0feff",
                        font=('Calibri Light', 12),fg="grey")
    label_id.place(relx=0.04, rely=0.15, relwidth=0.18, relheight=0.05)
    id_ = tk.Entry(frame)
    id_.place(relx=0.3, rely=0.15, relwidth=0.6, relheight=0.05)
    id_.configure(state="disabled")
    
    label_annee = tk.Label(frame, text="Année :", bg="#a0feff",
                           font=('Calibri Light', 12),fg="grey")
    label_annee.place(relx=0.04, rely=0.25, relwidth=0.18, relheight=0.05)
    textEntry = tk.StringVar()
    textEntry.set("2021/2022")
    annee = ttk.Combobox(frame,values=[
                                          "2021/2022",
                                          "2020/2021",
                                          "2019/2020",
                                          "2018/2019",
                                          "2017/2018",
                                          "2016/2017",
                                          "2015/2016",
                                          "2014/2015"],
                                          state="readonly")
    annee.grid(column = 0,row = 1)
    annee.current(0)
    annee.place(relx=0.3, rely=0.25, relwidth=0.6, relheight=0.05)
    annee.configure(state="disabled")
    
    label_matiere = tk.Label(frame, text="matière :", bg="#a0feff",
                             font=('Calibri Light', 12),fg="grey")
    label_matiere.place(relx=0.04, rely=0.35, relwidth=0.2, relheight=0.05)
    matiere = ttk.Combobox(frame,values=[
                                          "Mathematique",
                                          "Aeronotique",
                                          "Informatique",
                                          "Anglais",
                                          "Electronique",
                                          "Physique",
                                          "Mecanique",
                                          "Grand Projet"],
                                          state = "readonly")
    matiere.grid(column = 0,row = 1)
    matiere.current(0)
    matiere.place(relx=0.3, rely=0.35, relwidth=0.6, relheight=0.05)
    matiere.configure(state="disabled")
    
    label_note = tk.Label(frame, text="Note :", bg="#a0feff",
                          font=('Calibri Light', 12),fg="grey")
    label_note.place(relx=0.04, rely=0.45, relwidth=0.18, relheight=0.05)
    note = tk.Entry(frame)
    note.place(relx=0.3, rely=0.45, relwidth=0.6, relheight=0.05)
    note.configure(state="disabled")
    
    label_attention = tk.Label(frame, text="Sélectionnez d'abord une option !",
                               bg="#a0feff", font=('Calibri Light ', 12,'bold')
                               ,fg="red")
    label_attention.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.05)
    
    btn_ajouter = tk.Radiobutton(frame, text="Ajouter", variable=var2, value=1,
                                 font=("Calibri Light", 12), bg="#a0feff",
                                 fg="#010000",
                                 command=lambda:activation_btn1(label_id,
                                                                id_,
                                                                label_annee,
                                                                annee,
                                                                label_matiere,
                                                                matiere,
                                                                label_note,note
                                                                ,label_attention
                                                                ,var2))
    btn_ajouter.place(relx=0.1, rely=0.65, relwidth=0.3, relheight=0.05)
        
    btn_modifier = tk.Radiobutton(frame, text="Modifier", variable=var2,
                                  value=2, font=("Calibri Light", 12),
                                  bg="#a0feff",fg="#010000",
                                  command=lambda:activation_btn1(label_id,id_,
                                                                 label_annee,
                                                                 annee,
                                                                 label_matiere,
                                                                 matiere,
                                                                 label_note,
                                                                 note,
                                                                 label_attention
                                                                 ,var2))
    btn_modifier.place(relx=0.5, rely=0.65, relwidth=0.3, relheight=0.05)

    btn_supprimer = tk.Radiobutton(frame, text="Supprimer", variable=var2,
                                   value=3, font=("Calibri Light", 12),
                                   bg="#a0feff",fg="#010000",
                                   command=lambda:activation_btn1(label_id,
                                                                  id_,label_annee
                                                                  ,annee,
                                                                  label_matiere,
                                                                  matiere,
                                                                  label_note,
                                                                  note,
                                                                  label_attention,
                                                                  var2))
    btn_supprimer.place(relx=0.1, rely=0.75, relwidth=0.3, relheight=0.05)

    btn_valider = tk.Button(frame, text="Valider",
                            font=("Calibri Light", 12,'bold'),
                            bg="#a0feff",fg="#00CC66",
                            command=lambda:valider1(id_, annee,
                                                    matiere,
                                                    note,var2,frame2))
    btn_valider.place(relx=0.1, rely=0.85, relwidth=0.3, relheight=0.05)
    
    btn_reset = tk.Button(frame, text="effacer", font=("Calibri Light", 12),
                          fg="red", bg="#a0feff",
                          command=lambda:clear1(id_ ,annee, matiere, note))
    btn_reset.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.05)

    ##########################################################################
    #Affichage des données
    ##########################################################################
    tableau2(frame2)

    
