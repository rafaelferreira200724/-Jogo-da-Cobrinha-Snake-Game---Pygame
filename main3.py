# configurações iniciais
import pygame
import random
import sys

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha")
largura, altura = 800, 500
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# cores RGB (Mantidas as suas definições personalizadas)
preta = (0, 200, 90)
branca = (255, 0, 50)
vermelha = (210, 255, 80)
verde = (190, 0, 200)
texto_vel_cor = (255, 255, 255)
cor_game_over = (255, 0, 0)  # Vermelho marcante para o Game Over

# parametros da cobrinha
tamanho_quadrado = 20
VELOCIDADE_INICIAL = 10


def gerar_comida():
    colunas = largura // tamanho_quadrado
    linhas = altura // tamanho_quadrado
    comida_x = random.randint(0, colunas - 1) * tamanho_quadrado
    comida_y = random.randint(0, linhas - 1) * tamanho_quadrado
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])


def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {int(pontuacao)}", True, vermelha)
    tela.blit(texto, [1, 1])


def desenhar_velocidade(velocidade):
    fonte = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Velocidade: {velocidade} FPS", True, texto_vel_cor)
    tela.blit(texto, [largura - 220, 1])


# NOVO: Função para desenhar a tela de Game Over centralizada
def mostrar_tela_game_over(pontuacao):
    tela.fill((0, 0, 0))  # Fundo preto para destacar o fim do jogo

    fonte_principal = pygame.font.SysFont("Helvetica", 60, bold=True)
    fonte_secundaria = pygame.font.SysFont("Helvetica", 30)

    texto_go = fonte_principal.render("GAME OVER", True, cor_game_over)
    texto_pontos = fonte_secundaria.render(f"Pontuação Final: {pontuacao}", True, vermelha)
    texto_instrucoes = fonte_secundaria.render("Pressione C para Continuar ou S para Sair", True, texto_vel_cor)

    # Centralizando os textos na tela
    tela.blit(texto_go, [largura // 2 - texto_go.get_width() // 2, altura // 2 - 80])
    tela.blit(texto_pontos, [largura // 2 - texto_pontos.get_width() // 2, altura // 2])
    tela.blit(texto_instrucoes, [largura // 2 - texto_instrucoes.get_width() // 2, altura // 2 + 60])

    pygame.display.update()


def selecionar_velocidade(tecla, vel_x_atual, vel_y_atual):
    if tecla == pygame.K_DOWN and vel_y_atual >= 0:
        return 0, tamanho_quadrado
    if tecla == pygame.K_UP and vel_y_atual <= 0:
        return 0, -tamanho_quadrado
    if tecla == pygame.K_RIGHT and vel_x_atual >= 0:
        return tamanho_quadrado, 0
    if tecla == pygame.K_LEFT and vel_x_atual <= 0:
        return -tamanho_quadrado, 0
    return vel_x_atual, vel_y_atual


def rodar_jogo():
    fim_jogo = False
    game_over = False  # NOVO: Controla se o jogador perdeu mas está na tela de opções

    # Posições iniciais
    x = (largura // 2) // tamanho_quadrado * tamanho_quadrado
    y = (altura // 2) // tamanho_quadrado * tamanho_quadrado

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    velocidade_atual = VELOCIDADE_INICIAL

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:

        # NOVO: Loop da tela de Game Over (bloqueia o jogo até o jogador escolher C ou S)
        while game_over:
            mostrar_tela_game_over(tamanho_cobra - 1)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                    game_over = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:  # S para Sair
                        fim_jogo = True
                        game_over = False
                    if evento.key == pygame.K_c:  # C para Continuar
                        rodar_jogo()  # Reinicia chamando a função novamente
                        return  # Encerra a execução atual para não acumular na memória

        tela.fill(preta)

        # captura de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)

        # atualizar posição
        x += velocidade_x
        y += velocidade_y

        # Colisão com as paredes ativa o Game Over em vez de fechar direto
        if x < 0 or x >= largura or y < 0 or y >= altura:
            game_over = True

        # Comer a comida
        if int(x) == int(comida_x) and int(y) == int(comida_y):
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

            pontuacao_atual = tamanho_cobra - 1
            velocidade_atual = VELOCIDADE_INICIAL + (pontuacao_atual // 3) * 2

        # Atualizar os pixels do corpo da cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # Colisão com o próprio corpo ativa o Game Over
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                if velocidade_x != 0 or velocidade_y != 0:
                    game_over = True

        # desenhar elementos
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_cobra - 1)
        desenhar_velocidade(velocidade_atual)

        # atualizar a tela
        pygame.display.update()
        relogio.tick(velocidade_atual)

    pygame.quit()
    sys.exit()


rodar_jogo()