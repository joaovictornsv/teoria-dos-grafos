from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from meu_grafo import *

g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('a1', 'A', 'B')
g_l1.adicionaAresta('a2', 'A', 'C')
g_l1.adicionaAresta('a3', 'B', 'C')
g_l1.adicionaAresta('a4', 'C', 'A')
g_l1.adicionaAresta('a5', 'C', 'D')

g_l1.dijkstra('A', 'D')

