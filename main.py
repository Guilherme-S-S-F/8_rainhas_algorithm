import pygame
import sys
from genetic_algorithm import genetic_algorithm
from ant_colony_algorithm import ant_colony

# Configurações
TAM_CELULA = 60
NUM_RAINHAS = 8
LARGURA = TAM_CELULA * NUM_RAINHAS
ALTURA = TAM_CELULA * NUM_RAINHAS + 60

# Estado inicial
solucao, _ = genetic_algorithm()
algoritmo_usado = "genetic"

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Problema das 8 Rainhas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 120, 255)
CINZA = (200, 200, 200)
CINZA_ESCURO = (100, 100, 100)

# Fonte
fonte = pygame.font.SysFont(None, 24)

# Botões
botao_genetico = pygame.Rect(10, ALTURA - 45, 180, 35)
botao_ant = pygame.Rect(200, ALTURA - 45, 180, 35)

def desenhar_tabuleiro():
    for linha in range(NUM_RAINHAS):
        for coluna in range(NUM_RAINHAS):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            rect = pygame.Rect(coluna * TAM_CELULA, linha * TAM_CELULA, TAM_CELULA, TAM_CELULA)
            pygame.draw.rect(screen, cor, rect)

def desenhar_rainhas():
    cor_rainha = VERMELHO if algoritmo_usado == "genetic" else AZUL
    for coluna, linha in enumerate(solucao):
        center_x = coluna * TAM_CELULA + TAM_CELULA // 2
        center_y = linha * TAM_CELULA + TAM_CELULA // 2
        radius = TAM_CELULA // 3
        pygame.draw.circle(screen, cor_rainha, (center_x, center_y), radius)

def desenhar_botoes():
    pygame.draw.rect(screen, CINZA_ESCURO, botao_genetico)
    pygame.draw.rect(screen, CINZA_ESCURO, botao_ant)

    texto_gen = fonte.render("Usar Genético", True, BRANCO)
    texto_ant = fonte.render("Usar Ant Colony", True, BRANCO)

    screen.blit(texto_gen, (botao_genetico.x + 25, botao_genetico.y + 7))
    screen.blit(texto_ant, (botao_ant.x + 20, botao_ant.y + 7))

def main():
    global solucao, algoritmo_usado
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_genetico.collidepoint(event.pos):
                    solucao, _ = genetic_algorithm()
                    algoritmo_usado = "genetic"
                elif botao_ant.collidepoint(event.pos):
                    solucao, _ = ant_colony()
                    algoritmo_usado = "ant"

        screen.fill(CINZA)
        desenhar_tabuleiro()
        desenhar_rainhas()
        desenhar_botoes()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
