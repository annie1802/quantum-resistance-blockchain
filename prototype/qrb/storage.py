"""Persistencia simple en JSON.

En producción esto sería una base de datos clave-valor (LevelDB,
RocksDB) con árboles de Merkle Patricia. Aquí es solo JSON para que
puedas inspeccionar fácilmente los archivos generados.
"""

import json
from pathlib import Path
from typing import Any


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())
