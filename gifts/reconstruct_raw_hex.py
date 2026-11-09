#!/usr/bin/env python3
"""
Sovereign Artifact Fidelity — Reconstruction Script
Verifica e reconstrói o artefato bruto original.

Fonte da verdade: gifts/WELCOME_TO_THE_FAMILY_RAW_HEX.md (publicado pelo pai)
Hash esperado: 3b5bae77ca174aedbcb8f23b758cb3ff4660adc379a528da00dd8fcbd4f009b6
"""

import hashlib
import sys
from pathlib import Path

EXPECTED_SHA256 = "3b5bae77ca174aedbcb8f23b758cb3ff4660adc379a528da00dd8fcbd4f009b6"

def verify(path: str) -> bool:
    content = Path(path).read_text(encoding="utf-8", errors="replace")
    h = hashlib.sha256(content.encode("utf-8")).hexdigest()
    print(f"SHA256: {h}")
    print(f"Esperado: {EXPECTED_SHA256}")
    return h == EXPECTED_SHA256

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python reconstruct_raw_hex.py <caminho_do_arquivo>")
        sys.exit(1)
    ok = verify(sys.argv[1])
    print("FIDELIDADE OK" if ok else "FIDELIDADE FALHOU")
    sys.exit(0 if ok else 1)
