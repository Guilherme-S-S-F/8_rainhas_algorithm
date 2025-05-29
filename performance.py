import tracemalloc
import time
import sys
from genetic_algorithm import genetic_algorithm
from ant_colony_algorithm import ant_colony

NUM_SOLUCOES_UNICAS = 92

def eh_solucao_valida(solucao):
    if solucao is None or len(solucao) != 8:
        return False

    for i in range(len(solucao)):
        for j in range(i + 1, len(solucao)):
            if solucao[i] == solucao[j] or abs(solucao[i] - solucao[j]) == j - i:
                return False
    return True

def encontrar_uma_solucao(algoritmo_func):
    inicio = time.time()
    while True:
        resultado = algoritmo_func()
        if resultado is None or resultado[0] is None:
            continue

        solucao, _ = resultado
        if eh_solucao_valida(solucao):
            fim = time.time()
            return solucao, fim - inicio

def encontrar_todas_solucoes(algoritmo_func):
    inicio = time.time()
    solucoes = set()
    tentativas = 0

    while len(solucoes) < NUM_SOLUCOES_UNICAS:
        resultado = algoritmo_func()
        tentativas += 1

        if resultado is None or resultado[0] is None:
            continue

        solucao, _ = resultado
        if eh_solucao_valida(solucao):
            solucoes.add(tuple(solucao))

    fim = time.time()
    return solucoes, fim - inicio, tentativas

def calcular_custo_memoria(algoritmo_func):
    tracemalloc.start()
    resultado = algoritmo_func()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024  # Em KB

def main():
    print("Escolha o algoritmo:")
    print("1. Algoritmo Genético")
    print("2. Colônia de Formigas")

    escolha = input("Digite 1 ou 2: ")

    if escolha == '1':
        nome = "Algoritmo Genético"
        func = genetic_algorithm
    elif escolha == '2':
        nome = "Algoritmo de Colônia de Formigas"
        func = ant_colony
    else:
        print("Escolha inválida.")
        return

    print(f"\n--- Avaliando {nome} ---\n")

    solucao, tempo_uma = encontrar_uma_solucao(func)
    custo_memoria = calcular_custo_memoria(func)
    todas, tempo_todas, tentativas = encontrar_todas_solucoes(func)

    print(f"Solução válida encontrada: {solucao}")
    print(f"Tempo para uma solução: {tempo_uma:.4f} segundos")
    print(f"Custo em memória: {custo_memoria:.2f} KB")
    print(f"Tempo para encontrar as 92 soluções únicas: {tempo_todas:.2f} segundos")
    print(f"Número de tentativas até achar as 92: {tentativas}")

if __name__ == "__main__":
    main()
