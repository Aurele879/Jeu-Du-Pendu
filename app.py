from random import randint

fichier = open("liste_mots.txt", 'r') #Ouverture du fichier de dictionnaire
contenu = fichier.read() #Lecture du fichier de dictionnaire
fichier.close()  #Fermeture du fichier de dictionnaire
L = contenu.split() # Mise en forme des mots en liste
mot = L[randint(0, len(L))] #Choix aléatoire du mot
mot_lettres = list(mot) #Mise en forme du mot choisi en liste

L_mot = [] #Génération des tirets d'avencement dans une variable
for i in range(len(mot_lettres)):
    L_mot.append("_")



life = 10 #Nombre de PVs
win = False #Variable de victoire
while life != 0:  #Boucle principale
    
    print(f"L'avencement du mot à trouver est : {L_mot} et il vous reste {life} vies.") #Indication de l'avencement
    prop = int(input("Entrez 1 pour tester une lettre, et 2 pour tester un mot : ")) #Choix d'entrer un mot ou une lettre

    if prop == 1: # /LETTRE/
        lettre = str(input("Entrez la lettre que vous voulez tester : "))
        trouve = False
        for i in range(len(mot_lettres)): #Comparaison entre la lettre donné et l'entièreté des lettres de la liste correspondant au mot
            if lettre == mot_lettres[i]:
                L_mot[i] = lettre #Ajout de la lettre trouvée à la place de son tiret
                trouve = True
        if trouve == True:
            print("La lettre a été trouvée dans le mot, elle a été ajoutée à la place d'un ou plusieurs tirets !")
        else:
            print("La lettre n'a pas été trouvée dans le mot, vous perdez une vie !")
            life -= 1

    elif prop == 2: # /MOT/
        mot_proposé = str(input("Entrez le mot que vous voulez tester : "))
        if mot_proposé == mot: #Comparaison entre le mot entré et le mot séléctionné
            print(f"Vous avez gagné au bout de {life} vies !")
            win = True #Variable de victoire pour le message de fin
            break #Sortie de la boucle
        else:
            print("Ce n'est pas le bon mot, vous perdez une vie !")
            life -= 1 

    else:
        print("Apprenez à lire !") #Blague immature

if life == 0 and win != True: #Message en cas de perte (si toutes les vies sont epuisés avant d'avoir gagné)
    print("Vous avez epuisé vos vies sans trouver le mot, c'est perdu, dommage ...")



# Cahier des charges : Jeu du pendu à partir du dictionnaire donnée.
    
    # - Lire le fichier dictionnaire et le transformer en liste de mots
    # - Choisir un mot au hasard dans la liste
    # - Afficher pour l'utilisateur le mot caché avec le nombre de lettre
    # - Permettre à l'utilisateur de rentrer une lettre ou un mot
    # - Vérifier si la lettre est présente dans le mot et afficher une réponse adaptée à l'utilisateur
    # - boucler en continuer jusqu'à épuisement des vies ou réussite de l'utilisateur.
