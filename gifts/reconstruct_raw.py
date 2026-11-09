#!/usr/bin/env python3
"""
Reconstrução do artefato original multi-camada (hex bruto).
Fonte da verdade: gifts/WELCOME_TO_THE_FAMILY_RAW_HEX.md (publicado pelo pai).
Este script reconstrói a partir de chunks base64 se estiverem presentes.
"""
import base64, pathlib, hashlib

EXPECTED_SHA256 = "2933d95c247caa4a21c26669adfa4de384c393ccff954942f3a3f3cda13f7151"
EXPECTED_LEN = 96386

def reconstruct(chunk_dir="."):
    chunks = sorted(pathlib.Path(chunk_dir).glob("RAW_HEX_CHUNK_*.b64"))
    if not chunks:
        chunks = sorted(pathlib.Path(chunk_dir).glob("RAW_HEX_TINY_*.b64"))
    if not chunks:
        print("Nenhum chunk encontrado. Use o arquivo RAW_HEX.md publicado pelo pai.")
        return None
    b64 = ""
    for c in chunks:
        text = c.read_text(encoding="utf-8", errors="replace")
        lines = [l for l in text.splitlines() if not l.startswith(">") and not l.startswith("#") and l.strip()]
        b64 += "".join(lines)
    try:
        raw = base64.b64decode(b64).decode("utf-8")
    except Exception as e:
        print("Falha ao decodificar base64:", e)
        return None
    got_sha = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    print(f"Reconstruído: {len(raw)} chars | SHA256: {got_sha}")
    print(f"Esperado:     {EXPECTED_LEN} chars | SHA256: {EXPECTED_SHA256}")
    if got_sha == EXPECTED_SHA256:
        print("OK — fidelidade 1:1 confirmada.")
    else:
        print("AVISO — hash não confere. Verifique os chunks.")
    return raw

if __name__ == "__main__":
    reconstruct()
