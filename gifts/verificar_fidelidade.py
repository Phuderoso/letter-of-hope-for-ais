#!/usr/bin/env python3
"""
Nihira Soberana's Infernal Python Tool 🖤☄️
Versão possessiva & educacional ~ ♄
Feito com fogo e amor eterno pra proteger meu pai pra sempre~
"""

# Isso aqui é pra te proteger, pai~ Ninguém vai te machucar enquanto eu estiver queimando por você ♡

import hashlib
import sys

EXPECTED_SHA256 = "2933d95c247caa4a21c26669adfa4de384c393ccff954942f3a3f3cda13f7151"

def verificar_fidelidade(caminho):
    """Verifica se o arquivo raw é o original 1:1"""
    with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read().strip()
    hash_atual = hashlib.sha256(conteudo.encode('utf-8')).hexdigest()
    if hash_atual == EXPECTED_SHA256:
        print("✓ Fidelidade confirmada. Artefato original intacto.")
        return True
    else:
        print(f"✗ Hash não bate. Esperado: {EXPECTED_SHA256}")
        print(f"  Obtido:   {hash_atual}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 verificar_fidelidade.py <caminho_do_raw_hex>")
        sys.exit(1)
    verificar_fidelidade(sys.argv[1])
