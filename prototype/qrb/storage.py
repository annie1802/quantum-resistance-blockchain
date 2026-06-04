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
    """Carga JSON desde un archivo, lanzando un error claro que nombra el
    archivo si está corrupto (proceso cortado a mitad de escritura, JSON
    editado a mano, etc.). El CLI convierte el ValueError en 'ERROR: ...'
    con código de salida 1."""
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError) as exc:
        raise ValueError(
            f"no se pudo leer o parsear {path} -- el archivo puede estar "
            f"corrupto (proceso cortado a mitad de escritura, o editado a mano). "
            f"Prueba a borrarlo o repararlo. Detalles: {exc}"
        ) from exc
