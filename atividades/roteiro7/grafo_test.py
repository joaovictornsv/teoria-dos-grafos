import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        self.g_p_warshall_gabarito = [
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
        ]

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        self.g_p_sem_paralelas_warshall_gabarito = [
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
        ]

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c_warshall_gabarito = [
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0]
        ]

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c2_warshall_gabarito = [
            [0, 1],
            [0, 0]
        ]

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        # Grafo adicionado por João Victor
        # Grafo com arestas paralelas onde os vértices estão "invertidos"
        # Exemplo: a1=(A-B) e a2=(B-A)
        self.g_a_p = MeuGrafo(['A', 'B'])
        self.g_a_p.adicionaAresta('a1', 'A', 'B')
        self.g_a_p.adicionaAresta('a2', 'B', 'A')

        self.g_a_p_warshall_gabarito = [
            [1, 1],
            [1, 1]
        ]
        
        self.g_warshall = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_warshall.adicionaAresta('a1', 'A', 'B')
        self.g_warshall.adicionaAresta('a2', 'A', 'C')
        self.g_warshall.adicionaAresta('a3', 'B', 'C')
        self.g_warshall.adicionaAresta('a4', 'C', 'A')
        self.g_warshall.adicionaAresta('a5', 'C', 'D')

        self.g_warshall_warshall_gabarito = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 0]
        ]


        # Grafos gabaritos DFS
        self.g_p_dfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'T', 'M', 'Z'])
        self.g_p_dfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_J.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_J.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_J.adicionaAresta('a8', 'M', 'T')
        self.g_p_dfs_J.adicionaAresta('a9', 'T', 'Z')

        self.g_c_dfs_J = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_dfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_c_dfs_J.adicionaAresta('a4', 'E', 'C')
        self.g_c_dfs_J.adicionaAresta('a6', 'P', 'E')

        self.g_a_p_dfs_A = MeuGrafo(['A', 'B'])
        self.g_a_p_dfs_A.adicionaAresta('a1', 'A', 'B')

        self.g_l1_dfs_A = MeuGrafo(['A', 'B'])
        self.g_l1_dfs_A.adicionaAresta('a2', 'A', 'B')
        
        self.g_c2_dfs_Nina = MeuGrafo(['Nina', 'Maria'])
        self.g_c2_dfs_Nina.adicionaAresta('amiga', 'Nina', 'Maria')

        
        self.g_p_sem_paralelas_dfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a7', 'T', 'Z')

        # Grafos gabaritos BFS
        self.g_p_bfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'T', 'M', 'Z'])
        self.g_p_bfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_J.adicionaAresta('a4', 'P', 'C')
        self.g_p_bfs_J.adicionaAresta('a6', 'T', 'C')
        self.g_p_bfs_J.adicionaAresta('a7', 'M', 'C')
        self.g_p_bfs_J.adicionaAresta('a9', 'T', 'Z')

        self.g_c_bfs_J = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_bfs_J.adicionaAresta('a1','J','C')
        self.g_c_bfs_J.adicionaAresta('a2', 'J', 'E')
        self.g_c_bfs_J.adicionaAresta('a3', 'J', 'P')

        self.g_l1_bfs_A = MeuGrafo(['A', 'B'])
        self.g_l1_bfs_A.adicionaAresta('a2', 'A', 'B')

        self.g_a_p_bfs_A = MeuGrafo(['A', 'B'])
        self.g_a_p_bfs_A.adicionaAresta('a1', 'A', 'B')

        self.g_c2_bfs_Nina = MeuGrafo(['Nina', 'Maria'])
        self.g_c2_bfs_Nina.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_p_sem_paralelas_bfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a7', 'T', 'Z')


        # Grafos desconexos
        self.g_desconexo_1 = MeuGrafo(['A', 'B', 'C'])
        self.g_desconexo_1.adicionaAresta('a1', 'A', 'B')

        self.g_desconexo_2 = MeuGrafo(['A', 'B'])


        # Grafos sem ciclo
        self.g_sem_ciclo_1 = MeuGrafo(['A', 'B', 'C'])
        self.g_sem_ciclo_1.adicionaAresta('a1', 'A', 'B')
        self.g_sem_ciclo_1.adicionaAresta('a2', 'B', 'C')

        self.g_sem_ciclo_2 = MeuGrafo(['D', 'E', 'F'])
        self.g_sem_ciclo_2.adicionaAresta('a1', 'D', 'E')
        self.g_sem_ciclo_2.adicionaAresta('a2', 'D', 'F')


    def test_warshall(self):
        self.assertListEqual(self.g_p.warshall(), self.g_p_warshall_gabarito)
        self.assertListEqual(self.g_p_sem_paralelas.warshall(), self.g_p_sem_paralelas_warshall_gabarito)
        self.assertListEqual(self.g_warshall.warshall(), self.g_warshall_warshall_gabarito)
        self.assertListEqual(self.g_c.warshall(), self.g_c_warshall_gabarito)
        self.assertListEqual(self.g_c2.warshall(), self.g_c2_warshall_gabarito)
        self.assertListEqual(self.g_a_p.warshall(), self.g_a_p_warshall_gabarito)
