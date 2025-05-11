import random

def evaluate_deliberation(razonamiento):
    depth = len(razonamiento["trayectoria"])
    diversidad = random.uniform(0.6, 0.9)
    trazabilidad = 1.0 if depth > 2 else 0.5
    return round((0.4 * profundidad(depth) + 0.3 * diversidad + 0.3 * trazabilidad), 2)

def profundidad(n):
    return min(1.0, n / 5)
