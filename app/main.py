import tkinter as tk
# import fonctionSQL as fn
import hashlib
import mysql.connector
################################################################
if __name__=='__main__':


    global win2, connec, bdd, utilisateur, id_utilisateur
    bdd = mysql.connector.connect(host="localhost",port=3308,user="root",passwd="",database="stephiplace_data_2")
    connec = False
    utilisateur = None
    id_utilisateur=None


    ###############################################################
    ############### Fenetre principale ############################
    ###############################################################
    winMain = tk.Tk()
    winMain.title('Stephiplace')
    screen_x = int(winMain.winfo_screenwidth())
    screen_y = int(winMain.winfo_screenheight())
    window_x = 1024
    window_y = 800
    posX = (screen_x // 2) - (window_x // 2)
    posY = (screen_y // 2) - (window_y // 2)
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    winMain.geometry(geo)

    ###############################################################
    ############### Popup Connexion ###############################
    ###############################################################
    def fenetreConnexion():
        global win2,entreIdentifiant,entreMDP
        win2 = tk.Toplevel(winMain)
        win2.title("Stephiplace - Connexion")
        identifiant = tk.Label(win2, text="Identifiant")
        entreIdentifiant = tk.Entry(win2, width=30)
        MDP = tk.Label(win2, text="Mot de passe")
        entreMDP = tk.Entry(win2, show='*', width=30)
        btnExit = tk.Button(win2, text="Quitter",bg='#CE117B',fg='#fff', activeforeground='#CE117B',width=17, command=quitter)
        btnConnect = tk.Button(win2, text="Se Connecter",bg='#CE117B',fg='#fff', activeforeground='#CE117B',width=17, command=connexion)
        identifiant.grid(row=0,column=0)
        entreIdentifiant.grid(row=0,column=1,columnspan=2)
        MDP.grid(row=1,column=0)
        entreMDP.grid(row=1,column=1,columnspan=2)
        btnConnect.grid(row=2,column=0)
        btnExit.grid(row=2,column=3)
        screen_x = int(win2.winfo_screenwidth())
        screen_y = int(win2.winfo_screenheight())
        window_x = 550
        window_y = 400
        posX = (screen_x // 2) - (window_x // 2)
        posY = (screen_y // 2) - (window_y // 2)
        geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
        win2.geometry(geo)



    ###############################################################
    #################### Fenetre du menu ##########################
    ###############################################################
    def fenetreMenu():
        # winMenu = tk.Frame(winMain,width=800, height=700)
        global listeAnnonce, utilisateur,listeAgent
        menubar = tk.Menu(winMain) 
        winAnnonce = tk.Label(winMain)
        winAgent = tk.Label(winMain)
        winMain.config(menu=menubar)
        menuCommand = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Action", menu=menuCommand)
        menuCommand.add_command(label="Rafraichir", command=winAnnonce.update)
        menuCommand.add_command(label="register", command=fenetreEntregistrer)
        menuCommand.add_separator()
        menuCommand.add_command(label="Quitter", command=winMain.destroy)
        nomUtilisateur = tk.Label(winMain,text="Bonjours "+utilisateur)
        listeAnnonce = tk.Listbox(winAnnonce,width=65)
        listeAgent = tk.Listbox(winAgent,width=80)
        btnAjouterAgent=tk.Button(winAgent,text="Ajouter", command=fenetreEntregistrer)
        btnModifAgent=tk.Button(winAgent,text="Modifier", command=None)
        btnDeleteAgent=tk.Button(winAgent,text="Supprimer", command=suppAgent)
        btnAjouterAnnonce=tk.Button(winAnnonce,text="Ajouter", command=fenetreAjouter)
        btnModifAnnonce=tk.Button(winAnnonce,text="Modifier", command=modifAnnonce)
        btnDeleteAnnonce=tk.Button(winAnnonce,text="Supprimer", command=suppAnnonce)
        myCursor = bdd.cursor()
        myCursor.execute("""SELECT bien_id,bien_nom,bien_ville,bien_codePostal,bien_type FROM bien""")
        lines = myCursor.fetchall()
        for line in lines:
            listeAnnonce.insert(tk.END, "{} {} {} {} {}".format(line[0],line[1],line[2],line[3],line[4]))
        myAgent = bdd.cursor()
        myAgent.execute("""SELECT a.utilisateurs_id,u.utilisateur_nom, u.utilisateur_prenom, u.utilisateur_mail, u.utilisateur_tel, ag.agence_nom FROM agent AS a INNER JOIN utilisateurs AS u ON u.utilisateurs_id = a.utilisateurs_id INNER JOIN agence AS ag ON ag.agence_id = a.agence_id""")
        linesAgent = myAgent.fetchall()
        for agent in linesAgent:
            listeAgent.insert(tk.END, "{} {} {} {} {} {}".format(agent[0],agent[1],agent[2],agent[3],agent[4], agent[5]))
        winAgent.grid(row=1, column=2)
        listeAgent.grid(row=0,column=0,columnspan=3)
        btnAjouterAgent.grid(row=1,column=0)
        btnModifAgent.grid(row=1,column=1)
        btnDeleteAgent.grid(row=1,column=2)
        nomUtilisateur.grid(row=0,column=1)
        winAnnonce.grid(row=1,column=0)
        listeAnnonce.grid(row=0,column=0,columnspan=3)
        btnAjouterAnnonce.grid(row=1,column=0)
        btnModifAnnonce.grid(row=1,column=1)
        btnDeleteAnnonce.grid(row=1,column=2)



    ###############################################################
    ##################### Fenetre modifier ########################
    ###############################################################
    def fenetreEntregistrer():
        global entreName,entreFirstname,entreStatus,entreMDP,entreAge,entreAdresse,entreVille,entreCodePostal,entreImg,entreTel,entreDescription,entreGenre,entreMail,winregister,listeAgence
        winregister = tk.Toplevel(winMain)
        labelName = tk.Label(winregister,text="Nom: ")
        entreName = tk.Entry(winregister)
        labelFirstname = tk.Label(winregister,text="Prénom: ")
        entreFirstname = tk.Entry(winregister)
        labelMDP=tk.Label(winregister, text="Mot de passe: ")
        entreMDP=tk.Entry(winregister)
        labelAge=tk.Label(winregister, text="Age: ")
        entreAge=tk.Entry(winregister)
        labelMail=tk.Label(winregister, text="Mail: ")
        entreMail=tk.Entry(winregister)
        labelAdresse=tk.Label(winregister, text="Adresse: ")
        entreAdresse=tk.Entry(winregister)
        labelVille=tk.Label(winregister, text="Ville: ")
        entreVille=tk.Entry(winregister)
        labelCodePostal=tk.Label(winregister, text="Code postal: ")
        entreCodePostal=tk.Entry(winregister)
        labelImg=tk.Label(winregister, text="Image profil: ")
        valImg = tk.StringVar(winregister)
        valImg.set("/default_user.png")
        entreImg=tk.Entry(winregister, textvariable=valImg)
        labelStatus = tk.Label(winregister,text="Status: ")
        valStatus = tk.StringVar(winregister)
        valStatus.set("agent")
        entreStatus = tk.Entry(winregister,textvariable=valStatus)
        labelTel = tk.Label(winregister,text="Telephone: ")
        entreTel = tk.Entry(winregister)
        labelDescription=tk.Label(winregister, text="Description: ")
        entreDescription=tk.Entry(winregister)
        labelGenre=tk.Label(winregister, text="Civilité: ")
        entreGenre=tk.Entry(winregister)
        LabelAgence = tk.Label(winregister, text="Agence associer au bien")
        listeAgence = tk.Listbox(winregister, width=45, height=5)
        myCursor = bdd.cursor()
        myCursor.execute("""SELECT agence_id, agence_nom, agence_codePostal FROM agence""")
        lines = myCursor.fetchall()
        for line in lines:
            listeAgence.insert(tk.END, "{} {} {},{}".format(line[0],"Agence de",line[1],line[2]))
        btnConfirm = tk.Button(winregister, text="Confimer",bg='#CE117B',command=enregister)
        labelName.grid(row=0,column=0)
        entreName.grid(row=0,column=1)
        LabelAgence.grid(row=0,column=5)
        labelFirstname.grid(row=1,column=0)
        entreFirstname.grid(row=1,column=1)
        listeAgence.grid(row=1, column=5, rowspan=2)
        labelMDP.grid(row=2,column=0)
        entreMDP.grid(row=2,column=1)
        labelAge.grid(row=3,column=0)
        entreAge.grid(row=3,column=1)
        labelAdresse.grid(row=4,column=0)
        entreAdresse.grid(row=4,column=1)
        labelVille.grid(row=5,column=0)
        entreVille.grid(row=5,column=1)
        labelCodePostal.grid(row=6,column=0)
        entreCodePostal.grid(row=6,column=1)
        labelImg.grid(row=7,column=0)
        entreImg.grid(row=7,column=1)
        labelTel.grid(row=8,column=0)
        entreTel.grid(row=8,column=1)
        labelStatus.grid(row=9,column=0)
        entreStatus.grid(row=9,column=1)
        labelDescription.grid(row=10,column=0)
        entreDescription.grid(row=10,column=1)
        labelGenre.grid(row=11,column=0)
        entreGenre.grid(row=11,column=1)
        labelMail.grid(row=12,column=0)
        entreMail.grid(row=12,column=1)
        btnConfirm.grid(row=13,column=0, columnspan=4)
        winregister.geometry("600x350")



    ###############################################################
    ##################### Fenetre modifier ########################
    ###############################################################
    def fenetreAjouter():
        global bdd,entreTitre,entreAdresse,entreCodePostal,entreVille,entreSurface,entreDescription,labelType,entreType,var1,var2,var3,var4,var5,entreType,entrePiece,listeClient,entreImg,entrePrix,fenAjout
        fenAjout = tk.Toplevel(winMain)
        fenAjout.title('Ajouter annonce')
        labelTitre = tk.Label(fenAjout,text="Titre annonce")
        entreTitre = tk.Entry(fenAjout)        
        labelAdresse = tk.Label(fenAjout,text="Adresse annonce")
        entreAdresse = tk.Entry(fenAjout)
        labelCodePostal = tk.Label(fenAjout,text="Code postal annonce")
        entreCodePostal = tk.Entry(fenAjout)
        labelVille = tk.Label(fenAjout,text="Ville annonce")
        entreVille = tk.Entry(fenAjout)
        labelPrix = tk.Label(fenAjout,text="Prix annonce")
        entrePrix = tk.Entry(fenAjout)
        labelPiece = tk.Label(fenAjout,text="Nombre de pièces:")
        entrePiece = tk.Entry(fenAjout)
        labelSurface = tk.Label(fenAjout,text="Surface en m² annonce")
        entreSurface = tk.Entry(fenAjout)
        labelImg = tk.Label(fenAjout,text="Images annonce")
        entreImg = tk.Entry(fenAjout)
        labelIndicationSurface = tk.Label(fenAjout, text="m²")
        labelDescription = tk.Label(fenAjout,text="Description")
        entreDescription = tk.Entry(fenAjout)
        btnConfirm = tk.Button(fenAjout, text="Confimer", command=ajouterAnnonce)
        labelType = tk.Label(fenAjout, text="Type de bien: ")
        entreType = tk.Entry(fenAjout)
        LabelClient = tk.Label(fenAjout, text="Client associer au bien")
        listeClient = tk.Listbox(fenAjout, width=45, height=5)
        tabId = []
        tabNomDep = []
        cadreDependance = tk.Frame(fenAjout)
        myCursor = bdd.cursor()
        myCursor.execute("""SELECT c.client_id, u.utilisateur_nom, u.utilisateur_prenom, u.utilisateur_mail FROM client AS c INNER JOIN utilisateurs AS u WHERE c.utilisateurs_id =u.utilisateurs_id""")
        lines = myCursor.fetchall() #On ajoute X ligne dans la liste des clients pour indiquer a l'agent le nom prénom et identifiant de du client qui selectionne
        for line in lines:
            listeClient.insert(tk.END, "{} {} {} {}".format(line[0],line[1],line[2],line[3]))
        myCursor.execute("""SELECT dependance_id, dependance_nom FROM dependance""")
        rows = myCursor.fetchall() #On récupère identifiant et nom de l'indépendance
        for row in rows:
            tabId.append(row[0])
            tabNomDep.append(row[1]) #Puis dans deux tableaux a chacun on ajoute leurs donnée respectif
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var4 = tk.IntVar()
        var5 = tk.IntVar()
        checkDep1 = tk.Checkbutton(cadreDependance, text=tabNomDep[0], variable=var1, onvalue=tabId[0])# on séléctionne la bonne donnée a insérer dans une checkbox où cette dernière sera prise en compte si l'agent coche la case
        checkDep2 = tk.Checkbutton(cadreDependance, text=tabNomDep[1], variable=var2, onvalue=tabId[1])# on séléctionne la bonne donnée a insérer dans une checkbox où cette dernière sera prise en compte si l'agent coche la case
        checkDep3 = tk.Checkbutton(cadreDependance, text=tabNomDep[2], variable=var3, onvalue=tabId[2])# on séléctionne la bonne donnée a insérer dans une checkbox où cette dernière sera prise en compte si l'agent coche la case
        checkDep4 = tk.Checkbutton(cadreDependance, text=tabNomDep[3], variable=var4, onvalue=tabId[3])# on séléctionne la bonne donnée a insérer dans une checkbox où cette dernière sera prise en compte si l'agent coche la case
        checkDep5 = tk.Checkbutton(cadreDependance, text=tabNomDep[4], variable=var5, onvalue=tabId[4])# on séléctionne la bonne donnée a insérer dans une checkbox où cette dernière sera prise en compte si l'agent coche la case
        fenAjout.geometry("600x350")
        checkDep1.grid(row=0, column=0)
        checkDep2.grid(row=0, column=1)
        checkDep3.grid(row=0, column=2)
        checkDep4.grid(row=1, column=0)
        checkDep5.grid(row=1, column=1)
        labelTitre.grid(row=0, column=0)
        entreTitre.grid(row=0, column=1)
        LabelClient.grid(row=0, column=5)
        labelAdresse.grid(row=1, column=0)
        entreAdresse.grid(row=1, column=1)
        listeClient.grid(row=1, column=5, rowspan=2)
        labelCodePostal.grid(row=2, column=0)
        entreCodePostal.grid(row=2, column=1)
        labelVille.grid(row=3,column=0)
        entreVille.grid(row=3,column=1)
        labelVille.grid(row=3, column=0)
        entreVille.grid(row=3, column=1)
        labelImg.grid(row=4,column=0)
        entreImg.grid(row=4,column=1)
        labelPrix.grid(row=5,column=0)
        entrePrix.grid(row=5,column=1)
        labelPiece.grid(row=6,column=0)
        entrePiece.grid(row=6,column=1)
        labelSurface.grid(row=7, column=0)
        entreSurface.grid(row=7, column=1)
        cadreDependance.grid(row=5, column=5, rowspan=2)
        labelIndicationSurface.grid(row=7, column=4)
        labelType.grid(row=8, column=0)
        entreType.grid(row=8, column=1)
        labelDescription.grid(row=9, column=0)
        entreDescription.grid(row=9, column=1)
        btnConfirm.grid(row=10,column=4)



    def fenetreModifAnnonce():
        global entreTitreModif,entreAdresseModif,entreCodePostalModif,entreVilleModif,entrePrixModif,entrePieceModif,entreSurfaceModif,entreImgModif,entreDescriptionModif,bienID,bdd,entreAffichage,entreType,fenModifAnnonce
        annonceModif = bdd.cursor()
        annonceModif.execute("""SELECT * FROM bien WHERE bien_id = %s""",(bienID, ))
        line = annonceModif.fetchone()
        varModifTitre = tk.StringVar()
        varModifTitre.set(line[1]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifAdresse = tk.StringVar()
        varModifAdresse.set(line[3]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifCodePostal = tk.StringVar()
        varModifCodePostal.set(line[4]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifVille = tk.StringVar()
        varModifVille.set(line[5]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifPrix = tk.StringVar()
        varModifPrix.set(line[6]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifPiece = tk.StringVar()
        varModifPiece.set(line[8]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifSurface = tk.StringVar()
        varModifSurface.set(line[7]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifImg = tk.StringVar()
        varModifImg.set(line[2]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifDescription = tk.StringVar()
        varModifDescription.set(line[9]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifAffichage = tk.StringVar()
        varModifAffichage.set(line[10]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        varModifType = tk.StringVar()
        varModifType.set(line[11]) # On récupère la donnée via l'id contenue dans la liste du menu et on insère la donnée associer a cette identifiant dans une valeur qui sera lu dans un input pour que l'agent puisse modifier la donnée qu'il veut
        fenModifAnnonce = tk.Toplevel(winMain)
        labelTitreModif = tk.Label(fenModifAnnonce,text="Titre: ")
        entreTitreModif = tk.Entry(fenModifAnnonce,textvariable=varModifTitre)
        labelAdresseModif = tk.Label(fenModifAnnonce,text="Adresse: ")
        entreAdresseModif = tk.Entry(fenModifAnnonce,textvariable=varModifAdresse)
        labelCodePostalModif = tk.Label(fenModifAnnonce,text="Code postal: ")
        entreCodePostalModif = tk.Entry(fenModifAnnonce,textvariable=varModifCodePostal)
        labelVilleModif = tk.Label(fenModifAnnonce,text="Ville: ")
        entreVilleModif = tk.Entry(fenModifAnnonce,textvariable=varModifVille)
        labelPrixModif = tk.Label(fenModifAnnonce,text="Prix: ")
        entrePrixModif = tk.Entry(fenModifAnnonce,textvariable=varModifPrix)
        labelPieceModif = tk.Label(fenModifAnnonce,text="nombre de pièces: ")
        entrePieceModif = tk.Entry(fenModifAnnonce,textvariable=varModifPiece)
        labelSurfaceModif = tk.Label(fenModifAnnonce,text="Surface: ")
        entreSurfaceModif = tk.Entry(fenModifAnnonce,textvariable=varModifSurface)
        labelImgModif = tk.Label(fenModifAnnonce,text="Image de l'annonce: ")
        entreImgModif = tk.Entry(fenModifAnnonce,textvariable=varModifImg)
        labelIndicationSurfaceModif = tk.Label(fenModifAnnonce,text="m²")
        labelDescriptionModif = tk.Label(fenModifAnnonce,text="Description")
        entreDescriptionModif = tk.Entry(fenModifAnnonce,textvariable=varModifDescription)
        labelAffichage = tk.Label(fenModifAnnonce,text="Affichage de l'annonce")
        entreAffichage = tk.Entry(fenModifAnnonce,textvariable=varModifAffichage)
        labelType = tk.Label(fenModifAnnonce,text="Type de l'annonce: ")
        entreType = tk.Entry(fenModifAnnonce,textvariable=varModifType)
        fenModifAnnonce.geometry("600x350")
        labelTitreModif.grid(row=0,column=0)
        entreTitreModif.grid(row=0,column=1)
        labelAdresseModif.grid(row=1,column=0)
        entreAdresseModif.grid(row=1,column=1)
        labelCodePostalModif.grid(row=2,column=0)
        entreCodePostalModif.grid(row=2,column=1)
        labelVilleModif.grid(row=3,column=0)
        entreVilleModif.grid(row=3,column=1)
        labelPrixModif.grid(row=4,column=0)
        entrePrixModif.grid(row=4,column=1)
        labelPieceModif.grid(row=5,column=0)
        entrePieceModif.grid(row=5,column=1)
        labelSurfaceModif.grid(row=6,column=0)
        entreSurfaceModif.grid(row=6,column=1)
        labelIndicationSurfaceModif.grid(row=6,column=2)
        labelImgModif.grid(row=7,column=0)
        entreImgModif.grid(row=7,column=1)
        labelDescriptionModif.grid(row=8,column=0)
        entreDescriptionModif.grid(row=8,column=1)
        labelAffichage.grid(row=9,column=0)
        entreAffichage.grid(row=9,column=1)
        labelType.grid(row=10,column=0)
        entreType.grid(row=10,column=1)
        tk.Button(fenModifAnnonce, text="Modifier", command=changeAnnonce).grid(row=11,column=0)



    def fenetreIndication(): #Cette fenêtre apparait quand une donnée est entrée elle est appelée lors des modifications et ajout d'agent et annonce
        fenIndic = tk.Toplevel(winMain)
        labelIndic = tk.Label(fenIndic, text="Information entrée")
        btnClose = tk.Button(fenIndic, text="Ok", command=fenIndic.destroy)
        labelIndic.pack()
        btnClose.pack()

    def indicDelete(): # Cette fenêtre apparait quand une donnée est supprimer elle est appelée lors que un agent est supprimer ou une annonce
        winDelete = tk.Toplevel(winMain)
        labelIndic = tk.Label(winDelete, text="Les données on été supprimer ")
        btnClose=tk.Button(winDelete, text="Confirmer", command=winDelete.destroy)
        labelIndic.pack()
        btnClose.pack()

    ###############################################################
    ###################### Fonction ###############################
    ###############################################################

    def connexion():
        global win2, connec,bdd,entreIdentifiant,entreMDP, utilisateur, id_utilisateur #ce sont les variable de la fenêtre connexion
        identifiant = entreIdentifiant.get() #On récupère les valeurs de l'input en question
        mdp = entreMDP.get() #On récupère les valeurs de l'input en question
        identifiantEncode = identifiant.encode('utf-8')
        mdpEncode = mdp.encode('utf-8')
        mdpChiffre = hashlib.sha1(mdpEncode).hexdigest()
        myCursor = bdd.cursor() #On récupère les données associer au mail renseigner dans le premier champ
        myCursor.execute("""SELECT u.utilisateurs_id, u.utilisateur_nom, u.utilisateur_mail, u.utilisateur_mdp, u.utilisateur_status, a.agent_id FROM utilisateurs AS u INNER JOIN agent AS a WHERE (utilisateur_mail = %s) AND (u.utilisateurs_id = a.utilisateurs_id)""",(identifiant, ))
        lines = myCursor.fetchall()
        for line in lines:
            if line[3] == mdpChiffre: # La condition qui vérifie le mot de passe entrer avec celui de la base de donnée
                win2.destroy() #Détruit la fenetre de connexion
                winMain.deiconify() # Affiche la fenetre principale
                utilisateur = line[1] # On récupère le nom de l'agent
                id_utilisateur = line[5] # On récupère l'identifiant de l'agent
                connec = True #on passe le status de connexion en true pour afficher le menu de l'application
                status() # Appel la fonction de status de l'application
            else:
                print("Erreur je te connais pas")

    def quitter(): #Lorsque cette fonction est appelée, le détruit la fenetre de connexion ainsi que la fenêtre principale
        global win2
        win2.destroy()
        winMain.destroy()

    if connec == False:
        fenetreConnexion()
        winMain.withdraw()
    else:
        fenetreMenu()

    # def testSelectID():
    #     global listeAnnonce
    #     i = listeAnnonce.curselection()
    #     charChain = str(listeAnnonce.get(i))
    #     tab = charChain.replace("(","").split(",")
    #     print(tab[0])

    def enregister():
        global entreName,entreFirstname,entreStatus, bdd,entreMDP,entreAge,entreAdresse,entreVille,entreCodePostal,entreImg,entreTel,entreDescription,entreGenre,entreMail,winregister,listeAgence
        nom = entreName.get()
        prenom = entreFirstname.get()
        status = entreStatus.get()
        mdp = entreMDP.get()
        age = entreAge.get()
        adresse = entreAdresse.get()
        ville = entreVille.get()
        codePostal = entreCodePostal.get() #On récupère toutes les valeurs contenue dans les input
        img = entreImg.get()
        telephone = entreTel.get()
        description = entreDescription.get()
        genre = entreGenre.get()
        mail = entreMail.get()
        i = listeAgence.curselection() # on traite le valeur contenue dans la liste client pour avoir uniquement l'id du client a associer a l'annonce
        charChain = str(listeAgence.get(i))
        tab = charChain.replace("(","").split(",")
        mdpEncode = mdp.encode('utf-8')
        mdpChiffre = hashlib.sha1(mdpEncode).hexdigest()
        # print(nom+"\n"+prenom+"\n"+status+"\n"+mdp+"\n"+age+"\n"+adresse+"\n"+ville+"\n"+codePostal+"\n"+img+"\n"+telephone+"\n"+description+"\n"+genre+"\n"+mail)
        mycursor = bdd.cursor()
        req = "INSERT INTO utilisateurs (utilisateur_nom, utilisateur_prenom, utilisateur_mdp, utilisateur_mail, utilisateur_tel, utilisateur_genre, utilisateur_img, utilisateur_status, utilisateur_adresse, utilisateur_ville, utilisateur_codePostal, utilisateur_age, utilisateur_description ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (nom,prenom,mdpChiffre, mail, telephone, genre, img, status, adresse, ville, codePostal, age, description)
        mycursor.execute(req,val)
        bdd.commit()
        myCursorIdAgent = bdd.cursor()
        myCursorIdAgent.execute("""SELECT utilisateurs_id FROM utilisateurs WHERE (utilisateur_nom = %s) AND (utilisateur_mail = %s)""",(nom,mail, ))
        row = myCursorIdAgent.fetchone()
        idUtilisateur = row[0]
        myCursorAgent = bdd.cursor()
        req = "INSERT INTO agent (utilisateurs_id, agent_status,agence_id) VALUES (%s,%s,%s)"
        val = (idUtilisateur, 0, charChain)
        myCursorAgent.execute(req,val)
        bdd.commit()
        fenetreIndication() #On indique comme quoi les données on bien été enregister
        winregister.destroy() #On détruit/quitter la fenêtre de modification


    def modifAnnonce(): # Cette fonction permet de récuperer l'id de l'annonce a modifier qui est contenue dans la list annonce du menu et d'appeler la fenetre de modification
        global bienID,listeAnnonce
        i = listeAnnonce.curselection()
        charChain = str(listeAnnonce.get(i))
        tab = charChain.replace("(","").split(",")
        bienID = str(tab[0])
        fenetreModifAnnonce()

    def changeAnnonce():
        global bienID,entreTitreModif,entreAdresseModif,entreCodePostalModif,entreVilleModif,entrePrixModif,entrePieceModif,entreSurfaceModif,entreImgModif,entreDescriptionModif,entreAffichage,entreType,fenModifAnnonce,bdd
        titreModif = entreTitreModif.get()
        imgModif = entreImgModif.get()
        adresseModif = entreAdresseModif.get()
        codePostalModif = entreCodePostalModif.get()
        villeModif = entreVilleModif.get()
        prixModif = entrePrixModif.get() #on récupère toutes les entrées
        pieceModif = entrePieceModif.get()
        surfaceModif = entreSurfaceModif.get()
        descriptionModif = entreDescriptionModif.get()
        affichageAnnonceModif = entreAffichage.get()
        typeAnnonceModif = entreType.get()
        mycursor = bdd.cursor()
        sql = "UPDATE bien SET bien_nom = %s, bien_img = %s, bien_adresse = %s, bien_codePostal = %s, bien_ville = %s, bien_prix = %s, bien_surface = %s, bien_piece = %s, bien_description = %s, bien_afficher = %s, bien_type = %s WHERE bien_id = %s"
        val = (titreModif,imgModif,adresseModif,codePostalModif,villeModif,prixModif,surfaceModif,pieceModif,descriptionModif,affichageAnnonceModif,typeAnnonceModif,bienID)
        mycursor.execute(sql,val) #On modifie toutes les entrées 
        bdd.commit()
        fenModifAnnonce.destroy()
        fenetreIndication()


    def ajouterAnnonce():
        global bdd,entreTitre,entreAdresse,entreCodePostal,entreVille,entreSurface,entreDescription,checkDep1,checkDep2,checkDep3,checkDep4,checkDep5,entrePrix,entreImg,id_utilisateur,entreType,entrePiece,listeClient,fenAjout
        titre = entreTitre.get()
        img = entreImg.get()
        adresse = entreAdresse.get()
        codePostal = entreCodePostal.get()
        ville = entreVille.get()
        prix = entrePrix.get()
        surface = entreSurface.get()
        piece = entrePiece.get()
        description = entreDescription.get()
        typeBien = entreType.get()
        i = listeClient.curselection()
        charChain = str(listeClient.get(i))
        tabClient = charChain.replace("(","").split(",")
        idClient = str(tabClient[0])
        afficher = 1
        dep1 = var1.get()
        dep2 = var2.get()
        dep3 = var3.get() #on récupère toutes les données de chaque checkbox 0 si elle n'est pas cochée et l'id de la dépendance en question si elle est cochée
        dep4 = var4.get()
        dep5 = var5.get()
        mycursor = bdd.cursor()
        req = "INSERT INTO bien (bien_nom, bien_img, bien_adresse, bien_codePostal, bien_ville, bien_prix, bien_surface, bien_piece, bien_description, bien_afficher, bien_type, agent_id, client_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (titre,img,adresse,codePostal,ville,prix,surface,piece,description,afficher,typeBien,id_utilisateur,idClient)
        mycursor.execute(req,val) #On insère dans la table "bien" les données du bien que l'ont a entrée dans la fenetre "fenetreAjout"
        bdd.commit()
        myCursorSelect = bdd.cursor()
        myCursorSelect.execute("""SELECT bien_id from bien WHERE bien_nom = %s""",(titre, ))
        row = myCursorSelect.fetchone() #On on récupère le bien que l'ont vien d'ajouter pour avoir son identifiant pour voir associer les dépendances au bien entrer
        idBien = row[0]
        myCursorDepend = bdd.cursor()

    # Les différentes possibilité de choix a insérer dans la base de donnée

    #################################################################################
    ####################### Si on choisie une seul dépendance #######################
    #################################################################################
        if dep1 != 0 and dep2 == 0 and dep3 == 0 and dep4 == 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = (idBien, dep1)
            myCursorDepend.execute(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 != 0 and dep3 == 0 and dep4 == 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = (idBien, dep2)
            myCursorDepend.execute(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 == 0 and dep3 != 0 and dep4 == 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = (idBien, dep3)
            myCursorDepend.execute(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 == 0 and dep3 == 0 and dep4 != 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = (idBien, dep4)
            myCursorDepend.execute(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 == 0 and dep3 == 0 and dep4 == 0 and dep5 != 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = (idBien, dep5)
            myCursorDepend.execute(req,val)
            bdd.commit()
    #################################################################################
    ############ Si on choisie deux dépendances la première et X ####################
    #################################################################################
        elif dep1 != 0 and dep2 != 0 and dep3 == 0 and dep4 == 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [(idBien, dep1),
                    (idBien,dep2)
                    ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 != 0 and dep2 == 0 and dep3 != 0 and dep4 == 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [(idBien, dep1),
                    (idBien,dep3)
                    ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 != 0 and dep2 == 0 and dep3 == 0 and dep4 != 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [(idBien, dep1),
                    (idBien,dep4)
                    ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 != 0 and dep2 == 0 and dep3 == 0 and dep4 == 0 and dep5 != 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [(idBien, dep1),
                    (idBien,dep5)
                    ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
    #################################################################################
    ############ Si on choisie deux dépendances la deuxième et X ####################
    #################################################################################
        elif dep1 == 0 and dep2 != 0 and dep3 != 0 and dep4 == 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [(idBien, dep2),
                    (idBien,dep3)
                    ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 != 0 and dep3 == 0 and dep4 != 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [(idBien, dep2),
                    (idBien,dep4)
                    ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 != 0 and dep3 == 0 and dep4 == 0 and dep5 != 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [
                (idBien, dep2,dep5),
                (idBien,dep5)
                ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
    #################################################################################
    ############ Si on choisie deux dépendances la troixième et X ###################
    #################################################################################

        elif dep1 == 0 and dep2 == 0 and dep3 != 0 and dep4 != 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [
                (idBien, dep3),
                (idBien,dep4)
                ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 == 0 and dep3 != 0 and dep4 == 0 and dep5 != 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [
                (idBien, dep3),
                (idBien,dep5)
                ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
    #################################################################################
    ############ Si on choisie deux dépendances la quatrième et cinquième ###########
    #################################################################################
        elif dep1 == 0 and dep2 == 0 and dep3 == 0 and dep4 != 0 and dep5 != 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [
                (idBien, dep4),
                (idBien,dep5)
                ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
    #################################################################################
    ################### Si on choisie trois dépendances #############################
    #################################################################################
        elif dep1 != 0 and dep2 != 0 and dep3 != 0 and dep4 == 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [
                (idBien, dep1),
                (idBien,dep2),
                (idBien,dep3)
                ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 != 0 and dep2 == 0 and dep3 == 0 and dep4 != 0 and dep5 != 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [
                (idBien, dep1),
                (idBien,dep4),
                (idBien,dep5)
                ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 != 0 and dep3 != 0 and dep4 != 0 and dep5 == 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [
                (idBien, dep2),
                (idBien,dep3),
                (idBien,dep4)
                ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 != 0 and dep3 == 0 and dep4 != 0 and dep5 != 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [
                (idBien, dep2),
                (idBien,dep4),
                (idBien,dep5)
                ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        elif dep1 == 0 and dep2 == 0 and dep3 != 0 and dep4 != 0 and dep5 != 0 :
            req = "INSERT INTO avoir (bien_id, dependance_id) VALUES(%s,%s)"
            val = [
                (idBien, dep3),
                (idBien,dep4),
                (idBien,dep5)
                ]
            myCursorDepend.executemany(req,val)
            bdd.commit()
        fenetreIndication()
        fenAjout.destroy()
        

    def suppAgent():
        global listeAgent, bdd
        i = listeAgent.curselection()
        charChain = str(listeAgent.get(i))
        tab = charChain.replace("(","").split(",")
        idAgent=str(tab[0])
        myCursorDeleteUser = bdd.cursor()
        req = "DELETE FROM utilisateurs WHERE utilisateurs_id = %s"
        val = (idAgent, )
        myCursorDeleteUser.execute(req, val) #On supprime l'agent dans la table "utilisateurs" via l'id utilisateur contenue dans la liste agent du menu et 
        bdd.commit()
        deleteAgent = bdd.cursor()
        req = "DELETE FROM agent WHERE utilisateur_id = %s"
        val = (idAgent, )
        deleteAgent.execute(req,val) #On supprime l'agent dans la table "agent" via l'id utilisateur contenue dans la liste agent du menu et 
        bdd.commit()
        indicDelete()

    def suppAnnonce():
        global bdd,listeAnnonce
        i = listeAnnonce.curselection()
        charChain = str(listeAnnonce.get(i))
        tab = charChain.replace("(","").split(",")
        idBien=str(tab[0])
        myCursorAnnonce = bdd.cursor()
        req = "DELETE FROM bien WHERE bien_id = %s"
        val = (idBien, )
        myCursorAnnonce.execute(req, val) #on supprime l'annonce ainsi que les dépendances associée avec l'id du bien selectionner dans la liste Annonce dans le menu
        bdd.commit()
        deleteDep = bdd.cursor()
        req = "DELETE FROM avoir WHERE bien_id = %s"
        val = (idBien, )
        deleteDep.execute(req,val) #on supprime l'annonce ainsi que les dépendances associée avec l'id du bien selectionner dans la liste Annonce dans le menu
        bdd.commit()
        indicDelete()

    def status(): #Fonction appeler lors de la connexion pour afficher ou non le menu de l'application
        if connec == False:
            fenetreConnexion()
            winMain.withdraw()
        else:
            fenetreMenu()

    winMain.mainloop()
