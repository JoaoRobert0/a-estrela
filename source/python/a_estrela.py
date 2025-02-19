import time

class Grafo():
    def __init__(self, vi, vf, m):
        self.vertice_inicial = vi
        self.vertice_final = vf

class Vertice():
    def __init__(self, linha, coluna, g = 0):
        self.linha = linha
        self.coluna = coluna
        self.g = g

        self.f = "infinito"
        self.h = 0
        self.antecessor = None

    def __str__(self):
        return f"V({self.linha},{self.coluna}) - f = {self.f}"
    
    def __repr__(self):
        return self.__str__()
    
if __name__ == "__main__":
    matriz = [
       # 0  1  2  3  4  5  6  7  8  9 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 1
        [1, 0, 0, 0, 2, 1, 0, 1, 0, 1], # 2
        [1, 1, 1, 1, 0, 1, 0, 1, 0, 1], # 3
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1], # 4
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 3], # 5
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 6
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1], # 7
        [3, 1, 0, 0, 1, 0, 0, 0, 0, 1], # 8
        [1, 1, 0, 1, 0, 0, 1, 1, 1, 1], # 9
        [1, 0, 0, 0, 0, 0, 0, 3, 0, 1], # 10
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 11
    ]

    vi = Vertice(linha = 2, coluna = 4)
    vf = Vertice(linha = 5, coluna = 9)

    grafo = Grafo(vi = vi, vf = vf, m = matriz)

    while True:
        print(vi)
        visitados = []

        # O g é o mesmo para todos
        g = vi.g + 1

        # Cima
        if (matriz[vi.linha - 1][vi.coluna] == 0):
            va = Vertice(linha = vi.linha - 1, coluna = vi.coluna, g = g)

            h = abs(va.linha - vf.linha) + abs(va.coluna - vf.coluna)
            f = g + h

            if va.f == "infinito" or f < va.f:
                va.f = f
            visitados.append(va)


        # Direita
        if (matriz[vi.linha][vi.coluna + 1] == 0):
            va = Vertice(linha = vi.linha, coluna = vi.coluna + 1, g = g)

            h = abs(va.linha - vf.linha) + abs(va.coluna - vf.coluna)
            f = g + h

            if va.f == "infinito" or f < va.f:
                va.f = f
            visitados.append(va)


        # Baixo
        if (matriz[vi.linha + 1][vi.coluna] == 0):
            va = Vertice(linha = vi.linha + 1, coluna = vi.coluna, g = g)

            h = abs(va.linha - vf.linha) + abs(va.coluna - vf.coluna)
            f = g + h

            if va.f == "infinito" or f < va.f:
                va.f = f
            visitados.append(va)


        # Esquerda
        if (matriz[vi.linha][vi.coluna - 1] == 0):
            va = Vertice(linha = vi.linha, coluna = vi.coluna - 1, g = g)

            h = abs(va.linha - vf.linha) + abs(va.coluna - vf.coluna)
            f = g + h

            if va.f == "infinito" or f < va.f:
                va.f = f
            visitados.append(va)

        # Inicializa com o primeiro visitado
        try:
            menor_vertice = visitados[0]
        except Exception as e:
            raise(e)
        
        for v in visitados:
            if v.f < menor_vertice.f:
                menor_vertice = v
        
        menor_vertice.antecessor = vi
        vi = menor_vertice

        time.sleep(1)