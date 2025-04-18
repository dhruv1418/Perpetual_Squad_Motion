import pygame
import random
import math
from pygame import mixer
import sys
import time

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Setup screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The Devil's Will")
icon = pygame.image.load('LOGO.png')
pygame.display.set_icon(icon)



def draw_rectangle(screen, x, y, width, height, color):
    rectangle = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rectangle)


# Background
background = pygame.image.load('background1.jpg')
background_mask = pygame.image.load('background1.jpg').convert()  # For pixel color detection


#boundary


# Player
playerImg = pygame.image.load('HEIF Image.jpeg.jpg')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 375
playerY = 200
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('unnamed.png')
enemyImg = pygame.transform.scale(enemyImg, (50, 50))
listpos=[(380,100), (200,192), (600,192), (380,450)]
enemyX,enemyY= random.choice(listpos)

enemyX_change = 0.3

# Bullet
bulletImg = pygame.image.load('Stick.png')
bulletImg = pygame.transform.scale(bulletImg, (20, 20))
bullet_speed = 0.3
bullets = []  # List of bullet dictionaries: {"x", "y", "dir"}

# Background music
mixer.music.load('heartbeat.mp3')
mixer.music.play(-1)

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y, direction):
    bullets.append({"x": x, "y": y, "dir": direction})

def iscollision(ax, ay, bx, by, aw=50, ah=50, bw=20, bh=20):
    rect1 = pygame.Rect(ax, ay, aw, ah)  # enemy rectangle
    rect2 = pygame.Rect(bx, by, bw, bh)  # bullet rectangle
    return rect1.colliderect(rect2)

def is_valid_position(x, y):
    try:
        color = background_mask.get_at((int(x + 10), int(y + 10)))[:3]
        return color == (0, 0, 0)  # Adjust this color based on your corridor color
    except IndexError:
        return False

def update_bullets():
    global bullets, score, enemyX, enemyY
    for bullet in bullets[:]:
        # Move bullet
        if bullet["dir"] == "up":
            bullet["y"] -= bullet_speed
        elif bullet["dir"] == "down":
            bullet["y"] += bullet_speed
        elif bullet["dir"] == "left":
            bullet["x"] -= bullet_speed
        elif bullet["dir"] == "right":
            bullet["x"] += bullet_speed

        # Remove if off-screen
        if bullet["x"] < 0 or bullet["x"] > 800 or bullet["y"] < 0 or bullet["y"] > 600:
            bullets.remove(bullet)
            continue

        # Check collision
        if iscollision(enemyX, enemyY, bullet["x"], bullet["y"]):
            bullets.remove(bullet)
            score += 1
            print("Score:", score)
            old_pos = (enemyX, enemyY)
            new_pos = random.choice([pos for pos in listpos if pos != old_pos])
            enemyX, enemyY = new_pos
            continue

        screen.blit(bulletImg, (bullet["x"], bullet["y"]))

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
   # draw_rectangle(screen, 400, 100, 50, 100, 'WHITE')


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5

            # Bullet firing in 4 directions
            player_center_x = playerX + 10  # since player is 20x20
            player_center_y = playerY + 10

            if event.key == pygame.K_a:
                fire_bullet(player_center_x, player_center_y, "left")
            if event.key == pygame.K_d:
                fire_bullet(player_center_x, player_center_y, "right")
            if event.key == pygame.K_w:
                fire_bullet(player_center_x, player_center_y, "up")
            if event.key == pygame.K_s:
                fire_bullet(player_center_x, player_center_y, "down")

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                playerY_change = 0

    #sounds

    channel=pygame.mixer.Channel(0)
    enemy_left=pygame.mixer.Sound('enemy_left.wav')
    enemy_right= pygame.mixer.Sound('enemy_right.wav')

    """ 
   def play_random_direction():
        direction = random.choice(['left', 'right'])
        if direction == 'left':
            print("🎧 Playing LEFT directional sound")
            print(score)
            channel.stop()
            channel.play(enemy_left)
        else:
            print("🎧 Playing RIGHT directional sound")
            channel.stop()
            channel.play(enemy_right)


    for i in range(5):
        print(f"🔊 Direction {i + 1}/20")
        play_random_direction()
        time.sleep(3)
        channel.stop()
        print("⏳ Silent interval")
        time.sleep(2)
    """
    # Store old position
    oldX, oldY = playerX, playerY

    # Attempt to move
    newX = playerX + playerX_change
    newY = playerY + playerY_change

    if is_valid_position(newX, newY):
        playerX, playerY = newX, newY
    else:
        playerX, playerY = oldX, oldY

    # Move enemy
    #enemyX += enemyX_change
    #if enemyX < 0 or enemyX > 750:
        #enemyX_change *= -1

    # Update bullets
    update_bullets()

    # Draw player and enemy
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
