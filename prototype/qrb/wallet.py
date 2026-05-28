"""Wallets QRB.

Una wallet es un par de claves ML-DSA-65 más la dirección derivada.
En este prototipo se persisten como JSON sin cifrar — NO USAR EN
PRODUCCIÓN: las claves privadas en disco deben ir cifradas con una
clave derivada de una passphrase (KDF tipo Argon2 o scrypt).
"""

import json
from dataclasses import dataclass
from pathlib import Path

from qrb.crypto import address_from_pubkey, generate_keypair


@dataclass
class Wallet:
    name: str
    address: str
    public_key: bytes
    private_key: bytes

    @classmethod
    def create(cls, name: str) -> "Wallet":
        """Genera una wallet nueva con par de claves ML-DSA-65."""
        public_key, private_key = generate_keypair()
        address = address_from_pubkey(public_key)
        return cls(
            name=name,
            address=address,
            public_key=public_key,
            private_key=private_key,
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "address": self.address,
            "public_key": self.public_key.hex(),
            "private_key": self.private_key.hex(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Wallet":
        return cls(
            name=data["name"],
            address=data["address"],
            public_key=bytes.fromhex(data["public_key"]),
            private_key=bytes.fromhex(data["private_key"]),
        )

    def save(self, wallets_dir: Path) -> Path:
        wallets_dir.mkdir(parents=True, exist_ok=True)
        path = wallets_dir / f"{self.name}.json"
        path.write_text(json.dumps(self.to_dict(), indent=2))
        return path

    @classmethod
    def load(cls, name: str, wallets_dir: Path) -> "Wallet":
        path = wallets_dir / f"{name}.json"
        if not path.exists():
            raise FileNotFoundError(
                f"Wallet '{name}' no encontrada en {wallets_dir}. "
                f"Crea una con: wallet create --name {name}"
            )
        data = json.loads(path.read_text())
        return cls.from_dict(data)

    @classmethod
    def list_all(cls, wallets_dir: Path) -> list[str]:
        if not wallets_dir.exists():
            return []
        return sorted(p.stem for p in wallets_dir.glob("*.json"))
