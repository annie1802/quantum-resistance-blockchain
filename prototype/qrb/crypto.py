"""Primitivas criptográficas post-cuánticas para QRB.

Usa ML-DSA-65 (estándar NIST FIPS 204, agosto 2024).
Equivalente al nivel de seguridad 3 de CRYSTALS-Dilithium.

Nivel de seguridad: ~AES-192 frente a ataques cuánticos.
Tamaños aproximados:
  - Clave pública: 1.952 bytes
  - Clave privada: 4.032 bytes
  - Firma:         3.309 bytes

Compárese con ECDSA secp256k1 (Ethereum/Bitcoin):
  - Clave pública: 33 bytes
  - Clave privada: 32 bytes
  - Firma:         64 bytes

El precio de la resistencia cuántica es un factor ~50× en tamaño.
QRB lo absorbe vía Account Abstraction y data availability eficiente.
"""

import hashlib

from dilithium_py.ml_dsa import ML_DSA_65

SIGNATURE_SCHEME = "ML-DSA-65"


def generate_keypair() -> tuple[bytes, bytes]:
    """Genera un par de claves ML-DSA-65.

    Returns:
        (public_key, private_key) como bytes.
    """
    pk, sk = ML_DSA_65.keygen()
    return pk, sk


def sign(message: bytes, private_key: bytes) -> bytes:
    """Firma un mensaje con clave privada ML-DSA-65.

    Args:
        message: bytes a firmar (típicamente el payload serializado
                 de una transacción o cabecera de bloque).
        private_key: clave privada del firmante.

    Returns:
        Firma desadjuntada (~3.309 bytes).
    """
    return ML_DSA_65.sign(private_key, message)


def verify(message: bytes, signature: bytes, public_key: bytes) -> bool:
    """Verifica una firma ML-DSA-65.

    Args:
        message: mensaje original.
        signature: firma a verificar.
        public_key: clave pública del firmante esperado.

    Returns:
        True si la firma es válida y corresponde a la clave dada,
        False en cualquier otro caso (incluida excepción).
    """
    try:
        return bool(ML_DSA_65.verify(public_key, message, signature))
    except Exception:
        return False


def address_from_pubkey(public_key: bytes) -> str:
    """Deriva una dirección QRB del hash de la clave pública.

    Igual que en Bitcoin y Ethereum modernos, las direcciones son el
    hash de la clave pública, no la clave pública en sí. Esto oculta
    la pubkey hasta el primer gasto desde esa dirección, lo cual es
    especialmente relevante en el contexto post-cuántico
    ('harvest now, decrypt later').

    Formato: '0x' + últimos 20 bytes del SHA3-256 de la pubkey, en hex.
    Total: 42 caracteres (compatible con la convención de Ethereum).

    Args:
        public_key: clave pública ML-DSA-65 en bytes.

    Returns:
        Dirección con prefijo '0x' y 40 hex chars.
    """
    h = hashlib.sha3_256(public_key).digest()
    return "0x" + h[-20:].hex()
