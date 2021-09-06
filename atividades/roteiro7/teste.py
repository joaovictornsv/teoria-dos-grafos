from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from meu_grafo import *

g_dijkstra1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
g_dijkstra1.adicionaAresta('a1', 'A', 'B', 1)
g_dijkstra1.adicionaAresta('a2', 'B', 'C', 1)
g_dijkstra1.adicionaAresta('a3', 'C', 'D', 1)
g_dijkstra1.adicionaAresta('a4', 'C', 'E', 2)
g_dijkstra1.adicionaAresta('a5', 'D', 'E', 3)
g_dijkstra1.adicionaAresta('a6', 'E', 'G', 2)
g_dijkstra1.adicionaAresta('a7', 'B', 'F', 3)
g_dijkstra1.adicionaAresta('a8', 'F', 'G', 1)


print(g_dijkstra1.dijkstra_drone('A', 'D', 2, 1, ['C']))

