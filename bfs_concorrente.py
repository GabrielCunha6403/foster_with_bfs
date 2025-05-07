import threading
from queue import Queue, Empty

def bfs_concorrente(labirinto, inicio, fim):
    fila = Queue()
    saida = Queue()
    visitados = set()
    lock = threading.Lock()
    encontrado = threading.Event()
    anterior = {}

    fila.put(inicio)

    def worker():
        while not fila.empty() and not encontrado.is_set():
            try:
                atual = fila.get(timeout=0.1)  # Aguarda um item na fila
            except Empty:
                return

            with lock:
                if atual in visitados:
                    continue
                visitados.add(atual)

            saida.put(("tentativa", atual))  # Emite tentativa em tempo real

            if atual == fim:
                caminho = []
                while atual != inicio:
                    caminho.append(atual)
                    atual = anterior[atual]
                caminho.append(inicio)
                caminho.reverse()
                saida.put(("solucao", caminho))
                encontrado.set()
                return

            for vizinho in labirinto.get_vizinhos(atual):
                with lock:
                    if vizinho not in visitados:
                        anterior[vizinho] = atual
                        fila.put(vizinho)

    # Inicia as threads
    threads = [threading.Thread(target=worker) for _ in range(8)]
    for t in threads:
        t.start()

    # Vai lendo da fila de saída em tempo real
    while True:
        try:
            evento = saida.get(timeout=0.1)
            yield evento
            if evento[0] == "solucao":
                break
        except Empty:
            if not any(t.is_alive() for t in threads):
                break

    # Aguarda as threads finalizarem
    for t in threads:
        t.join()
