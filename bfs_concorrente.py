import threading
from queue import Queue

def bfs_concorrente(labirinto, inicio, fim):
    resultado = []
    fila = Queue()
    visitados = set()
    lock = threading.Lock()
    encontrado = threading.Event()

    fila.put(([inicio], inicio))

    def worker():
        while not fila.empty() and not encontrado.is_set():
            try:
                caminho, atual = fila.get_nowait()
            except:
                return

            with lock:
                if atual in visitados:
                    continue
                visitados.add(atual)

            if atual == fim:
                with lock:
                    resultado.append(caminho)
                    encontrado.set()
                return

            for vizinho in labirinto.get_vizinhos(atual):
                if vizinho not in visitados:
                    fila.put((caminho + [vizinho], vizinho))

    threads = []
    for _ in range(8):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return resultado[0] if resultado else []
