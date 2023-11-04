import getpass
import hashlib
import bcrypt
from Crypto.PublicKey import RSA
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding

import A
import B




def menu_principal():
   

    while True:
        print(" A-premiére partie")
        print("               1- Haché le mot par sha256 ")
        print("               2- Haché le mot en générant un salt (bcrypt) ")
        print("               3- Attaquer par dictionnaire")
        print(" B-Dexiéme partie")
        print("               4-Générer les paires de clés dans un fichier")
        print("               5-Chiffrer et déchiffrer un message de votre choix par RSA")
        print("               6-Signer un message de votre choix par RSA et le vérifier ")
        print(" C-Troixiéme partie")
        print("               7-Générer les paires de clés dans un fichier")
        print("               8-Générer un certificat autosigné par RSA")
        print("               9-Chiffrer un message de votre choix par ce certificat")
        print("10. Quitter")

        choix = input("Sélectionnez une option : ")

        if choix == "1":
            option1()
        elif choix == "2":
            option2()
        elif choix == "3":
            option3()
        elif choix == "4":
            option4()
        elif choix == "5":
            option5()
        elif choix == "6":
            option6()
        elif choix == "7":
            option7()
        elif choix == "8":
            option8()
        elif choix == "9":
            option9()
        elif choix == "10":
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")

def option1():
    print(A.cryptage365())

def option2():
    print(A.gensalt())

def option3():
    print(A.attaque_par_dictionnaire())

def option4():
    print(B.generationcle())

def option5():
    print(B.Chiffrer_message_rsa())

def option6():
    print(B.Signer_msg())

def option7():
    print(B.generationcle())

def option8():
    import CC
    

def option9():
   import CHIF
  
if __name__ == "__main__":
    menu_principal()
