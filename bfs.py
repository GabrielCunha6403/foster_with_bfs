from grafo import Grafo

# Exemplo de uso
grafo = Grafo()

grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')
grafo.adicionar_vertice('E')
grafo.adicionar_vertice('F')

grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('A', 'C')
grafo.adicionar_aresta('A', 'E')
grafo.adicionar_aresta('B', 'A')
grafo.adicionar_aresta('C', 'D')
grafo.adicionar_aresta('C', 'F')
grafo.adicionar_aresta('D', 'B')
grafo.adicionar_aresta('D', 'C')
grafo.adicionar_aresta('D', 'F')
grafo.adicionar_aresta('E', 'C')
grafo.adicionar_aresta('F', 'E')

print('É cíclico?', grafo.verificar_ciclo())
print('É orientado?', grafo.verificar_orientado())
print('É ponderado?', grafo.verificar_ponderado())
