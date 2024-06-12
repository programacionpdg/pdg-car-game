import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Crear la pantalla del juego
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Esquivar objetos")

# Reloj para controlar la velocidad de actualización
reloj = pygame.time.Clock()

imagen_jugador = pygame.image.load("sprites/auto.png").convert_alpha()
imagen_jugador = pygame.transform.scale(imagen_jugador, (100, 100))

imagen_enemigo = pygame.image.load("sprites/rocket.png").convert_alpha()
imagen_enemigo = pygame.transform.scale(imagen_enemigo, (20, 40))

# Clase para el objeto del jugador
class ObjetoJugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = imagen_jugador
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 70)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += 5

# Clase para los objetos enemigos
class ObjetoEnemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 60))
        self.image.fill(ROJO)
        self.image = imagen_enemigo
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = random.randint(-150, -50)
        self.velocidad = random.randint(5, 8)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.rect.x = random.randint(0, ANCHO - self.rect.width)
            self.rect.y = random.randint(-150, -50)
            self.velocidad = random.randint(5, 15)

# Crear los grupos de sprites
todos_los_sprites = pygame.sprite.Group()
objetos_enemigos = pygame.sprite.Group()

# Crear el objeto del jugador
jugador = ObjetoJugador()
todos_los_sprites.add(jugador)

# Crear objetos enemigos
for _ in range(10):
    enemigo = ObjetoEnemigo()
    todos_los_sprites.add(enemigo)
    objetos_enemigos.add(enemigo)

# Bucle principal del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar los sprites
    todos_los_sprites.update()

    # Comprobar colisiones
    if pygame.sprite.spritecollideany(jugador, objetos_enemigos):
        jugando = False

    # Dibujar y actualizar la pantalla
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)
    pygame.display.flip()

    # Controlar la velocidad de actualización
    reloj.tick(60)

pygame.quit()
