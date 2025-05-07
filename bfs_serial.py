from collections import deque

def bfs_serial(labirinto, inicio, fim):
    fila = deque([inicio])
    visitados = set()
    anterior = {}

    while fila:
        atual = fila.popleft()
        yield ("tentativa", atual)

        if atual == fim:
            # Reconstruir o caminho do fim até o início
            caminho = []
            while atual != inicio:
                caminho.append(atual)
                atual = anterior[atual]
            caminho.append(inicio)
            caminho.reverse()
            yield ("solucao", caminho)
            return

        if atual in visitados:
            continue
        visitados.add(atual)

        for vizinho in labirinto.get_vizinhos(atual):
            if vizinho not in visitados and vizinho not in fila:
                anterior[vizinho] = atual
                fila.append(vizinho)
