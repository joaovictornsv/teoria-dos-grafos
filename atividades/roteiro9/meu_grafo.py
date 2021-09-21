from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from time import sleep

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):
    def clone_grafo(self):
        grafo_clone = deepcopy(self)

        return grafo_clone


    def removeVertice(self, v):
        if self.existeVertice(v):

            index = 0

            for i in range(len(self.N)):
                if self.N[i] == v:
                    index = i
                    break
            
            self.M.pop(index)

            for j in range(len(self.M)):
                self.M[j].pop(index)
            
            self.N.pop(index)

        else:
            raise VerticeInvalidoException('O vértice {} não existe no grafo.'.format(v))

    def vertices_isolados(self):
        isolados = []
        for i in range(len(self.M)):
            eh_pre_requisito = False
            for j in range(len(self.M)):
                if len(self.M[i][j]) > 0:
                    eh_pre_requisito = True
                    break

            tem_requisitos = False
            for j in range(len(self.M)):
                if len(self.M[j][i]) > 0:
                    tem_requisitos = True
                    break
            
            if not eh_pre_requisito and not tem_requisitos:
                isolados.append(self.N[i])

        return isolados


    def fontes(self):
        fontes = []
        for i in range(len(self.M)):
            ehFonte = True
            for j in range(len(self.M)):
                if len(self.M[j][i]) > 0:
                    ehFonte = False
                    break
            
            if ehFonte:
                fontes.append(self.N[i])
        
        return fontes

    
    def kahn(self):
        grafo_copia = self.clone_grafo()

        # isolados = grafo_copia.vertices_isolados()

        # for v in isolados:
        #     grafo_copia.removeVertice(v)

        fim_algoritmo = False

        ordenacao = []
        while(not fim_algoritmo):
            fontes = grafo_copia.fontes()
            for v in fontes:
                ordenacao.append(v)
                grafo_copia.removeVertice(v)

            if len(grafo_copia.N) == 0:
                fim_algoritmo = True

        return ordenacao



            

