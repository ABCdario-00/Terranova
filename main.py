import pygame as pg #Importei e criei um apelido para a biblioteca base do nosso jogo (pg)
import os

os.system("cls")

#Criando a janela do jogo
pg.init()

#Criando variaveis que armazenam o tamanho da nossa janela
largura_J = 800
altura_J = 600

#Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

#Cria a janela e armazena em uma variável
tela = pg.display.set_mode((largura_J, altura_J))

#Definindo o nome da janela
pg.display.set_caption("Joguin dos maia papai rs")

#Carregando o nosso png de personagem
try:
    personagem_img = pg.image.load('bolso.png')
#tratamento de erros
except pg.error:
    print(f"Não foi possível carregar imagem 'bolso.png' ")
    print(f"Certifique-se de que o a imagem esteja na mesma página do projeto")

    #Substituindo a imagem caso ela não seja encontrada
    personagem_img = pg.Surface(50,50)
    personagem_img.fill(AZUL)


#Tamanho do personagem
altura_personagem = 80
largura_personagem = 80

#Redimensionando personagem
personagem_img_redimensionado = pg.transform.scale(personagem_img, (largura_personagem, altura_personagem))

#Posição do personagem
pos_personagem_x = 300
pos_personagem_y = 400

#Localização inicial
pos_x = 50
pos_y = 50


#Criando loop de gameplay
rodando = True

while rodando:
    # 1. Processamento de eventos
    for evento in pg.event.get():
        # If para fechar a janela quando o "X" da janela for pressionado
        if evento.type == pg.QUIT:
            rodando = False #Mudando o valor da variável de controle para acabar com o loop
            
    # 2. Atualização do jogo (sem nada por enquanto) e Desenhar na tela

    tela.fill((255, 255, 255)) #preenchendo tela com a cor branca

    #Desenhando um quadrado
    pg.draw.rect(tela, VERMELHO, (pos_x, pos_y, 100, 100))
    pg.draw.circle(tela, AZUL, (200, 200), 40)

    #Desenhando a imagem
    tela.blit(personagem_img, (pos_personagem_x, pos_personagem_y))
    
    # Atualização da tela para exibir possíveis mudanças
    pg.display.flip()

pg.quit()
     