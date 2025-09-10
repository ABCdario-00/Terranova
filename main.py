import pygame as pg #Importei e criei um apelido para a biblioteca base do nosso jogo (pg)
import os

os.system("cls")

#Criando a janela do jogo
pg.init()

#Criando variaveis que armazenam o tamanho da nossa janela
largura = 800
altura = 600

#Cria a janela e armazena em uma variável
tela = pg.display.set_mode((largura, altura))

#Definindo o nome da janela
pg.display.set_caption("Joguin dos maia papai rs")

#Criando loop de gameplay
rodando = True

while rodando:
    # 1. Processamento de eventos
    for evento in pg.event.get():
        # If para fechar a janela quando o "X" da janela for pressionado
        if evento.type == pg.QUIT:
            rodando = False #Mudando o valor da variável de controle para acabar com o loop
            
    # 2. Atualização do jogo (sem nada por enquanto)
    
    # 3. Desenhar na tela
    tela.fill((255, 255, 255)) #preenchendo tela com a cor branca
    
    # Atualização da tela para exibir possíveis mudanças
    pg.display.flip()
     