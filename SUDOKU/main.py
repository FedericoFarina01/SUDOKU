import pygame
from funciones import *
from botones import *
from pantallas.inicio import dibujar_pantalla_inicio
from pantallas.principal import dibujar_pantalla_principal
from pantallas.puntajes import dibujar_pantalla_puntajes

# Inicializamos pygame
pygame.init()

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

# Cambia el título del juego
pygame.display.set_caption("Sudoku")

# Icono del juego
img_icono = pygame.image.load("SUDOKU/imagenes/icon_sudoku.png")
pygame.display.set_icon(img_icono)

# Variables de estado
juego_corriendo = True
pantalla_activa = "inicio"  
click_izq = pygame.MOUSEBUTTONDOWN

while juego_corriendo:
    # Iterar sobre todos los eventos
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            juego_corriendo = False
            pygame.quit()
            quit()

        # Detectar clics del mouse
        if evento.type == click_izq:
            cursor = pygame.mouse.get_pos()
            
            # Detectar clic en los botones de la pantalla de inicio
            if pantalla_activa == "inicio":
        
                if dibujar_boton_jugar(pantalla).collidepoint(cursor):
                    pantalla_activa = "principal"

                elif dibujar_boton_puntajes(pantalla).collidepoint(cursor):
                    pantalla_activa = "puntajes"

                elif dibujar_boton_salir(pantalla).collidepoint(cursor):
                    juego_corriendo = False
                    pygame.quit()
                    quit()

            # Detectar clic en el botón "Volver" en las pantallas "principal" o "puntajes"
            elif pantalla_activa == "principal":
                if dibujar_boton_volver(pantalla).collidepoint(cursor):
                    pantalla_activa = "inicio"

            elif pantalla_activa == "puntajes":
                if dibujar_boton_volver(pantalla).collidepoint(cursor):
                    pantalla_activa = "inicio"

    # Dibujar la pantalla correspondiente
    if pantalla_activa == "inicio":
        dibujar_pantalla_inicio(pantalla)

    elif pantalla_activa == "principal":
         dibujar_pantalla_principal(pantalla)

    elif pantalla_activa == "puntajes":
        dibujar_pantalla_puntajes(pantalla)

    pygame.display.flip()  # Actualiza la pantalla
