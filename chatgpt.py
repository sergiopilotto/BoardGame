import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800  # Tamaño de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tablero Cuadrado con Casilla Central y Camino Espiral")

# Colores
PASTEL_YELLOW = (255, 239, 186)
PASTEL_RED = (255, 200, 200)
PASTEL_GREEN = (200, 255, 200)
GOLD = (255, 215, 0)  # Casilla de victoria
SOFT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)

# Tipos de eventos con símbolos
EVENT_TYPES = ["Reto", "Castigo", "Recompensa"]
event_colors = {"Reto": PASTEL_YELLOW, "Castigo": PASTEL_RED, "Recompensa": PASTEL_GREEN}
event_symbols = {"Reto": "?", "Castigo": "X", "Recompensa": "$"}

# Configuración del tablero
GRID_SIZE = 10  # Tamaño del tablero (10x10)
CASILLA_SIZE = SCREEN_WIDTH // (GRID_SIZE + 10)  # Casillas más pequeñas
NUM_CASILLAS = GRID_SIZE * GRID_SIZE

# Asignar eventos aleatorios
events = [random.choice(EVENT_TYPES) for _ in range(NUM_CASILLAS - 1)] + ["Victoria"]

# Generar el recorrido en espiral
def generate_spiral(grid_size):
    """Genera las posiciones de las casillas en un recorrido espiral."""
    spiral = [[-1] * grid_size for _ in range(grid_size)]
    x, y = 0, 0
    dx, dy = 0, 1
    for i in range(grid_size * grid_size):
        spiral[x][y] = i
        if (
            0 <= x + dx < grid_size
            and 0 <= y + dy < grid_size
            and spiral[x + dx][y + dy] == -1
        ):
            x += dx
            y += dy
        else:
            dx, dy = dy, -dx
            x += dx
            y += dy
    return spiral

spiral = generate_spiral(GRID_SIZE)

# Flatten the spiral into a list of indices to easily check adjacency
spiral_indices = [spiral[x][y] for x in range(GRID_SIZE) for y in range(GRID_SIZE) if spiral[x][y] != -1]
print(spiral_indices)

# Función para determinar si dos casillas son sucesoras o predecesoras
def is_adjacent(index1, index2):
    """Determina si dos casillas son sucesoras o predecesoras en el recorrido espiral."""
    return abs(index1 - index2) == 1 or (index1 == 0 and index2 == NUM_CASILLAS - 1)  # Casillas contiguas

# Dibujar el tablero sin separaciones entre casillas
def draw_board():
    """Dibuja el tablero cuadrado sin separaciones entre las casillas."""
    for idx, index in enumerate(spiral_indices):
        x, y = index // GRID_SIZE, index % GRID_SIZE  # Convertir el índice a coordenadas de la espiral

        # Obtener evento
        event_type = events[index]
        color = GOLD if event_type == "Victoria" else event_colors[event_type]
        symbol = "🏆" if event_type == "Victoria" else event_symbols[event_type]

        # Coordenadas de la casilla sin separación
        rect_x = y * CASILLA_SIZE + 100  # Desplazamos un poco para ajustarlo
        rect_y = x * CASILLA_SIZE + 100  # Desplazamos un poco para ajustarlo

        # Dibujar la casilla
        pygame.draw.rect(screen, color, (rect_x, rect_y, CASILLA_SIZE, CASILLA_SIZE))
        pygame.draw.rect(screen, BLACK, (rect_x, rect_y, CASILLA_SIZE, CASILLA_SIZE), 1)

        # Dibujar el número
        font = pygame.font.SysFont(None, 20)
        number_text = font.render(str(index + 1), True, BLACK)
        screen.blit(number_text, (rect_x + 5, rect_y + 5))

        # Dibujar el símbolo en el centro
        symbol_text = font.render(symbol, True, BLACK)
        text_x = rect_x + CASILLA_SIZE // 2 - 10
        text_y = rect_y + CASILLA_SIZE // 2 - 10
        screen.blit(symbol_text, (text_x, text_y))

# Bucle principal
running = True
while running:
    screen.fill(SOFT_BLUE)  # Fondo suave
    draw_board()  # Dibujar el tablero sin separaciones

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
