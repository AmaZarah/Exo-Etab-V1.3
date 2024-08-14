

from datetime import datetime
import Professeur
import Eleve
import Users
from etab_DB import creer_base_de_donnees




Connexion = False


def Default():
    creer_base_de_donnees()
    global Connexion
    print("             *************************************************************************\n ")
    print("                               BIENVENUE DANS L'APPLICATION ETAB v1.2                 \n ")
    print("             *************************************************************************")
    print("                                         CONNEXION")
    
    while Connexion == False:   
        id = input("Identifiant : ")
        pwd = input("Mot de passe : ")
        if id == "admin" and pwd == "admin":
            print("Connexion réussie!")
            Connexion = True
            break
        else:
            print("Identifiants incorrects!")
    MenuPrincipal()

def MenuPrincipal():
    global Connexion
    while (Connexion):
        try : 
            print("             *************************************************************************\n ")
            print("                               BIENVENUE DANS L'APPLICATION ETAB v1.2                 \n ")
            print("             *************************************************************************")
            print(" MENU: ")
            print("\n 1. Gestion des élèves\n 2. Gestion des professeurs\n 3. Gestion des utilisateurs\n 4. Deconnexion\n 0. Quitter")
            print("Date système : {}:{}".format(datetime.now().hour, datetime.now().minute))

            answer = input("\n Aller à : ")
            match answer:
                case "1":
                    MenuEleve()
                case "2":
                    MenuProf()
                case "3":
                    MenuUsers()
                case "4":
                    Connexion = False
                    Default()
                case "0":
                    Connexion = False
                    print('Au revoir Mr/Mme')
                    break
                case _:
                    print("Erreur choix indisponible")


        except Exception as e: 
            print ("Veuillez verifier votre choix ")
            

def MenuProf():
    global Connexion
    while (Connexion):
        try : 
            print("             *************************************************************************\n ")
            print("                                      GESTION DES PROFESSEURS                         \n ")
            print("             *************************************************************************")
            print(" MENU: ")
            print("\n 1. Ajouter un professeur\n 2. Supprimer un professeur\n 3. Modifier les informations du professeur\n 4. Lister les professeurs\n 5. Obtenir le dernier professeur ajouté\n 6. retour\n0. Accueil")
            
           
            print("Date système : {}:{}".format(datetime.now().hour, datetime.now().minute))
            answer = int(input("\n Aller à : "))
            match answer:
                case 1:
                    id = int(input("Id : "))
                    nom = input("Nom : ")
                    prenom = input("Prenom : ")
                    # vacant = input("Classe : ")
                    birthDay = input("Birth Day (DD/MM/YYYY) : ")
                    
                    if len(birthDay) == 10:
                        # print("Valid date format")
                        try:

                            day, month, year = map(int, birthDay.split('/'))
                            print(f"Day: {day}, Month: {month}, Year: {year}")
                            # if    1<=day<=31 and 1<=month<=12:
                            #     date_object = datetime(year, month, day)
                            #     print(date_object)
                            birthDay = datetime(year, month, day)
                        except ValueError : 
                            print("Date entrée invalide")
                    
                    else :
                        print("Date entrée invalide")
                    ville = input('Ville : ')
                    profesor = Professeur.Professeur(id, birthDay ,ville,prenom,nom)
                    
                case 2:
                    id = int(input(" ID : "))
                    profesor.supprimer(id)
                case 3:
                    id = input("L'id à modifier : ")
                    continues = True
                    while continues:
                        print("\n   1. Modifier le nom \n   2. Modifier le prenom \n   3. Modifier la date de naissance \n   4. Modifier Vacant \n   5. Modifier la ville \n   6. Retour")
                        Res = int(input("Choisir une option : "))
                        match Res:
                            case 1 :
                                nom = input("Le nouveau nom du professeur : ")
                                profesor.mettreAJour(id,newNom=nom)
                            case  2:
                                prenom = input("Le nouveau prénom : ")
                                profesor.mettreAJour(id,newPrenom=prenom)
                            case  3:
                                while True :
                                    birthDay = input("Birth Day (DD/MM/YYYY) : ")
                                    if len(birthDay) == 10:
                                        # print("Valid date format")
                                        try:

                                            day, month, year = map(int, birthDay.split('/'))
                                            # print(f"Day: {day}, Month: {month}, Year: {year}")
                                            birthDay = datetime(year, month, day)
                                            profesor.mettreAJour(id,newDateNaissance=birthDay)
                                            break
                                        except ValueError : 
                                            print("Date entrée invalide")
                                    
                                    else :
                                        print("Date entrée invalide")
                                                
                            case  4:
                                classe = input("Vacant ? : O/N ")
                                while True:
                                    if classe.upper() == "O" or classe.upper() == "OUI" :
                                        profesor.mettreAJour(id,vacant=True)
                                        break
                                    elif classe.upper() == "N" or classe.upper() == "NON" :
                                        profesor.mettreAJour(id,vacant=False)
                                        break
                                    else :
                                        print("Veuillez entrez une valeur correcte")
                                        pass
                                
                            case  5:
                                ville = input('Nouvelle Ville : ')
                                profesor.mettreAJour(id,newVille=ville)
                            case 6:
                                continues = False
                            case _:
                                print("Erreur choix indisponible")
                                        
                case 4:
                    profesor.lister()
                case 5:
                    profesor.obtenirDernier()
                case 6:
                    MenuPrincipal()
                case 0:
                    Connexion = False
                    Default()
                    
                case _:
                    print("Erreur choix indisponible")


        except Exception as e : 
            print("Erreur : ", e)


