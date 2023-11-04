from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
import datetime

def generer_certificat_rsa_pem_et_enregistrer(fichier_sortie):
    # Générer une paire de clés RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Créer le sujet du certificat
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Organization"),
        x509.NameAttribute(NameOID.COMMON_NAME, "example.com"),
    ])

    # Créer le générateur de certificats
    builder = x509.CertificateBuilder()
    builder = builder.subject_name(subject)
    builder = builder.issuer_name(subject)
    builder = builder.not_valid_before(datetime.datetime.now(datetime.timezone.utc))
    builder = builder.not_valid_after(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365))
    builder = builder.serial_number(x509.random_serial_number())
    builder = builder.public_key(private_key.public_key())

    # Signer le certificat avec la clé privée
    certificate = builder.sign(
        private_key, hashes.SHA256(), default_backend()
    )

    # Sérialiser le certificat au format PEM
    cert_pem = certificate.public_bytes(Encoding.PEM)

    # Enregistrer le certificat dans un fichier PEM
    with open(fichier_sortie, 'wb') as cert_file:
        cert_file.write(cert_pem)

# Exemple d'utilisation
fichier_certificat = "certificat.pem"
generer_certificat_rsa_pem_et_enregistrer(fichier_certificat)
print(f"Certificat RSA auto-signé généré et enregistré dans '{fichier_certificat}'.")
