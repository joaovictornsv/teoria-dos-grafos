from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from time import sleep

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):
    def clone_matriz(self):
        matriz_clone = deepcopy(self.M)

        return matriz_clone

    def clone_grafo(self):
        grafo_clone = deepcopy(self)

        return grafo_clone
    
        
    def clone_vertices(self):
        vertices_clone = deepcopy(self.N)

        return vertices_clone


    def warshall(self):
        matriz_copia = self.clone_matriz()
        tamanho_matriz = len(matriz_copia)
        
        matriz_copia_uns_e_zeros = deepcopy(matriz_copia)
        
        for i in range(tamanho_matriz):
            for j in range(tamanho_matriz):
                if len(matriz_copia_uns_e_zeros[j][i]) >= 1:
                    matriz_copia_uns_e_zeros[j][i] = 1
                else:
                    matriz_copia_uns_e_zeros[j][i] = 0

        matriz_alcancabilidade = deepcopy(matriz_copia_uns_e_zeros)

        for i in range(tamanho_matriz):
            for j in range(tamanho_matriz):
                if matriz_alcancabilidade[j][i] == 1:
                    for k in range(tamanho_matriz):
                        item_jk = matriz_alcancabilidade[j][k]
                        item_ik = matriz_alcancabilidade[i][k]

                        if item_jk >= item_ik:
                            matriz_alcancabilidade[j][k] = item_jk

                        elif item_jk < item_ik:
                            matriz_alcancabilidade[j][k] = item_ik

        return matriz_alcancabilidade


    def remove_lacos(self):
        
        for linha in self.M:
            for aresta in linha:
                if len(aresta):
                    keys = list(aresta.keys())

                    for rotulo in keys:
                        if aresta[rotulo].getV1() == aresta[rotulo].getV2():
                            del aresta[rotulo]


    def remove_paralelas(self):
        
        for linha in self.M:
            for arestas in linha:
                if len(arestas):
                    keys = list(arestas.keys())

                    for rotulo1 in keys:
                        if rotulo1 in arestas.keys():
                            aresta1_str = f'{arestas[rotulo1].getV1()}-{arestas[rotulo1].getV2()}'

                            for rotulo2 in keys:
                                if rotulo2 in arestas.keys():

                                    if rotulo1 != rotulo2:
                                        aresta2_str = f'{arestas[rotulo2].getV1()}-{arestas[rotulo2].getV2()}'

                                        if aresta1_str == aresta2_str:
                                            peso1 = arestas[rotulo1].getPeso()
                                            peso2 = arestas[rotulo2].getPeso()

                                            if peso2 >= peso1:
                                                del arestas[rotulo2]
                                            else:
                                                del arestas[rotulo1]


    def arestas_partindo_do_vertice(self, vertice):
        arestas_dict = {}
        for linha in self.M:
            for arestas in linha:
                if len(arestas):
                    keys = list(arestas.keys())

                    for rotulo in keys:
                        if arestas[rotulo].getV1() == vertice:
                            arestas_dict[rotulo] = deepcopy(arestas[rotulo])

        return arestas_dict


    def arestas_entre(self, v1, v2):
        arestas_list = []
        for linha in self.M:
            for arestas in linha:
                if len(arestas):
                    keys = list(arestas.keys())

                    for rotulo in keys:
                        if arestas[rotulo].getV1() == v1 and arestas[rotulo].getV2() == v2:
                            arestas_list.append(rotulo)

        return arestas_list





    def dijkstra(self, u, v):
        grafo_copia = self.clone_grafo()
        matriz_copia = grafo_copia.clone_matriz()
        vertices_copia = grafo_copia.clone_vertices()
        
        phis = {}
        betas = {}
        pis = {}

        w = u

        for vertice in vertices_copia:
            phis[vertice] = 0
            betas[vertice] = 'infinity'
            pis[vertice] = 0

        phis[u] = 1
        betas[u] = 0

        fim_do_algoritmo = False
        ha_caminho = True

        def getPhi(vertice):
            return phis[vertice]

        def getBeta(vertice):
            return betas[vertice]

        def getPi(vertice):
            return pis[vertice]


        def setPhi(vertice, value):
            phis[vertice] = value

        def setBeta(vertice, value):
            betas[vertice] = value

        def setPi(vertice, value):
            pis[vertice] = value


        def isBetaInfity(vertice):
            if betas[vertice] == 'infinity':
                return True
            
            return False

        def getMinorBetaWithPhiZero():
            vertices = []
            for i in phis.keys():
                if phis[i] == 0:
                    vertices.append(i)
            
            betas_filtrados = []
            
            for j in betas.keys():
                if (j in vertices) and (not isBetaInfity(j)):
                    betas_filtrados.append(j)

            if len(betas_filtrados):
                menor_beta = betas_filtrados[0]
                for v in betas_filtrados:
                    if betas[v] < betas[menor_beta]:
                        menor_beta = v

                return menor_beta
            
            else:
                return False



        def getPhisZero():
            vertices = []
            for i in phis.keys():
                if phis[i] == 0:
                    vertices.append(phis[i])
            
            return vertices


        while(not fim_do_algoritmo):
            arcos_de_w = grafo_copia.arestas_partindo_do_vertice(w)
            arcos_de_w_keys = list(arcos_de_w.keys())

            beta_w = getBeta(w)


            for arco in arcos_de_w_keys:
                r = arcos_de_w[arco].getV2()
                alpha_w_r = arcos_de_w[arco].getPeso()
                phi_r = getPhi(r)
                beta_r = getBeta(r)

                if getPhi(r) == 0 and isBetaInfity(r):
                    setBeta(r, beta_w + alpha_w_r)
                    setPi(r, w)

                elif getPhi(r) == 0 and beta_r > (beta_w + alpha_w_r):
                    setBeta(r, beta_w + alpha_w_r)
                    setPi(r, w)

            # Buscando r*
            menor_beta = getMinorBetaWithPhiZero()
            if menor_beta != False:
                setPhi(menor_beta, 1)
                w = menor_beta

                if w != v:
                    continue

                else:
                    fim_do_algoritmo = True
                    break

            else:
                ha_caminho = False
                fim_do_algoritmo = True
                break
        
        
        if not ha_caminho:
            return False
        
        else:
            lista_caminho_dijkstra_temp = []
            vertice_atual = v
            lista_completa = False
            while(not lista_completa):
                lista_caminho_dijkstra_temp.append(vertice_atual)
                if vertice_atual == u:
                    lista_completa = True
                    break
                
                aresta = grafo_copia.arestas_entre(pis[vertice_atual], vertice_atual)[0]
                lista_caminho_dijkstra_temp.append(aresta)
                vertice_atual = pis[vertice_atual]

            lista_caminho_dijkstra = []
            for i in range(len(lista_caminho_dijkstra_temp)-1, -1, -1):
                lista_caminho_dijkstra.append(lista_caminho_dijkstra_temp[i])

            return lista_caminho_dijkstra


    def dijkstra_drone(self, u, v, carga_inicial:int, carga_maxima:int, pts_recarga:list):

        grafo_copia = self.clone_grafo()
        matriz_copia = grafo_copia.clone_matriz()
        vertices_copia = grafo_copia.clone_vertices()

        grafo_copia.remove_lacos()
        grafo_copia.remove_paralelas()
        
        phis = {}
        betas = {}
        pis = {}
        carga_em = {}
        alphas = {}

        w = u

        for vertice in vertices_copia:
            phis[vertice] = 0
            betas[vertice] = 'infinity'
            pis[vertice] = 0
            carga_em[vertice] = 0

    
        phis[u] = 1
        betas[u] = 0

        carga_em[u] = carga_inicial

        vertices_recarga = pts_recarga[:]


        for vertice in vertices_recarga:
            carga_em[vertice] = carga_maxima

        fim_do_algoritmo = False
        ha_caminho = True

        def getPhi(vertice):
            return phis[vertice]

        def getBeta(vertice):
            return betas[vertice]

        def getPi(vertice):
            return pis[vertice]


        def setPhi(vertice, value):
            phis[vertice] = value

        def setBeta(vertice, value):
            betas[vertice] = value

        def setPi(vertice, value):
            pis[vertice] = value


        def isBetaInfity(vertice):
            if betas[vertice] == 'infinity':
                return True
            
            return False

        def getMinorBetaWithPhiZero():
            vertices = []
            for i in phis.keys():
                if phis[i] == 0:
                    vertices.append(i)
            
            betas_filtrados = []
            
            for j in betas.keys():
                if (j in vertices) and (not isBetaInfity(j)):
                    betas_filtrados.append(j)

            if len(betas_filtrados):
                menor_beta = betas_filtrados[0]
                for vt in betas_filtrados:
                    pi_de_vt = getPi(vt)
                    aresta_entre_pi_e_vt = grafo_copia.arestas_entre(pi_de_vt, vt)[0]

                    if (betas[vt] <= betas[menor_beta]) and (alphas[aresta_entre_pi_e_vt] <= carga_em[pi_de_vt]):
                        menor_beta = vt
                    
                        if (ehPontoDeRecarga(vt)):
                            return menor_beta


                if menor_beta == betas_filtrados[0]:
                    pi_de_menor_beta = getPi(menor_beta)
                    aresta_entre_pi_e_menor_beta = grafo_copia.arestas_entre(pi_de_menor_beta, menor_beta)[0]

                    if (alphas[aresta_entre_pi_e_menor_beta] > carga_em[pi_de_menor_beta]):
                        menor_beta = False
                        return menor_beta

                    if (alphas[aresta_entre_pi_e_menor_beta] == carga_em[pi_de_menor_beta]) and (not ehPontoDeRecarga(menor_beta)) and (menor_beta != v):
                        menor_beta = False

                return menor_beta
            
            else:
                return False

        def getPhisZero():
            vertices = []
            for i in phis.keys():
                if phis[i] == 0:
                    vertices.append(phis[i])
            
            return vertices

        def ehPontoDeRecarga(v):
            if v in vertices_recarga:
                return True
            
            return False


        while(not fim_do_algoritmo):
            arcos_de_w = grafo_copia.arestas_partindo_do_vertice(w)
            arcos_de_w_keys = list(arcos_de_w.keys())

            beta_w = getBeta(w)


            for arco in arcos_de_w_keys:
                r = arcos_de_w[arco].getV2()
                alpha_w_r = arcos_de_w[arco].getPeso()
                alphas[arco] = alpha_w_r

                if not ehPontoDeRecarga(r):
                    carga_em[r] = carga_em[w] - alpha_w_r

                phi_r = getPhi(r)
                beta_r = getBeta(r)

                if getPhi(r) == 0 and isBetaInfity(r):
                    setBeta(r, beta_w + alpha_w_r)
                    setPi(r, w)

                elif getPhi(r) == 0 and beta_r > (beta_w + alpha_w_r):
                    setBeta(r, beta_w + alpha_w_r)
                    setPi(r, w)

            # Buscando r*
            menor_beta = getMinorBetaWithPhiZero()
            if menor_beta != False:
                setPhi(menor_beta, 1)
                w = menor_beta

                if w != v:
                    continue

                else:
                    fim_do_algoritmo = True
                    break

            else:
                ha_caminho = False
                fim_do_algoritmo = True
                break
        
        
        if not ha_caminho:
            return False
        
        else:
            lista_caminho_dijkstra_temp = []
            vertice_atual = v
            lista_completa = False
            while(not lista_completa):
                lista_caminho_dijkstra_temp.append(vertice_atual)
                if vertice_atual == u:
                    lista_completa = True
                    break
                
                aresta = grafo_copia.arestas_entre(pis[vertice_atual], vertice_atual)[0]
                lista_caminho_dijkstra_temp.append(aresta)
                vertice_atual = pis[vertice_atual]

            lista_caminho_dijkstra = []
            for i in range(len(lista_caminho_dijkstra_temp)-1, -1, -1):
                lista_caminho_dijkstra.append(lista_caminho_dijkstra_temp[i])

            return lista_caminho_dijkstra
