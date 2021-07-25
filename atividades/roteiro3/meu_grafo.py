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
            'arestas': [],
            'ehPai': False
        }

        vertices_examinados[V] = {
            'examinado': True,
            'pai': V,
            'arestas': [],
            'ehPai': True
        }
        

        arestas_examinadas = []
        arestas_de_retorno = []

        vertice_atual = V

        comeco = True

        grafo_final = MeuGrafo()

        grafo_final.adicionaVertice(vertice_atual)

        while(finalizada != True):
            # Se o vertice já foi examinado, retorne ao vértice pai
            if vertices_examinados[vertice_atual]['examinado'] == True and vertice_atual != V:
                vertice_atual == vertices_examinados[V]['pai']
                continue
            
            # Caso o algoritmo volte ao vértice de início, tendo percorrido todo o grafo
            elif comeco == False and vertice_atual == V:
                finalizada = True

            else:
                comeco = False
                # Guarda todas as arestas incidentes naquele vértice
                vertices_examinados[vertice_atual]['arestas'] = self.arestas_sobre_vertice(vertice_atual)
                todas_arestas_examinadas = False

                qtd_arestas_incidentes = len(vertices_examinados[vertice_atual]['arestas'])
                cont = 0

                # Para cada aresta faça as verificações do loop:
                for aresta_incidente in vertices_examinados[vertice_atual]['arestas']:
                    cont += 1
                    # Continue se a aresta ainda não foi examinada, ou seja, não é aresta de retorno
                    # ALTERAÇÃO = permitir voltar a aresta de retorno
                    if aresta_incidente not in arestas_examinadas:
                        todas_arestas_examinadas = False
                        # Pega v1 e v2
                        v1 = self.A[aresta_incidente].getV1()
                        v2 = self.A[aresta_incidente].getV2()
                        if v1 == v2:
                            continue

                        if v1 == vertice_atual:
                            # Verifica se v1 não veio de v2 (2a condição) e se v2 ainda não foi definido como pai de algúem (3a condicao)
                            # ALTERAÇÃO = permitir caso v2 seja pai de v1 ou v2 já foi pai de alguem

                            if vertices_examinados[v2]['examinado'] == False and vertices_examinados[v1]['pai'] != v2 and vertices_examinados[v2]['ehPai'] == False:
                                vertices_examinados[v2]['pai'] = vertice_atual
                                # Aresta pai vai aqui
                                vertices_examinados[vertice_atual]['ehPai'] = True
                                vertice_atual = v2
                                arestas_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                # Contagem de arestas soma aqui
                                break
                            else:
                                arestas_de_retorno.append(aresta_incidente)
                                if cont == qtd_arestas_incidentes:
                                    todas_arestas_examinadas = True
                                continue

                        elif v2 == vertice_atual:
                            # Verifica se v2 não veio de v1 (2a condição) e se v1 ainda não foi definido como pai de algúem (3a condicao)
                            # ALTERAÇÃO = permitir caso v1 seja pai de v1 ou v1 já foi pai de alguem
                            if vertices_examinados[v1]['examinado'] == False and vertices_examinados[v2]['pai'] != v1 and vertices_examinados[v1]['ehPai'] == False:
                                vertices_examinados[v1]['pai'] = vertice_atual
                                 # Aresta pai vai aqui
                                vertices_examinados[vertice_atual]['ehPai'] = True
                                vertice_atual = v1
                                arestas_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                # Contagem de arestas soma aqui

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

    

    def bfs(self, V=''):
        '''
        Realiza uma busca em largura (BFS) a partir do vértice especificado.
        :return: Um grafo contendo a árvore de busca ou árvore BFS 
        '''
        finalizada = False

        vertices_examinados = {}

        for vt in self.N:
            vertices_examinados[vt] = {
                'examinado': False,
                'root': False,
                'pai': False,
                'temPai': False,
                'arestaPai': ''
            }

        vertices_examinados[V] = {
            'examinado': True,
            'root': True,
            'pai': V,
            'temPai': True,
            'arestaPai': ''
        }
        

        vertice_atual = V

        comeco = True

        grafo_final = MeuGrafo()


        fila_vertices = []

        while (finalizada == False):
            arestas_incidentes = self.arestas_sobre_vertice(vertice_atual)
            for a in arestas_incidentes:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == vertice_atual:
                    if not vertices_examinados[v2]['temPai']:
                        vertices_examinados[v2]['pai'] = v1
                        vertices_examinados[v2]['temPai'] = True
                        vertices_examinados[v2]['arestaPai'] = a

                    if vertices_examinados[v2]['examinado'] == False and v2 not in fila_vertices:
                        fila_vertices.append(v2)

                if v2 == vertice_atual:
                    if not vertices_examinados[v1]['temPai']:
                        vertices_examinados[v1]['pai'] = v2
                        vertices_examinados[v1]['temPai'] = True
                        vertices_examinados[v1]['arestaPai'] = a

                    if vertices_examinados[v1]['examinado'] == False and v1 not in fila_vertices:
                        fila_vertices.append(v1)

            vertices_examinados[vertice_atual]['examinado'] = True

            if vertices_examinados[vertice_atual]['examinado']:
                grafo_final.adicionaVertice(vertice_atual)

            if vertices_examinados[vertice_atual]['root'] == False:
                v_pai = vertices_examinados[vertice_atual]['pai']
                aresta_do_pai = vertices_examinados[vertice_atual]['arestaPai']

                grafo_final.adicionaAresta(aresta_do_pai, vertice_atual, v_pai)


            if vertice_atual in fila_vertices:
               fila_vertices.remove(vertice_atual)
               if len(fila_vertices) == 0:
                   finalizada = True
                   break

            vertice_atual = fila_vertices[0]

        return grafo_final


    def caminho_dois_vertices(self, x, y):
        finalizada = False

        vertices_examinados = {}

        for vt in self.N:
            vertices_examinados[vt] = {
                'examinado': False,
                'root': False,
                'pai': False,
                'temPai': False,
                'arestaPai': ''
            }

        vertices_examinados[x] = {
            'examinado': True,
            'root': True,
            'pai': x,
            'temPai': True,
            'arestaPai': ''
        }
        

        vertice_atual = x
        vertice_final = y
        comeco = True   

        existeCaminho = False
        tamanhoCaminho = 0
        fila_vertices = []

        while (finalizada == False):
            arestas_incidentes = self.arestas_sobre_vertice(vertice_atual)
            if len(arestas_incidentes) == 0:
                finalizada = True
                break
            
            for a in arestas_incidentes:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == vertice_atual:
                    if not vertices_examinados[v2]['temPai']:
                        vertices_examinados[v2]['pai'] = v1
                        vertices_examinados[v2]['temPai'] = True
                        vertices_examinados[v2]['arestaPai'] = a

                    if vertices_examinados[v2]['examinado'] == False and v2 not in fila_vertices:
                        fila_vertices.append(v2)

                if v2 == vertice_atual:
                    if not vertices_examinados[v1]['temPai']:
                        vertices_examinados[v1]['pai'] = v2
                        vertices_examinados[v1]['temPai'] = True
                        vertices_examinados[v1]['arestaPai'] = a

                    if vertices_examinados[v1]['examinado'] == False and v1 not in fila_vertices:
                        fila_vertices.append(v1)

                if vertice_atual == y:
                    finalizada = True
                    existeCaminho = True
                    break

            vertices_examinados[vertice_atual]['examinado'] = True

            

            if vertices_examinados[vertice_atual]['root'] == False:
                v_pai = vertices_examinados[vertice_atual]['pai']
                aresta_do_pai = vertices_examinados[vertice_atual]['arestaPai']



            if vertice_atual in fila_vertices:
               fila_vertices.remove(vertice_atual)
               if len(fila_vertices) == 0:
                   finalizada = True
                   break
            
            
            vertice_atual = fila_vertices[0]

        
        lista_final = []
        if (existeCaminho):
            lista_preenchida = False
            lista_aux = []
            v_atual = vertice_final
            while(not lista_preenchida):
                if v_atual == x:
                    lista_preenchida = True
                    break
                lista_aux.append(vertices_examinados[v_atual]['arestaPai'])
                v_atual = vertices_examinados[v_atual]['pai']

            for i in range(len(lista_aux)-1, -1, -1):
                lista_final.append(lista_aux[i])


        return [existeCaminho, len(lista_final)]


    def conexo(self):
        lista_vertices = deepcopy(self.N)
        vertice_escolhido = lista_vertices[0]
        resto_da_lista = lista_vertices[1:]

        ehConexo = True

        for v in resto_da_lista:
            if not (self.caminho_dois_vertices(vertice_escolhido, v)[0]):
                ehConexo = False
        
        return ehConexo


    def caminho_por_dfs(self, n, V):
                
        finalizada = False

        vertices_examinados = {}

        lista_vertices = deepcopy(self.N)
        

        for vt in self.N:
            vertices_examinados[vt] = {
                'examinado': False,
                'pai': '',
                'arestas': [],
                'ehPai': False,
                'arestaPai': '',
                'tamanhoAteAqui': 0
            }

        vertices_examinados[V] = {
            'examinado': True,
            'pai': V,
            'arestas': [],
            'ehPai': True,
            'arestaPai': '',
            'tamanhoAteAqui': 0
        }
        

        arestas_examinadas = []
        arestas_de_retorno = []

        vertice_atual = V
        v_atual = ''
        comeco = True

        grafo_final = MeuGrafo()

        grafo_final.adicionaVertice(vertice_atual)
        cont_arestas_examinadas = 0
        while(finalizada != True):
            # Se o vertice já foi examinado, retorne ao vértice pai
            if vertices_examinados[vertice_atual]['examinado'] == True and vertice_atual != V:
                vertice_atual == vertices_examinados[V]['pai']
                continue
            
            # Caso o algoritmo volte ao vértice de início, tendo percorrido todo o grafo
            elif comeco == False and vertice_atual == V:
                finalizada = True

            else:
                comeco = False
                # Guarda todas as arestas incidentes naquele vértice
                vertices_examinados[vertice_atual]['arestas'] = self.arestas_sobre_vertice(vertice_atual)
                todas_arestas_examinadas = False

                qtd_arestas_incidentes = len(vertices_examinados[vertice_atual]['arestas'])
                cont = 0

                # Para cada aresta faça as verificações do loop:
                for aresta_incidente in vertices_examinados[vertice_atual]['arestas']:
                    cont += 1
                    # Continue se a aresta ainda não foi examinada, ou seja, não é aresta de retorno
                    # XXXX NAO PRECISA XXXX ALTERAÇÃO = permitir voltar a aresta de retorno
                    if aresta_incidente not in arestas_examinadas:
                        todas_arestas_examinadas = False
                        # Pega v1 e v2
                        v1 = self.A[aresta_incidente].getV1()
                        v2 = self.A[aresta_incidente].getV2()
                        if v1 == vertice_atual:
                            # Verifica se v1 não veio de v2 (2a condição) e se v2 ainda não foi definido como pai de algúem (3a condicao)
                            # ALTERAÇÃO = permitir caso v2 seja pai de v1 ou v2 já foi pai de alguem

                            if vertices_examinados[v2]['examinado'] == False and vertices_examinados[v1]['pai'] != v2 and vertices_examinados[v2]['ehPai'] == False:
                                vertices_examinados[v2]['pai'] = vertice_atual
                                vertices_examinados[v2]['tamanhoAteAqui'] = vertices_examinados[vertice_atual]['tamanhoAteAqui'] + 1
                                
                                # Aresta pai vai aqui OK
                                vertices_examinados[v2]['arestaPai'] = aresta_incidente
                                vertices_examinados[vertice_atual]['ehPai'] = True
                                vertice_atual = v2
                                arestas_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                # Contagem de arestas soma aqui
                                if vertices_examinados[v2]['tamanhoAteAqui'] == n:
                                    finalizada = True
                                    v_atual = v2
                               
                                break
                            else:
                                arestas_de_retorno.append(aresta_incidente)
                                if cont == qtd_arestas_incidentes:
                                    todas_arestas_examinadas = True
                                continue

                        elif v2 == vertice_atual:
                            # Verifica se v2 não veio de v1 (2a condição) e se v1 ainda não foi definido como pai de algúem (3a condicao)
                            # ALTERAÇÃO = permitir caso v1 seja pai de v1 ou v1 já foi pai de alguem
                            if vertices_examinados[v1]['examinado'] == False and vertices_examinados[v2]['pai'] != v1 and vertices_examinados[v1]['ehPai'] == False:
                                vertices_examinados[v1]['pai'] = vertice_atual
                                vertices_examinados[v1]['tamanhoAteAqui'] = vertices_examinados[vertice_atual]['tamanhoAteAqui'] + 1
                                
                                # Aresta pai vai aqui OK
                                vertices_examinados[v1]['arestaPai'] = aresta_incidente  
                                vertices_examinados[vertice_atual]['ehPai'] = True
                                vertice_atual = v1
                                arestas_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                
                                if vertices_examinados[v1]['tamanhoAteAqui'] == n:
                                    finalizada = True
                                    v_atual = v1
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

        lista_preenchida = False
        lista_aux = []
        lista_final = []
        if v_atual == '':
            raise ValueError('Tamanho de caminho não encontrado')
        while(not lista_preenchida):
            lista_aux.append(v_atual)
            if v_atual == V:
                lista_preenchida = True
                break
            lista_aux.append(vertices_examinados[v_atual]['arestaPai'])
            v_atual = vertices_examinados[v_atual]['pai']

        for i in range(len(lista_aux)-1, -1, -1):
            lista_final.append(lista_aux[i])

        return lista_final






    def caminho_por_bfs(self, n, V):
        finalizada = False

        lista_vertices = deepcopy(self.N)
        
        V = lista_vertices[0]
        vertices_examinados = {}

        for vt in self.N:
            vertices_examinados[vt] = {
                'examinado': False,
                'root': False,
                'pai': False,
                'temPai': False,
                'arestaPai': '',
                'tamanhoAteAqui': 0
            }

        vertices_examinados[V] = {
            'examinado': True,
            'root': True,
            'pai': V,
            'temPai': True,
            'arestaPai': '',
            'tamanhoAteAqui': 0
        }
        

        vertice_atual = V
        v_atual = ''

        comeco = True

        grafo_final = MeuGrafo()


        fila_vertices = []

        while (finalizada == False):
            arestas_incidentes = self.arestas_sobre_vertice(vertice_atual)
            for a in arestas_incidentes:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == vertice_atual:
                    if not vertices_examinados[v2]['temPai']:
                        vertices_examinados[v2]['pai'] = v1
                        vertices_examinados[v2]['tamanhoAteAqui'] = vertices_examinados[v1]['tamanhoAteAqui'] + 1
                        
                        vertices_examinados[v2]['temPai'] = True
                        vertices_examinados[v2]['arestaPai'] = a

                        if vertices_examinados[v2]['tamanhoAteAqui'] == n:
                            finalizada = True
                            v_atual = v2

                    if vertices_examinados[v2]['examinado'] == False and v2 not in fila_vertices:
                        fila_vertices.append(v2)

                if v2 == vertice_atual:
                    if not vertices_examinados[v1]['temPai']:
                        vertices_examinados[v1]['pai'] = v2
                        vertices_examinados[v1]['tamanhoAteAqui'] = vertices_examinados[v2]['tamanhoAteAqui'] + 1
                       
                        vertices_examinados[v1]['temPai'] = True
                        vertices_examinados[v1]['arestaPai'] = a

                        if vertices_examinados[v1]['tamanhoAteAqui'] == n:
                            finalizada = True
                            v_atual = v1

                    if vertices_examinados[v1]['examinado'] == False and v1 not in fila_vertices:
                        fila_vertices.append(v1)

            vertices_examinados[vertice_atual]['examinado'] = True

            if vertices_examinados[vertice_atual]['examinado']:
                grafo_final.adicionaVertice(vertice_atual)

            if vertices_examinados[vertice_atual]['root'] == False:
                v_pai = vertices_examinados[vertice_atual]['pai']
                aresta_do_pai = vertices_examinados[vertice_atual]['arestaPai']

                grafo_final.adicionaAresta(aresta_do_pai, vertice_atual, v_pai)


            if vertice_atual in fila_vertices:
               fila_vertices.remove(vertice_atual)
               if len(fila_vertices) == 0:
                   finalizada = True
                   break

            vertice_atual = fila_vertices[0]

        
        lista_preenchida = False
        lista_aux = []
        lista_final = []
        if v_atual == '':
            raise ValueError('Tamanho de caminho não encontrado')
        while(not lista_preenchida):
            lista_aux.append(v_atual)
            if v_atual == V:
                lista_preenchida = True
                break
            lista_aux.append(vertices_examinados[v_atual]['arestaPai'])
            v_atual = vertices_examinados[v_atual]['pai']

        for i in range(len(lista_aux)-1, -1, -1):
            lista_final.append(lista_aux[i])

        return lista_final


    def caminho(self, n, V = ''):
        tamanho = n
        vertice_inicio = V
        lista_vertices = deepcopy(self.N)

        if V == '':
            vertice_inicio = lista_vertices[0]

        try:
            lista_por_dfs = self.caminho_por_dfs(tamanho, vertice_inicio)
            return lista_por_dfs
        except:
            try:
                lista_por_bfs = self.caminho_por_bfs(tamanho, vertice_inicio)
                return lista_por_bfs

            except ValueError:
                return ValueError('Tamanho de caminho não encontrado')

    def ha_ciclo(self):
        lista_ciclo_final = []
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                lista_ciclo_final.append(self.A[a].getV1())
                lista_ciclo_final.append(a)
                lista_ciclo_final.append(self.A[a].getV2())
                return lista_ciclo_final
            
        # Pega o dfs, remove a condição da aresta de retorno e deixa ele seguir ate achar o vertice inicial de novo c
        # Mantém a condição de não permitir vértices repetidos, apenas se for o vértice inicial
        

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

                    if a1_str == a2_str or a1_str == a2_str_swap:
                        lista_ciclo_final.append(v1_a1)
                        lista_ciclo_final.append(a1)
                        lista_ciclo_final.append(v2_a1)
                        lista_ciclo_final.append(a2)
                        lista_ciclo_final.append(v1_a1)

                        return lista_ciclo_final

                    elif a2_str == a1_str_swap:
                        lista_ciclo_final.append(v2_a1)
                        lista_ciclo_final.append(a1)
                        lista_ciclo_final.append(v1_a1)
                        lista_ciclo_final.append(a2)
                        lista_ciclo_final.append(v2_a1)

                        return lista_final_ciclo

        lista_vertices = deepcopy(self.N)
        vertices_examinados = {}
        flag = False
        for v in lista_vertices:
            print(f'dfs em {v}')
            [grafo_final, ha_ciclo_no_grafo, vertices_examinados_no_grafo] = self.procurar_ciclo(v)
            if ha_ciclo_no_grafo:
                flag = True
                vertices_examinados = deepcopy(vertices_examinados_no_grafo)
                v_atual = v
                lista_aux = []
                passagem_pelo_v_raiz = 0
                lista_preenchida = False
                while(not lista_preenchida):
                    lista_aux.append(v_atual)
                    if v_atual == v:
                        passagem_pelo_v_raiz += 1
                        if passagem_pelo_v_raiz == 2:
                            lista_preenchida = True
                            break
                    lista_aux.append(vertices_examinados[v_atual]['arestaPai'])
                    v_atual = vertices_examinados[v_atual]['pai']

                for i in range(len(lista_aux)-1, -1, -1):
                    lista_ciclo_final.append(lista_aux[i])
                break
        
        if not flag:
            return False

        
        return lista_ciclo_final




    def procurar_ciclo(self, V):
        finalizada = False

        ha_ciclo = False


        vertices_examinados = {}
        # Pega o dfs, remove a condição da aresta de retorno e deixa ele seguir ate achar o vertice inicial de novo c
        # Mantém a condição de não permitir vértices repetidos, apenas se for o vértice inicial

        # Salvar arestas do pai
        # Setar o pai como nao examinado

        for vt in self.N:
            vertices_examinados[vt] = {
            'examinado': False,
            'pai': '',
            'arestas': [],
            'arestaPai': '',
            'ehPai': False
        }

        vertices_examinados[V] = {
            'examinado': False,
            'pai': V,
            'arestas': [],
            'arestaPai': '',
            'ehPai': False
        }
        

        vertice_atual = V
        arestas_examinadas = []
        arestas_de_retorno = []
        arestas_do_pai = self.arestas_sobre_vertice(vertice_atual)
        arestas_do_pai_examinadas = []


        comeco = True

        grafo_final = MeuGrafo()
        oi = False
        grafo_final.adicionaVertice(vertice_atual)
        while(finalizada != True):

            # Se o vertice já foi examinado, retorne ao vértice pai
            if vertices_examinados[vertice_atual]['examinado'] == True and vertice_atual != V:
                vertice_atual == vertices_examinados[V]['pai']
                continue
            
            # Caso o algoritmo volte ao vértice de início, tendo percorrido todo o grafo
            

            elif comeco == False and vertice_atual == V:
                arestas_do_vertice_atual_verificadas = True

                for a in vertices_examinados[vertice_atual]['arestas']:
                    if a not in arestas_do_pai_examinadas:
                        arestas_do_vertice_atual_verificadas = False
                
                if arestas_do_vertice_atual_verificadas: 
                    finalizada = True
                else: comeco = True

            else:
                comeco = False
                # Guarda todas as arestas incidentes naquele vértice
                vertices_examinados[vertice_atual]['arestas'] = self.arestas_sobre_vertice(vertice_atual)
                todas_arestas_examinadas = False

                qtd_arestas_incidentes = len(vertices_examinados[vertice_atual]['arestas'])
                cont = 0
                # Para cada aresta faça as verificações do loop:
                for aresta_incidente in vertices_examinados[vertice_atual]['arestas']:
                    cont += 1
                    # Continue se a aresta ainda não foi examinada, ou seja, não é aresta de retorno
                    # ALTERAÇÃO = permitir voltar a aresta de retorno
                    if aresta_incidente not in arestas_examinadas:
                        todas_arestas_examinadas = False
                        # Pega v1 e v2
                        v1 = self.A[aresta_incidente].getV1()
                        v2 = self.A[aresta_incidente].getV2()
                        if v1 == v2:
                            continue

                        if v1 == vertice_atual:
                            if (v2 == V) and (vertices_examinados[v1]['arestaPai'] != aresta_incidente):
                                
                                vertices_examinados[v2]['pai'] = vertice_atual
                                vertices_examinados[v2]['arestaPai'] = aresta_incidente
                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                finalizada = True
                                ha_ciclo = True
                                break


                            # Verifica se v1 não veio de v2 (2a condição) e se v2 ainda não foi definido como pai de algúem (3a condicao)
                            # ALTERAÇÃO = permitir caso v2 seja pai de v1 ou v2 já foi pai de alguem

                            # if v2 == V: -> SE O PROXIMO VERTICE É A RAIZ

                            if (vertices_examinados[v2]['examinado'] == False) and (vertices_examinados[v1]['pai'] != v2) and (vertices_examinados[v2]['ehPai'] == False):
                                vertices_examinados[v2]['pai'] = vertice_atual
                                vertices_examinados[v2]['arestaPai'] = aresta_incidente
                                # Aresta pai vai aqui
                                vertices_examinados[vertice_atual]['ehPai'] = True
                                vertice_atual = v2
                                
                                if aresta_incidente not in arestas_do_pai: arestas_examinadas.append(aresta_incidente)
                                else: arestas_do_pai_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                break
                            else:
                                arestas_de_retorno.append(aresta_incidente)
                                if cont == qtd_arestas_incidentes:
                                    todas_arestas_examinadas = True
                                continue

                        elif v2 == vertice_atual:
                            if (v1 == V) and (vertices_examinados[v2]['arestaPai'] != aresta_incidente):
                                vertices_examinados[v1]['pai'] = vertice_atual
                                vertices_examinados[v1]['arestaPai'] = aresta_incidente
                                grafo_final.adicionaAresta(aresta_incidente, v2, v1)
                                finalizada = True
                                ha_ciclo = True
                                break
                            # Verifica se v2 não veio de v1 (2a condição) e se v1 ainda não foi definido como pai de algúem (3a condicao)
                            # ALTERAÇÃO = permitir caso v1 seja pai de v1 ou v1 já foi pai de alguem
                            if (vertices_examinados[v1]['examinado'] == False) and (vertices_examinados[v2]['pai'] != v1) and (vertices_examinados[v1]['ehPai'] == False):
                                vertices_examinados[v1]['pai'] = vertice_atual
                                vertices_examinados[v1]['arestaPai'] = aresta_incidente
                                 # Aresta pai vai aqui
                                vertices_examinados[vertice_atual]['ehPai'] = True
                                vertice_atual = v1
                                if aresta_incidente not in arestas_do_pai: arestas_examinadas.append(aresta_incidente)
                                else: arestas_do_pai_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                # Contagem de arestas soma aqui

                                break
                            else:
                                arestas_de_retorno.append(aresta_incidente)
                                if cont == qtd_arestas_incidentes:
                                    todas_arestas_examinadas = True
                                continue

                    todas_arestas_examinadas = True
                
                if todas_arestas_examinadas:
                    if vertice_atual != V: vertices_examinados[vertice_atual]['examinado'] = True
                    else: vertices_examinados[vertice_atual]['examinado'] = False
                    vertice_atual = vertices_examinados[vertice_atual]['pai']
                    continue
                
                else:
                    continue

        return [grafo_final, ha_ciclo, vertices_examinados]
        
                            