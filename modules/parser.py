# modules/parser.py

def load_contract(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def split_contract(text, sep="Cláusula"):
    partes = text.split(sep)
    return [f"{sep}{p.strip()}" for p in partes if p.strip()]
