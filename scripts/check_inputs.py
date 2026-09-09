#!/usr/bin/env python3
"""
Validador de arquivos de entrada para o gerador de Painel AVCB/PPCI V.tal.
Garante que a logo da V.tal e a planilha Excel estejam presentes antes de iniciar a execução.
"""

import os
import sys

REQUIRED_FILES = [
    "logo-vtal-footer.png",
    "Big_Numbers_AVCB_-_planilha_IA__1_.xlsx"
]

def check_inputs(base_dir="."):
    missing = []
    for file_name in REQUIRED_FILES:
        file_path = os.path.join(base_dir, file_name)
        if not os.path.exists(file_path):
            missing.append(file_name)
    
    if missing:
        print("❌ [ERRO] A COLETA DOS ARQUIVOS É OBRIGATÓRIA PARA RODAR O PROMPT.")
        print(f"Arquivos ausentes: {', '.join(missing)}")
        print("A execução foi suspensa. Por favor, anexe os arquivos solicitados e envie um novo prompt.")
        return False
    
    print("✅ [OK] Todos os arquivos obrigatórios foram encontrados:")
    for f in REQUIRED_FILES:
        print(f"   - {f}")
    return True

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    success = check_inputs(target_dir)
    sys.exit(0 if success else 1)
