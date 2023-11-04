import getpass
import hashlib
from datetime import datetime
import bcrypt

def cryptage365():
    mot= getpass.getpass("Entrez votre mot de passe : ")
    hache_sha256 = hashlib.sha256(mot.encode()).hexdigest()
    print(f"Le haché SHA-256 de '{mot}' est '{hache_sha256}'")
    
def gensalt():
        mot= getpass.getpass("Entrez votre mot de passe : ")
        mott=mot.encode('utf-8')
        passmot=bcrypt.hashpw(mott,bcrypt.gensalt())
        print(f"le haché de {mot} est {passmot}")

def attaque_par_dictionnaire():
    mot= getpass.getpass("Entrez votre mot de passe : ")
    with open('dic.txt', mode='r') as dic:
        n = 0
        t = datetime.now()
        for line in dic:
            word = line.strip()
            if word == mot:
                print(f"Le mot de passe cible ({mot}) a été trouvé dans le dictionnaire le ({t}).")
                break
        else:
            print(f"Le mot de passe cible ({mot}) n'a pas été trouvé dans le dictionnaire.")

      
            