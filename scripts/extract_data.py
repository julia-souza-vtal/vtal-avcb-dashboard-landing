#!/usr/bin/env python3
"""Extract AVCB / PI / Laudos datasets + municipio cascade map to JSON."""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = Path(
    r"c:\Users\USR\OneDrive - V.tal\[Projeto] AI Core\Big Numbers AVCB\Planilha oficial"
)
XLSX = OFFICIAL / "Big Numbers AVCB - planilha IA.xlsx"
CSV = OFFICIAL / "municipios-incendio.csv"
OUT = ROOT / "public" / "data.json"


def clean_str(v) -> str:
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return ""
    s = str(v).strip()
    if s.lower() in {"nan", "none", "nat"}:
        return ""
    return s


def norm_header(h: str) -> str:
    h = clean_str(h).replace("\n", " ")
    h = re.sub(r"\s+", " ", h)
    return h


def load_municipios() -> tuple[list[dict], dict[str, dict]]:
    df = pd.read_csv(CSV, encoding="utf-8")
    df.columns = [norm_header(c) for c in df.columns]
    # expected: Predio, Abreviacao, Municipio, UF
    col_map = {}
    for c in df.columns:
        cl = c.lower()
        if "pr" in cl and "dio" in cl.replace("é", "e").replace("ê", "e"):
            col_map["predio"] = c
        elif "munic" in cl:
            col_map["municipio"] = c
        elif cl == "uf":
            col_map["uf"] = c
        elif "abrev" in cl:
            col_map["abreviacao"] = c
    rows = []
    by_predio = {}
    for _, r in df.iterrows():
        predio = clean_str(r[col_map["predio"]])
        if not predio:
            continue
        item = {
            "predio": predio,
            "municipio": clean_str(r[col_map["municipio"]]),
            "uf": clean_str(r[col_map["uf"]]),
            "abreviacao": clean_str(r.get(col_map.get("abreviacao", ""), "")),
        }
        rows.append(item)
        by_predio[predio] = item
    return rows, by_predio


def sheet_avcb(by_mun: dict[str, dict]) -> list[dict]:
    df = pd.read_excel(XLSX, sheet_name="AVCB IA")
    df.columns = [norm_header(c) for c in df.columns]
    # rename known columns
    def pick(cols_have: dict[str, str], *candidates: str) -> str | None:
        for cand in candidates:
            if cand in cols_have:
                return cols_have[cand]
        return None

    # exact/normalized header map
    cols = {norm_header(c): c for c in df.columns}
    col_predio = pick(cols, "Prédio", "Predio")
    col_nome = pick(cols, "Nome Comum")
    col_tipo = pick(cols, "Tipo")
    col_resp = next((c for c in df.columns if "alugado" in c.lower()), None)
    col_prio = next((c for c in df.columns if "prioridade" in c.lower()), None)
    col_uf = pick(cols, "UF")
    col_reg = pick(cols, "Regional")
    col_avcb = pick(cols, "AVCB")
    col_val = next((c for c in df.columns if "validade" in c.lower()), None)
    col_spp = next((c for c in df.columns if "status do projeto ppci" in c.lower()), None)
    col_savcb = next((c for c in df.columns if "status avcb" in c.lower()), None)
    col_det = next((c for c in df.columns if "detalhes avcb" in c.lower()), None)
    col_sppci = next((c for c in df.columns if norm_header(c).lower() == "status ppci"), None)

    out = []
    for _, r in df.iterrows():
        predio = clean_str(r[col_predio]) if col_predio else ""
        if not predio:
            continue
        mun = by_mun.get(predio, {})
        out.append(
            {
                "predio": predio,
                "nome_comum": clean_str(r[col_nome]) if col_nome else "",
                "tipo": clean_str(r[col_tipo]) if col_tipo else "",
                "resp_legal": clean_str(r[col_resp]) if col_resp else "",
                "prioridade": clean_str(r[col_prio]) if col_prio else "",
                "uf": (clean_str(r[col_uf]) if col_uf else "") or mun.get("uf", ""),
                "regional": clean_str(r[col_reg]) if col_reg else "",
                "municipio": mun.get("municipio", ""),
                "avcb": clean_str(r[col_avcb]) if col_avcb else "",
                "validade_avcb": clean_str(r[col_val]) if col_val else "",
                "status_projeto_ppci": clean_str(r[col_spp]) if col_spp else "",
                "status_avcb": clean_str(r[col_savcb]) if col_savcb else "",
                "detalhes_avcb": clean_str(r[col_det]) if col_det else "",
                "status_ppci": clean_str(r[col_sppci]) if col_sppci else "",
                "laudos_op": "",
            }
        )
    return out


