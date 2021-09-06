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

        self.g_p_dijkstra = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dijkstra.adicionaAresta('a1', 'J', 'C')
        self.g_p_dijkstra.adicionaAresta('a2', 'C', 'E')
        self.g_p_dijkstra.adicionaAresta('a3', 'E', 'C')
        self.g_p_dijkstra.adicionaAresta('a4', 'P', 'C')
        self.g_p_dijkstra.adicionaAresta('a5', 'C', 'P')
        self.g_p_dijkstra.adicionaAresta('a6', 'C', 'T')
        self.g_p_dijkstra.adicionaAresta('a7', 'M', 'C')
        self.g_p_dijkstra.adicionaAresta('a8', 'M', 'T')
        self.g_p_dijkstra.adicionaAresta('a9', 'T', 'Z')

        self.g_p_dijkstra_J_Z_gabarito = ['J', 'a1', 'C', 'a6', 'T', 'a9', 'Z']

        self.g_p_dijkstra_drone_M_Z_gabarito = ['M', 'a8', 'T', 'a9', 'Z']
        self.g_p_dijkstra_drone_P_E_gabarito = ['P', 'a4', 'C', 'a2', 'E']

        self.g_p_dijkstra_com_pesos = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dijkstra_com_pesos.adicionaAresta('a1', 'J', 'C')
        self.g_p_dijkstra_com_pesos.adicionaAresta('a2', 'C', 'E')
        self.g_p_dijkstra_com_pesos.adicionaAresta('a3', 'E', 'C')
        self.g_p_dijkstra_com_pesos.adicionaAresta('a4', 'P', 'C')
        self.g_p_dijkstra_com_pesos.adicionaAresta('a5', 'C', 'P')
        self.g_p_dijkstra_com_pesos.adicionaAresta('a6', 'C', 'T', 8)
        self.g_p_dijkstra_com_pesos.adicionaAresta('a7', 'C', 'M')
        self.g_p_dijkstra_com_pesos.adicionaAresta('a8', 'M', 'T')
        self.g_p_dijkstra_com_pesos.adicionaAresta('a9', 'T', 'Z')

        self.g_p_dijkstra_com_pesos_J_Z_gabarito = ['J', 'a1', 'C', 'a7', 'M', 'a8', 'T', 'a9', 'Z']

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

        # Grafos testes para Dijkstra
        self.g_dijkstra1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.g_dijkstra1.adicionaAresta('a1', 'A', 'B', 1)
        self.g_dijkstra1.adicionaAresta('a2', 'B', 'C', 1)
        self.g_dijkstra1.adicionaAresta('a3', 'C', 'D', 1)
        self.g_dijkstra1.adicionaAresta('a4', 'C', 'E', 2)
        self.g_dijkstra1.adicionaAresta('a5', 'D', 'E', 3)
        self.g_dijkstra1.adicionaAresta('a6', 'E', 'G', 2)
        self.g_dijkstra1.adicionaAresta('a7', 'B', 'F', 3)
        self.g_dijkstra1.adicionaAresta('a8', 'F', 'G', 1)

        self.g_dijkstra1_A_G_gabarito = ['A', 'a1', 'B', 'a7', 'F', 'a8', 'G']
        self.g_dijkstra1_drone_A_G_gabarito = ['A', 'a1', 'B', 'a7', 'F', 'a8', 'G']
        self.g_dijkstra1_drone_A_D_gabarito = ['A', 'a1', 'B', 'a2', 'C', 'a3', 'D']

        self.g_dijkstra2 = MeuGrafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.g_dijkstra2.adicionaAresta('a1', '1', '2', 2)
        self.g_dijkstra2.adicionaAresta('a2', '1', '3', 5)
        self.g_dijkstra2.adicionaAresta('a3', '1', '4', 2)
        self.g_dijkstra2.adicionaAresta('a4', '2', '3', 3)
        self.g_dijkstra2.adicionaAresta('a5', '2', '5', 1)
        self.g_dijkstra2.adicionaAresta('a6', '3', '4', 3)
        self.g_dijkstra2.adicionaAresta('a7', '5', '3', 1)
        self.g_dijkstra2.adicionaAresta('a8', '3', '6', 1)
        self.g_dijkstra2.adicionaAresta('a9', '3', '8', 1)
        self.g_dijkstra2.adicionaAresta('a10', '4', '7', 2)
        self.g_dijkstra2.adicionaAresta('a11', '5', '9', 7)
        self.g_dijkstra2.adicionaAresta('a12', '6', '8', 1)
        self.g_dijkstra2.adicionaAresta('a13', '7', '6', 2)
        self.g_dijkstra2.adicionaAresta('a14', '8', '9', 1)

        self.g_dijkstra2_1_9_gabarito = ['1', 'a1', '2', 'a5', '5', 'a7', '3', 'a9', '8', 'a14', '9']


    def test_warshall(self):
        self.assertListEqual(self.g_p.warshall(), self.g_p_warshall_gabarito)
        self.assertListEqual(self.g_p_sem_paralelas.warshall(), self.g_p_sem_paralelas_warshall_gabarito)
        self.assertListEqual(self.g_warshall.warshall(), self.g_warshall_warshall_gabarito)
        self.assertListEqual(self.g_c.warshall(), self.g_c_warshall_gabarito)
        self.assertListEqual(self.g_c2.warshall(), self.g_c2_warshall_gabarito)
        self.assertListEqual(self.g_a_p.warshall(), self.g_a_p_warshall_gabarito)

        
    def test_dijkstra(self):
        self.assertListEqual(self.g_dijkstra1.dijkstra('A', 'G'), self.g_dijkstra1_A_G_gabarito)
        self.assertListEqual(self.g_dijkstra2.dijkstra('1', '9'), self.g_dijkstra2_1_9_gabarito)
        self.assertListEqual(self.g_p_dijkstra.dijkstra('J', 'Z'), self.g_p_dijkstra_J_Z_gabarito)
        self.assertListEqual(self.g_p_dijkstra_com_pesos.dijkstra('J', 'Z'), self.g_p_dijkstra_com_pesos_J_Z_gabarito)
        self.assertFalse(self.g_desconexo_1.dijkstra('A', 'C'))
        self.assertFalse(self.g_desconexo_2.dijkstra('A', 'B'))
        self.assertFalse(self.g_sem_ciclo_1.dijkstra('C', 'A'))
        self.assertFalse(self.g_sem_ciclo_2.dijkstra('E', 'F'))


    def test_dijkstra_drone(self):
        self.assertFalse(self.g_p.dijkstra_drone('J', 'Z', 2, 1, ['T']))
        self.assertFalse(self.g_p.dijkstra_drone('M', 'E', 1, 1, ['T']))
        self.assertFalse(self.g_p.dijkstra_drone('M', 'Z', 0, 10, ['T']))
        self.assertFalse(self.g_dijkstra1.dijkstra_drone('A', 'D', 1, 1, ['C']))
        self.assertListEqual(self.g_p.dijkstra_drone('M', 'Z', 0, 10, ['M']), self.g_p_dijkstra_drone_M_Z_gabarito)
        self.assertListEqual(self.g_p.dijkstra_drone('P', 'E', 1, 1, ['C']), self.g_p_dijkstra_drone_P_E_gabarito)
        self.assertListEqual(self.g_dijkstra1.dijkstra_drone('A', 'G', 1, 4, ['B']), self.g_dijkstra1_drone_A_G_gabarito)
        self.assertListEqual(self.g_dijkstra1.dijkstra_drone('A', 'D', 2, 1, ['C']), self.g_dijkstra1_drone_A_D_gabarito)