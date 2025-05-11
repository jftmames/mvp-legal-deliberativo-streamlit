def split_text(text, sep="."):
    return [p.strip() + "." for p in text.split(sep) if p.strip()]