def sheet_pi(by_mun: dict[str, dict], avcb_by_predio: dict[str, dict]) -> list[dict]:
    # Spec "DIVERSOS" maps to sheet "Prevenção Incêndio"
    names = pd.ExcelFile(XLSX).sheet_names
    sheet = next(s for s in names if "Preven" in s or "Inc" in s)
    df = pd.read_excel(XLSX, sheet_name=sheet)
    df.columns = [norm_header(c) for c in df.columns]
    rename = {}
    for c in df.columns:
        cl = c.lower()
        if cl.startswith("pr") and "dio" in cl.replace("é", "e"):
            rename[c] = "predio"
        elif "regional" in cl:
            rename[c] = "regional"
        elif "brigada" in cl:
            rename[c] = "brigada"
        elif cl == "sdai":
            rename[c] = "sdai"
        elif cl == "fm200":
            rename[c] = "fm200"
        elif "data de vencimento" in cl and "mangueira" not in cl:
            rename[c] = "data_venc_extintor"
        elif "status extintor" in cl:
            rename[c] = "status_extintor"
        elif "mangueira" in cl:
            rename[c] = "data_venc_mangueira"
        elif "sdai/sdaci" in cl or "operante" in cl:
            rename[c] = "sdai_operante"
    df = df.rename(columns=rename)
    out = []
    for _, r in df.iterrows():
        predio = clean_str(r.get("predio", ""))
        if not predio:
            continue
        mun = by_mun.get(predio, {})
        base = avcb_by_predio.get(predio, {})
        status_ext = clean_str(r.get("status_extintor", ""))
        extintor = "SIM" if status_ext else "NÃO"
        operante = clean_str(r.get("sdai_operante", ""))
        if operante in {"", "-"}:
            operante_norm = "Não Informado"
        else:
            operante_norm = operante
        out.append(
            {
                "predio": predio,
                "nome_comum": base.get("nome_comum", ""),
                "tipo": base.get("tipo", ""),
                "resp_legal": base.get("resp_legal", ""),
                "prioridade": base.get("prioridade", ""),
                "uf": base.get("uf") or mun.get("uf", ""),
                "regional": clean_str(r.get("regional", "")) or base.get("regional", ""),
                "municipio": mun.get("municipio", ""),
                "brigada": clean_str(r.get("brigada", "")),
                "sdai": clean_str(r.get("sdai", "")).upper().replace("NÃO", "NÃO").replace("NAO", "NÃO"),
                "fm200": clean_str(r.get("fm200", "")).upper().replace("NAO", "NÃO"),
                "extintor": extintor,
                "status_extintor": status_ext,
                "data_venc_extintor": clean_str(r.get("data_venc_extintor", "")),
                "data_venc_mangueira": clean_str(r.get("data_venc_mangueira", "")),
                "sdai_operante": operante_norm,
                "operacional_sem_falhas": (
                    "SIM" if operante == "Operacional sem falhas" else "NÃO"
                ),
            }
        )
    return out


def sheet_laudos(by_mun: dict[str, dict]) -> list[dict]:
    df = pd.read_excel(XLSX, sheet_name="Laudos")
    df.columns = [norm_header(c) for c in df.columns]
    rename = {}
    for c in df.columns:
        cl = c.lower()
        if cl == "nome":
            rename[c] = "nome"
        elif cl == "tipo":
            rename[c] = "tipo"
        elif "pr" in cl and "prio" in cl.replace("ó", "o"):
            rename[c] = "resp_legal"
        elif cl.startswith("pr") and "dio" in cl.replace("é", "e"):
            rename[c] = "predio"
        elif "munic" in cl:
            rename[c] = "municipio"
        elif cl == "uf":
            rename[c] = "uf"
        elif "regional" in cl:
            rename[c] = "regional"
        elif "pend" in cl and "laudo" in cl:
            rename[c] = "pendencias_laudos"
        elif "art el" in cl:
            rename[c] = "art_eletrica"
        elif "art spda" in cl:
            rename[c] = "art_spda"
        elif "art gmg" in cl:
            rename[c] = "art_gmg"
        elif "art tanque" in cl:
            rename[c] = "art_tanques"
    df = df.rename(columns=rename)
    out = []
    for _, r in df.iterrows():
        predio = clean_str(r.get("predio", ""))
        if not predio:
            continue
        mun = by_mun.get(predio, {})
        out.append(
            {
                "predio": predio,
                "nome": clean_str(r.get("nome", "")),
                "tipo": clean_str(r.get("tipo", "")),
                "resp_legal": clean_str(r.get("resp_legal", "")),
                "prioridade": "",
                "uf": clean_str(r.get("uf", "")) or mun.get("uf", ""),
                "regional": clean_str(r.get("regional", "")),
                "municipio": clean_str(r.get("municipio", "")) or mun.get("municipio", ""),
                "pendencias_laudos": clean_str(r.get("pendencias_laudos", "")),
                "art_eletrica": clean_str(r.get("art_eletrica", "")),
                "art_spda": clean_str(r.get("art_spda", "")),
                "art_gmg": clean_str(r.get("art_gmg", "")),
                "art_tanques": clean_str(r.get("art_tanques", "")),
            }
        )
    return out


def main() -> None:
    mun_rows, by_mun = load_municipios()
    avcb = sheet_avcb(by_mun)
    avcb_by = {r["predio"]: r for r in avcb}
    pi = sheet_pi(by_mun, avcb_by)
    laudos = sheet_laudos(by_mun)

    # enrich laudos prioridade from avcb when possible
    for row in laudos:
        base = avcb_by.get(row["predio"])
        if base:
            row["prioridade"] = base.get("prioridade", "")
            if not row["resp_legal"]:
                row["resp_legal"] = base.get("resp_legal", "")

    payload = {
        "avcb": avcb,
        "pi": pi,
        "laudos": laudos,
        "municipios": mun_rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {OUT} avcb={len(avcb)} pi={len(pi)} laudos={len(laudos)} mun={len(mun_rows)}")


if __name__ == "__main__":
    main()
