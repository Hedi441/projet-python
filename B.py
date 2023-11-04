from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

import getpass


def generationcle():
    key = RSA.generate(2048)  # You can choose your desired key size
    private_pem = key.export_key()
    public_pem = key.publickey().export_key()
    with open("key_privé.pem", "wb") as private_key_file:
        private_key_file.write(private_pem)
        with open("key_public.pem", "wb") as public_key_file:
            public_key_file.write(public_pem)
            print("les cles sont générer")
def Chiffrer_message_rsa():
    with open('key_privé.pem', 'rb') as key_file:
        cle_privé = RSA.import_key(key_file.read())
        message =getpass.getpass("Entrez votre message : ")
        cipher = PKCS1_OAEP.new(cle_privé)
        encrypted_message = cipher.encrypt(message.encode())
        print("le message crypter:", encrypted_message.hex())
        decipher = PKCS1_OAEP.new(cle_privé)
        decrypted_message = decipher.decrypt(encrypted_message)
        print("---------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------")
        print("le message decrypter:", decrypted_message.decode())
        print("-------------------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------")
def Signer_msg():
    with open('key_privé.pem', 'rb') as key_file:
        private_key = RSA.import_key(key_file.read())
        message = input("Donnez le mot pour signateur : ")
        message_hash = SHA256.new(message.encode())
        signature = pkcs1_15.new(private_key).sign(message_hash)
        print("la signature du mot saisie=    ",signature)
        print("-------------------------------------------------------------------------------------------")
    with open('key_public.pem', 'rb') as key_file:
        public_key = RSA.import_key(key_file.read())
        try:
            pkcs1_15.new(public_key).verify(message_hash,signature)
            print("-------------------------------------------------------------------------------------------")
            print("Verification de la signature avec la clé publique : La signature est valide. Le message n'a pas été altéré.")
            print("-------------------------------------------------------------------------------------------")
        except (ValueError, TypeError):
            print("-------------------------------------------------------------------------------------------")
            print("Verification de la signature avec la clé publique : La signature n'est pas valide. Le message a été altéré ou la clé publique ne correspond pas à la clé privée utilisée pour signer.")
            print("-------------------------------------------------------------------------------------------")

            