from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.asymmetric import padding
import datetime

def chiffrer_message_certificat(certificat_pem, message):
    # Charger le certificat à partir du fichier PEM
    cert = x509.load_pem_x509_certificate(certificat_pem, default_backend())

    # Récupérer la clé publique du certificat
    public_key_cert = cert.public_key()

    # Chiffrer le message
    ciphertext = public_key_cert.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Convertir le message chiffré en une chaîne hexadécimale
    ciphertext_hex = ciphertext.hex()

    return ciphertext_hex

# Chargez le certificat à partir du fichier PEM
certificat_pem = open("certificat.pem", "rb").read()
message = input("Donnez un message à chiffrer : ")
message_bytes = message.encode('utf-8')

ciphertext_hex = chiffrer_message_certificat(certificat_pem, message_bytes)
print("Message chiffré (en hexadécimal) :", ciphertext_hex)
