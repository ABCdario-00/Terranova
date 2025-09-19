import pygame as pg #Importei e criei um apelido para a biblioteca base do nosso jogo (pg)
import os
import math

os.system("cls")

#Criando a janela do jogo
pg.init()

#Criando variaveis que armazenam o tamanho da nossa janela
largura_J = 1280
altura_J = 720

#Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

#Cria a janela e armazena em uma variável
tela_principal = pg.display.set_mode((largura_J, altura_J), pg.RESIZABLE)

tela_do_jogo = pg.display.set_mode((largura_J, altura_J))

#Definindo o nome da janela
pg.display.set_caption("Joguin dos maia papai rs")

#Carregando o nosso png de personagem
try:
    personagem_img = pg.image.load('bolso.png').convert_alpha()
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

personagem_img = personagem_img_redimensionado

#Posição do personagem
pos_personagem_x = 300
pos_personagem_y = 400

#Localização inicial
pos_rect_x = 50
pos_rect_y = 50
pos_circle_x = 200
pos_circle_y = 200

#Velocidade do personagem
velocidade_pers = 50

#Variável de controle da tela
is_fullscreen = False

#posição da camera
camera_y = 0
camera_x = 0

tamanho_malha = 50

#inicialização do clock
clock = pg.time.Clock()

#Criando loop de gameplay
rodando = True

while rodando:
    # 1. Processamento de eventos
    for evento in pg.event.get():
        # If para fechar a janela quando o "X" da janela for pressionado
        if evento.type == pg.QUIT:
            rodando = False #Mudando o valor da variável de controle para acabar com o loop

        #Redimensionamento da tela
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_F11:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    tela_principal = pg.display.set_mode((largura_J, altura_J), pg.FULLSCREEN)
                else:
                    tela_principal = pg.display.set_mode((largura_J, altura_J))

        if evento.type == pg.VIDEORESIZE:
            tela_principal = pg.display.set_mode((evento.w, evento.h), pg.RESIZABLE)
            
    # 2. Atualização do jogo (sem nada por enquanto) e Desenhar na tela

    dt = clock.tick(60) / 100

    #Detecção de input (pressionado) :P 
    key = pg.key.get_pressed()

    #Controle de velocidade
    deslocamento_x = 0
    deslocamento_y = 0

    #Movimentação do personagem
    if key[pg.K_a]:
        deslocamento_x -= 1

    if key[pg.K_d]:
        deslocamento_x += 1

    if key[pg.K_w]:
        deslocamento_y -= 1 

    if key[pg.K_s]:
        deslocamento_y += 1

    #Normalizando a velocidade
    if deslocamento_x != 0 and deslocamento_y != 0:
        normalizador = math.sqrt(2) #Porque ele soma as velocidades (1² + 1² = 2), então queremos fazer ela ser igual a velocidade normal
        deslocamento_x /= normalizador
        deslocamento_y /= normalizador

    #Atualização da localização
    pos_personagem_x += deslocamento_x * velocidade_pers * dt
    pos_personagem_y += deslocamento_y * velocidade_pers * dt

    camera_y = pos_personagem_x - largura_J / 2
    camera_x = pos_personagem_y - altura_J / 2

    #Virar para mira de mouse
    #Pegar posição do mouse
    mouse_x, mouse_y = pg.mouse.get_pos()

    #Pegar centro do personagem
    # centro_personagem_x = pos_personagem_x - largura_personagem / 2
    # centro_personagem_y = pos_personagem_y - altura_personagem / 2
    centro_personagem_x = largura_J / 2
    centro_personagem_y = altura_J / 2

    diferença_x = mouse_x - centro_personagem_x
    diferença_y = mouse_y - centro_personagem_y

    #Calcula o ângulo em radianos e converte para graus
    angulo = -math.degrees(math.atan2(diferença_y, diferença_x))

    #Rotaciona a imagem 
    imagem_rotacionada = pg.transform.rotate(personagem_img, angulo)

    #Obtem um novo retângulo e obtem o cento dele
    # rect_rotacionado = imagem_rotacionada.get_rect(center=(centro_personagem_x, centro_personagem_y))
    rect_rotacionado = imagem_rotacionada.get_rect(center=(centro_personagem_x, centro_personagem_y))

    tela_do_jogo.fill((255, 255, 255)) #preenchendo tela com a cor branca

    # desenhando malha em amarelo
    for x in range(int(largura_J / tamanho_malha) + 2):
        x_pos = x * tamanho_malha - (camera_y % tamanho_malha)
        pg.draw.line(tela_do_jogo, AMARELO, (x_pos, 0), (x_pos, altura_J))

    for y in range(int(altura_J / tamanho_malha) + 2):
        y_pos = y * tamanho_malha - (camera_x % tamanho_malha)
        pg.draw.line(tela_do_jogo, AMARELO, (0, y_pos), (largura_J, y_pos))

    #Desenhando um quadrado
    pg.draw.rect(tela_do_jogo, VERMELHO, (pos_rect_y - camera_y, pos_rect_x - camera_x, 100, 100))
    pg.draw.circle(tela_do_jogo, AZUL, (int(pos_circle_y - camera_y), int(pos_circle_x - camera_x)), 40)

    #Desenhando a imagem
    # tela.blit(personagem_img, (pos_personagem_x, pos_personagem_y))
    tela_do_jogo.blit(imagem_rotacionada, rect_rotacionado)

    pg.draw.rect(tela_do_jogo, (255, 255, 0), (0, 0, largura_J, altura_J), 5)

    #Escalando a tela do jogo
    tela_escalada = pg.transform.scale(tela_do_jogo, tela_principal.get_size())
    tela_principal.blit(tela_escalada, (0, 0))
    
    # Atualização da tela para exibir possíveis mudanças
    pg.display.flip()

pg.quit()