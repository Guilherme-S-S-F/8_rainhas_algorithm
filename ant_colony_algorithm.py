import random

N = 8
NUM_FORMIGAS = 50
NUM_ITERACOES = 1000
TAXA_EVAPORACAO = 0.1
REFORCO_FEROMONIO = 10.0

def contar_conflitos(tabuleiro_parcial):
    conflitos = 0
    for i in range(len(tabuleiro_parcial)):
        for j in range(i + 1, len(tabuleiro_parcial)):
            if tabuleiro_parcial[i] == tabuleiro_parcial[j] or abs(tabuleiro_parcial[i] - tabuleiro_parcial[j]) == j - i:
                conflitos += 1
    return conflitos


def escolher_coluna(linha, feromonio, tabuleiro):
    probabilidades = []
    total = 0

    for col in range(N):
        tabuleiro[linha] = col
        conflitos = contar_conflitos(tabuleiro[:linha + 1])
        heuristica = 1 / (1 + conflitos)
        p = feromonio[linha][col] * heuristica
        probabilidades.append(p)
        total += p

    if total == 0:
        return random.randint(0, N - 1)

    r = random.uniform(0, total)
    acum = 0
    for col in range(N):
        acum += probabilidades[col]
        if r <= acum:
            return col
    return N - 1  # fallback

def construir_solucao(feromonio):
    tabuleiro = [-1] * N
    for linha in range(N):
        col = escolher_coluna(linha, feromonio, tabuleiro)
        tabuleiro[linha] = col
    return tabuleiro

def atualizar_feromonio(feromonio, todas_solucoes):
    # Evaporação
    for i in range(N):
        for j in range(N):
            feromonio[i][j] *= (1 - TAXA_EVAPORACAO)

    # Reforço
    for solucao in todas_solucoes:
        conflitos = contar_conflitos(solucao)
        if conflitos == 0:
            incremento = REFORCO_FEROMONIO
        else:
            incremento = 1 / conflitos
        for linha, col in enumerate(solucao):
            feromonio[linha][col] += incremento

def ant_colony():
    feromonio = [[1.0 for _ in range(N)] for _ in range(N)]
    melhor_solucao = None
    melhor_conflitos = float('inf')

    for iteracao in range(NUM_ITERACOES):
        todas_solucoes = []
        for _ in range(NUM_FORMIGAS):
            solucao = construir_solucao(feromonio)
            conflitos = contar_conflitos(solucao)
            todas_solucoes.append(solucao)

            if conflitos < melhor_conflitos:
                melhor_solucao = solucao
                melhor_conflitos = conflitos
                if conflitos == 0:
                    return melhor_solucao, iteracao + 1

        atualizar_feromonio(feromonio, todas_solucoes)

    return melhor_solucao, NUM_ITERACOES