def MenuEleve():
    global Connexion
    while (Connexion):
        try : 
            print("             *************************************************************************\n ")
            print("                                       GESTION DES ELEVES                             \n ")
            print("             *************************************************************************")
            print(" MENU: ")
            print("\n 1. Ajouter un élève\n 2. Supprimer un élève\n 3. Modifier les informations de l'élève\n 4. Lister les élèves\n 5. Obtenir le dernier élève ajouté\n 6. retour\n 0. Accueil")
            
           
            print("Date système : {}:{}".format(datetime.now().hour, datetime.now().minute))

            answer = int(input("\n Aller à : "))
            match answer:
                case 1:
                    id = int(input("Id : "))
                    nom = input("Nom : ")
                    prenom = input("Prenom : ")
                    classe = input("Classe : ")
                    birthDay = input("Birth Day (DD/MM/YYYY) : ")
                    
                    if len(birthDay) == 10:
                        # print("Valid date format")
                        try:

                            day, month, year = map(int, birthDay.split('/'))
                            print(f"Day: {day}, Month: {month}, Year: {year}")
                            # if    1<=day<=31 and 1<=month<=12:
                            #     date_object = datetime(year, month, day)
                            #     print(date_object)
                            birthDay = datetime(year, month, day)
                        except ValueError : 
                            print("Date entrée invalide")
                    
                    else :
                        print("Date entrée invalide")
                    ville = input('Ville : ')
                    eleve = Eleve.Eleve(id, birthDay ,ville,prenom,nom, classe)
                    
                case 2:
                    id = int(input(" ID : "))
                    eleve.supprimer(id)
                case 3:
                    id = input("L'id de l'élève à modifier : ")
                    continues = True
                    while continues:
                        print("\n   1. Modifier le nom \n   2. Modifier le prenom \n   3. Modifier la date de naissance \n   4. Modifier la classe \n   5. Modifier la ville \n   6. Retour")
                        Res = int(input("Choisir une option : "))
                        if Res == 1 :
                            nom = input("Le nouveau nom de l'élève : ")
                            eleve.mettreAJour(id,newNom=nom)
                        if Res == 2:
                            prenom = input("Le nouveau prénom de l'élève : ")
                            eleve.mettreAJour(id,newPrenom=prenom)
                        if Res == 3:
                            birthDay = input("Birth Day (DD/MM/YYYY) : ")
                            if len(birthDay) == 10:
                                # print("Valid date format")
                                try:

                                    day, month, year = map(int, birthDay.split('/'))
                                    print(f"Day: {day}, Month: {month}, Year: {year}")
                                    birthDay = datetime(year, month, day)
                                    eleve.mettreAJour(id,newDateNaissance=birthDay)
                                except ValueError : 
                                    print("Date entrée invalide")
                            
                            else :
                                print("Date entrée invalide")
                                        
                        if Res == 4:
                            classe = input("Nouvelle Classe : ")
                            eleve.mettreAJour(id,newClasse=classe)
                        if Res == 5:
                            ville = input('Nouvelle Ville : ')
                            eleve.mettreAJour(id,newVille=ville)
                        if Res == 6:
                            continues = False
                                    
                case 4:
                    eleve.lister()
                case 5:
                    eleve.obtenirDernier()
                case 6:
                    MenuPrincipal()
                case 0:
                    Connexion = False
                    Default()
                    
                case _:
                    print("Erreur choix indisponible")


        except Exception as e : 
            print("Erreur detectée: ", e)







def MenuUsers():
    global Connexion
    while (Connexion):
        try : 
            print("             *************************************************************************\n ")
            print("                                      GESTION DES UTILISATEURS                        \n ")
            print("             *************************************************************************")
            print(" MENU: ")
            print("\n 1. Ajouter un utilisateur\n 2. Supprimer un utilisateur\n 3. Modifier les informations d'un utilisateur\n 4. Lister les utilisateurs\n 5. Obtenir le dernier utilisateur ajouté\n 6. retour\n0. Accueil")
            
           
            print("Date système : {}:{}".format(datetime.now().hour, datetime.now().minute))

            answer = int(input("\n Aller à : "))
            match answer:
                case 1:
                    print("Ajouter un utilisateur")
                case 2:
                    print("Supprimer un utilisateur")
                case 3:
                    print("Modifier les informations d'un utilisateur")
                case 4:
                    print("Lister les utilisateurs")
                case 5:
                    print("Dernier professeur ajouté")
                case 6:
                    Connexion = False
                    Default()
                case 0:
                    Connexion = False
                    Default()
                    
                case _:
                    print("Erreur choix indisponible")


        except Exception as e : 
           print("Veuillez verifier votre saisie")




Default()