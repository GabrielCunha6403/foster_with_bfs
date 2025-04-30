from collections import deque

def bfs_serial(labirinto, inicio, fim):
    filas = deque([([inicio], inicio)])
    visitados = set()

    while filas:
        caminho, atual = filas.popleft()
        if atual == fim:
            return caminho

        if atual in visitados:
            continue
        visitados.add(atual)

        for vizinho in labirinto.get_vizinhos(atual):
            if vizinho not in visitados:
                filas.append((caminho + [vizinho], vizinho))
    
    return None
