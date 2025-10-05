import pygame
import sys

def mostrar_game_over(screen, fondo, j):
    """
    Muestra una pantalla de Game Over con botones clicables para Reiniciar o Salir.
    Retorna 'reiniciar' o 'salir' según la elección del jugador.
    """
    fuente_titulo = pygame.font.SysFont(None, 60)
    fuente_opcion = pygame.font.SysFont(None, 40)
    clock = pygame.time.Clock()

    # Mensaje principal según las vidas
    if j.vidas <= 0:
        mensaje = "¡Aninati kp... emanoma katu, ndereikói ni 25 segundo!"
    elif j.vidas < 3:
        mensaje = "¡Nde vale! Pero ndepya’e rupinde."
    else:
        mensaje = "¡Eikoite, ejogua héroe del Chaco pe!"

    # Opciones del menú
    opciones = ["Reiniciar", "Salir"]
    botones = []

    # Crear rectángulos de botones
    for i, texto in enumerate(opciones):
        render = fuente_opcion.render(texto, True, (255, 255, 255))
        rect = render.get_rect(center=(640, 400 + i * 60))
        botones.append((rect, texto, render))

    while True:
        screen.blit(fondo, (0, 0))

        # --- Título y mensaje ---
        titulo = fuente_titulo.render("GAME OVER", True, (0, 0, 0))
        mensaje_txt = fuente_opcion.render(mensaje, True, (0, 0, 0))
        rect_titulo = titulo.get_rect(center=(640, 200))
        rect_mensaje = mensaje_txt.get_rect(center=(640, 280))
        screen.blit(titulo, rect_titulo)
        screen.blit(mensaje_txt, rect_mensaje)

        # --- Dibujar botones ---
        mouse_pos = pygame.mouse.get_pos()
        for rect, texto, render in botones:
            # Cambia de color si el mouse está sobre el botón
            color = (255, 0, 0) if rect.collidepoint(mouse_pos) else (0, 0, 0)
            render = fuente_opcion.render(texto, True, color)
            screen.blit(render, rect)

        pygame.display.flip()

        # --- Manejo de eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for rect, texto, _ in botones:
                    if rect.collidepoint(event.pos):
                        if texto == "Reiniciar":
                            return "reiniciar"
                        elif texto == "Salir":
                            return "salir"

        clock.tick(30)