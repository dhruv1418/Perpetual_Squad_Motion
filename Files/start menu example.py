import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Fonts
FONT = pygame.font.Font(None, 40)
FONT2 = pygame.font.Font(None, 35)
HEADING_FONT = pygame.font.Font(None, 90)
SUBHEADING_FONT = pygame.font.Font(None, 63)


# TYPING ANIMATION ----------------------------------------------------------------------------------------------

typing_sound = pygame.mixer.Sound("typing_sound.mp3")  # Replace with your sound file
typing_sound.set_volume(0.5)  # Adjust volume (0.0 to 1.0)

def draw_typing_text(screen, text, y, font, color, delay=0.06, previous_lines=[]):
    """Display text with a typing animation effect, while keeping previous lines center-aligned."""
    displayed_text = ""
    for char in text:
        displayed_text += char

        typing_sound.play()
        
        
        screen.fill(BLACK)
        for i, line in enumerate(previous_lines):
            line_surface = font.render(line, True, color)
            line_rect = line_surface.get_rect(center=(WIDTH // 2, y + i * font.get_linesize()))
            screen.blit(line_surface, line_rect)


        # Render the current line being typed
        text_surface = font.render(displayed_text, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y + len(previous_lines) * font.get_linesize()))
        screen.blit(text_surface, text_rect) 

        pygame.display.flip()
        time.sleep(delay)

def render_typing_multi_line_text(screen, text, y, font, color, delay=0.06):
    """Render multi-line text with a typing effect, retaining previous lines center-aligned."""
    lines = text.split("\n")  # Split the text into lines
    previous_lines = []
    for i, line in enumerate(lines):
        draw_typing_text(screen, line, y, font, color, delay, previous_lines)
        previous_lines.append(line)


# START MENU ---------------------------------------------------------------------------------------------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Start Menu")

# BUTTONS ------------------------------------------------------------------------------------------------------------
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, alignment="center"):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.alignment = alignment
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        # Change color on hover
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        # Render the text
        text_surface = FONT.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect()

        # Apply alignment
        if self.alignment == "center":
            text_rect.center = self.rect.center  # Center align
        elif self.alignment == "left":
            text_rect.midleft = (self.rect.left + 10, self.rect.centery)  # Left align with padding

        # Draw the text
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False
    
# Create buttons
play_button = Button("PLAY", 50, 250, 220, 50, RED, WHITE, alignment = "left")  # Shifted to the left
play_button2 = Button("PLAY", 290, 350, 220, 50, RED, WHITE, alignment = "center")
rules_button = Button("HOW TO PLAY", 50, 350, 220, 50, RED, WHITE, alignment = "left")  # Shifted to the left
how_to_play_button = Button("CREDITS", 50, 450, 220, 50, RED, WHITE, alignment = "left")  # Shifted to the left

# LOGO -------------------------------------------------------------------------------------------------------------
image = pygame.image.load("LOGO.png") 
image = pygame.transform.scale(image, (250, 250))
image_rect = image.get_rect()
image_rect.topleft = (400, 250) 

# PLAY STORY WINDOW ----------------------------------------------------------------------------------------------------------
def play_window():

    text= ('Hello Player 1! You are testing the game.\n'
           'You are playing as DAREDEVIL, savior of NEW YORK CITY.\n'
           'You are in a shipyard, being attacked by goons.\n'
           'Your mission is to defeat all enemies in fixed time,\n'
           'using only your hearing and 6th sense!\n'
           'GOOD LUCK!' )

    typing_complete = False 
    while True:
        if not typing_complete:
            screen.fill(BLACK)  

            render_typing_multi_line_text(screen, text, y=150, font=FONT2, color=WHITE, delay=0.06)
            typing_complete = True  

        if typing_complete:
            play_button2.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        pygame.display.flip()


# REAL GAME WINDOW ----------------------------------------------------------------------------------------------------------
def game_play():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        pygame.display.flip()


# RULES WINDOW ----------------------------------------------------------------------------------------------------------
def rules_window():

    text= ('Hello Player 1! You are testing the game.\n'
           '1. Use arrow keys for navigation. \n'
           '2. Use W to shoot forward. \n'
           '3 Use A to shoot left. \n'
           '4. Use D to shoot right. \n'
           '5. Use S to shoot backward. \n'
           'GOOD LUCK!' )

    typing_complete = False 
    while True:
        if not typing_complete:
            screen.fill(BLACK)  

            render_typing_multi_line_text(screen, text, y=150, font=FONT2, color=WHITE, delay=0.06)
            typing_complete = True  

        if typing_complete:
            play_button2.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        pygame.display.flip()


# CREDITS WINDOW ----------------------------------------------------------------------------------------------------------
def credits_window():

    text= ("GAME MADE BY:\n"
           "Perpetual Motion Squad\n"
           "Antara Garg\n"
           "Anoop Yadav\n"
           "Chinmay Garg\n"
           "Dhruv Prakash\n")

    typing_complete = False 
    while True:
        if not typing_complete:
            screen.fill(BLACK)  

            render_typing_multi_line_text(screen, text, y=150, font=FONT2, color=WHITE, delay=0.06)
            typing_complete = True  

        if typing_complete:
            play_button2.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        pygame.display.flip()

# MAIN LOOP -------------------------------------------------------------------------------------------------------
def main_menu():
        
    while True:

        # Render the heading
        heading_surface = HEADING_FONT.render("DEVIL'S WILL:", True, RED)
        heading_rect = heading_surface.get_rect(center=(WIDTH // 2, 100))
        screen.blit(heading_surface, heading_rect)

        # Render the subheading
        subheading_surface = SUBHEADING_FONT.render("A DAREDEVIL GAME", True, RED)
        subheading_rect = subheading_surface.get_rect(center=(WIDTH // 2, 170))
        screen.blit(subheading_surface, subheading_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if play_button.is_clicked(event):
                play_window()
                
            if rules_button.is_clicked(event):
                rules_window()
                
            if how_to_play_button.is_clicked(event):
                credits_window()

        # Draw buttons
        play_button.draw(screen)
        rules_button.draw(screen)
        how_to_play_button.draw(screen)

        # Draw the image
        screen.blit(image, image_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
