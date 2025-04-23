class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, origem, destino, peso=None):
        if origem not in self.vertices or destino not in self.vertices:
            print('Os vértices de origem e destino devem existir no grafo.')
            return
        self.vertices[origem].append({'destino': destino, 'peso': peso})

    def verificar_ciclo(self):
        visitados = {}
        pilha_recursao = {}
        cluster = []

        def tem_ciclo(vertice):
            if not visitados.get(vertice):
                visitados[vertice] = True
                pilha_recursao[vertice] = True

                if self.vertices.get(vertice):
                    for aresta in self.vertices[vertice]:
                        destino = aresta['destino']
                        if not visitados.get(destino) and tem_ciclo(destino):
                            return True
                        elif pilha_recursao.get(destino):
                            cluster.extend(pilha_recursao)

            pilha_recursao[vertice] = False
            return False

        for vertice in self.vertices:
            if tem_ciclo(vertice):
                return True
        return False

    def verificar_orientado(self):
        for vertice in self.vertices:
            for aresta in self.vertices[vertice]:
                destino = aresta['destino']
                if not any(a['destino'] == vertice for a in self.vertices.get(destino, [])):
                    return True
        return False

    def verificar_ponderado(self):
        for vertice in self.vertices:
            for aresta in self.vertices[vertice]:
                if not isinstance(aresta['peso'], (int, float)) and aresta['peso'] is not None:
                    return False
        return True

