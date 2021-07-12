from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from time import sleep

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vertices_nao_adjacentes = []

        for v in self.N:
            vertices_adjacentes = []
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == v:
                    vertices_adjacentes.append(v2)
                elif v2 == v:
                    vertices_adjacentes.append(v1)

            for vt in self.N:
                if vt != v and vt not in vertices_adjacentes:
                    a_test_1 = f'{v}-{vt}'
                    a_test_2 = f'{vt}-{v}'
                    if a_test_1 not in vertices_nao_adjacentes and a_test_2 not in vertices_nao_adjacentes:
                        vertices_nao_adjacentes.append(f'{v}-{vt}')

            vertices_adjacentes = []

        return vertices_nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                return True

        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''


        vertices_adjacentes = []

        verticeExiste = False

        for vt in self.N:
            if vt == V:
                verticeExiste = True
                vertices_adjacentes = []
                for a in self.A:
                    v1 = self.A[a].getV1()
                    v2 = self.A[a].getV2()
                    if v1 == vt:
                        vertices_adjacentes.append(v2)
                    if v2 == vt:
                        vertices_adjacentes.append(v1)

        if len(vertices_adjacentes) == 0 and verticeExiste == False:
            raise VerticeInvalidoException('O vértice ' + V + ' não existe no grafo')
        else:
            return len(vertices_adjacentes)



    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        
        for a1 in self.A:
            v1_a1 = self.A[a1].getV1()
            v2_a1 = self.A[a1].getV2()
            
            a1_str = f'{v1_a1}-{v2_a1}'
            a1_str_swap = f'{v2_a1}-{v1_a1}'

            for a2 in self.A:
                if a1 != a2:
                    v1_a2 = self.A[a2].getV1()
                    v2_a2 = self.A[a2].getV2()
                    a2_str = f'{v1_a2}-{v2_a2}'
                    a2_str_swap = f'{v2_a2}-{v1_a2}'

                    if a1_str == a2_str or a1_str == a2_str_swap or a2_str == a1_str_swap:
                        return True

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        arestas_adjacentes = []

        verticeExiste = False

        for vt in self.N:
            if vt == V:
                verticeExiste = True
                for a in self.A:
                    v1 = self.A[a].getV1()
                    v2 = self.A[a].getV2()
                    if v1 == vt or v2 == vt:
                        if a not in arestas_adjacentes:
                            arestas_adjacentes.append(a)

        if len(arestas_adjacentes) == 0 and verticeExiste == False:
            raise VerticeInvalidoException('O vértice ' + V + ' não existe no grafo')
        else:
            return arestas_adjacentes


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas():
            return False

        else:
            totalVertices = len(self.N)
            for v in self.N:
                if self.grau((v)) == totalVertices-1:
                    continue
                else:
                    return False

            return True


    def dfs(self, V=''):
        '''
        Realiza uma busca em profundidade (DFS) a partir do vértice especificado.
        :return: Um grafo contendo a árvore de busca ou árvore DFS 
        '''


        finalizada = False

        vertices_examinados = {}


        for vt in self.N:
            vertices_examinados[vt] = {
            'examinado': False,
            'pai': '',
            'arestas': []
        }

        vertices_examinados[V] = {
            'examinado': True,
            'pai': V,
            'arestas': []
        }
        

        arestas_examinadas = []
        arestas_de_retorno = []

        vertice_atual = V

        comeco = True

        grafo_final = MeuGrafo()

        grafo_final.adicionaVertice(vertice_atual)

        while(finalizada != True):
            sleep(0.1)
            print(vertices_examinados[vertice_atual])
            if vertices_examinados[vertice_atual]['examinado'] == True and vertice_atual != V:
                vertice_atual == vertices_examinados[V]['pai']
                continue

            elif comeco == False and vertice_atual == V:
                finalizada = True

            else:
                comeco = False
                vertices_examinados[vertice_atual]['arestas'] = self.arestas_sobre_vertice(vertice_atual)
                todas_arestas_examinadas = False

                qtd_arestas_incidentes = len(vertices_examinados[vertice_atual]['arestas'])
                cont = 0
                for aresta_incidente in vertices_examinados[vertice_atual]['arestas']:
                    cont += 1
                    if aresta_incidente not in arestas_examinadas:
                        todas_arestas_examinadas = False
                        v1 = self.A[aresta_incidente].getV1()
                        v2 = self.A[aresta_incidente].getV2()
                        if v1 == vertice_atual:
                            if vertices_examinados[v2]['examinado'] == False and vertices_examinados[v1]['pai'] != v2:
                                vertices_examinados[v2]['pai'] = vertice_atual
                                vertice_atual = v2
                                arestas_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                print(f'adicionei {aresta_incidente}')
                                break
                            else:
                                arestas_de_retorno.append(aresta_incidente)
                                if cont == qtd_arestas_incidentes:
                                    todas_arestas_examinadas = True
                                continue

                        elif v2 == vertice_atual:
                            if vertices_examinados[v1]['examinado'] == False and vertices_examinados[v2]['pai'] != v1:
                                vertices_examinados[v1]['pai'] = vertice_atual
                                vertice_atual = v1
                                arestas_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                print(f'adicionei {aresta_incidente}')
                                break
                            else:
                                arestas_de_retorno.append(aresta_incidente)
                                if cont == qtd_arestas_incidentes:
                                    todas_arestas_examinadas = True
                                continue

                    todas_arestas_examinadas = True
                
                if todas_arestas_examinadas:
                    vertices_examinados[vertice_atual]['examinado'] = True
                    vertice_atual = vertices_examinados[vertice_atual]['pai']
                    continue
                
                else:
                    continue

        return grafo_final