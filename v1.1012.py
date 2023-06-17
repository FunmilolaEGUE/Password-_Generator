from random import randint

def pass_simple(n):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    mot =[]  
    taille = len(alphabet)
    for i in range(0,n):
        index = randint(0,taille)
        mot.append(alphabet[index])
    passe = "".join(mot)
    print(passe)

def pass_intermediaire(n):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".","!","/","*","$"]
    mot =[]  
    taille = len(alphabet)
    for i in range(0,n):
        index = randint(0,taille)
        mot.append(alphabet[index])
    passe = "".join(mot)
    print(passe)

def pass_moyen(n):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    mot =[] 
    taille = len(alphabet)
    for i in range(0,n):
        index = randint(0,taille)
        mot.append(alphabet[index])
    passe = "".join(mot)
    print(passe)

def pass_complex(n):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".","!","/","*","$","0","1","2","3","4","5","6","7","8","9"]
    mot =[] 
    taille = len(alphabet)
    for i in range(0,n):
        index = randint(0,taille)
        mot.append(alphabet[index])
    passe = "".join(mot)
    print(passe)

def menu() :
    boucle = 1
    while (boucle ==1 ):
        print("Veuillez entrer la taille du mot de passe")
        n = int(input("Taille :"))
        print("1- Lettres uniquement")
        print("2- Lettres et caractères")
        print("3- Lettres et nombres")
        print("4- Lettres, nombres et caractères")
        choix = int(input("Votre choix :"))
        
        if (choix == 1) :
            pass_simple(n)
        else:
            if (choix ==2) :
                pass_intermediaire(n)
            else :
                if (choix ==3) :
                    pass_moyen(n)
                else :
                    if (choix == 4) :
                        pass_complex(n)
                    else :
                        print("mauvais choix ")
                        menu()
    
        print("Voulez vous recommencer ? 1 -> oui, 0 -> non")
        boucle = int(input())

    if (boucle == 0) :
        print("Au revoir ")


print("------Générateur aléatoire de mot de passe-------")

menu()

# A faire :
# - S'occuper de la gestion des erreurs au niveau de code
# - Faire une version avec GUI


