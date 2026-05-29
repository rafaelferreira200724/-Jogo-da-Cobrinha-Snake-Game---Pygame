# Jogo da Cobrinha (Snake Game) - Pygame

Um clássico jogo da cobrinha desenvolvido em Python utilizando a biblioteca **Pygame**. O projeto foi customizado com uma identidade visual moderna e mecânicas dinâmicas que aumentam o desafio conforme o jogador progride.

---

##  Como Jogar

1. **Iniciar:** Execute o arquivo principal do jogo. A cobra começará parada no centro da tela.
2. **Movimentação:** Use as setas do teclado para guiar a cobra:
   *  **Seta para Cima**
   * **Seta para Baixo**
   *  **Seta para Esquerda**
   *  **Seta para Direita**
3. **Objetivo:** Coma os blocos roxos (comida) para crescer e acumular pontos.
4. **Game Over:** O jogo termina se a cobra colidir com as bordas da tela ou com o seu próprio corpo.
5. **Opções de Fim de Jogo:** Na tela de Game Over:
   * Pressione **C** para reiniciar e tentar novamente.
   * Pressione **S** para fechar o jogo de forma segura.

---

## Customizações e Identidade Visual

O jogo foge do padrão verde/preto tradicional e adota uma paleta de cores vibrante e personalizada:
* **Fundo do Jogo:** Verde `(0, 200, 90)`
* **Cobra:** Vermelho `(255, 0, 50)`
* **Comida:** Roxo `(190, 0, 200)`
* **Pontuação:** Amarelo `(210, 255, 80)`

---

## Melhorias e Recursos Implementados

* **Velocidade Progressiva:** O jogo se torna mais desafiador à medida que você pontua. A velocidade inicial começa em **10 FPS** e ganha um acréscimo de **+2 FPS a cada 3 pontos** marcados.
* **Indicadores em Tempo Real:** Tela equipada com exibição de pontuação atual (canto superior esquerdo) e velocímetro do jogo (canto superior direito).
* **Bloqueio de Autocanibalismo Injusto:** A lógica de movimentação foi protegida para impedir que a cobra mude de direção diretamente para o lado oposto (ex: ir para a esquerda enquanto se move para a direita), evitando colisões acidentais consigo mesma.
* **Tela de Game Over Interativa:** Sistema de pausa no fim do jogo que exibe o placar final e permite reiniciar (`C`) ou sair (`S`) sem fechar o terminal de forma abrupta.

---

## Pré-requisitos

Antes de rodar o jogo, você precisará ter o Python e a biblioteca Pygame instalados.

```bash
# Instalar o Pygame
pip install pygame
