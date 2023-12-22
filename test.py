import pygame
import sys
import random

pygame.init()


BLACK = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
couleur_fond = (0, 0, 0)
couleur_texte = (255, 255, 255)
width, height = 640, 480
cell_size = 20
fps = 15

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Le Snake de La Mort qui Tue")

def afficher_menu():
    font = pygame.font.Font(None, 36)
    texte = font.render("Appuyez sur une touche pour jouer", True, couleur_texte)
    text_rect = texte.get_rect(center=(width // 2, height // 2))
    
    screen.fill(couleur_fond)
    screen.blit(texte, text_rect)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return

def snake_game():
    snake = [(100, 100), (90, 100), (80, 100)]
    snake_dir = (cell_size, 0)
    apple = pomme()
    score = 0  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != (0, cell_size):
                    snake_dir = (0, -cell_size)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -cell_size):
                    snake_dir = (0, cell_size)
                elif event.key == pygame.K_LEFT and snake_dir != (cell_size, 0):
                    snake_dir = (-cell_size, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-cell_size, 0):
                    snake_dir = (cell_size, 0)

        snake = update_snake(snake, snake_dir)

        if snake[0] == apple:
            snake.append(snake[-1])
            score += 10  
            apple = pomme()

        if (
            snake[0][0] < 0
            or snake[0][0] >= width
            or snake[0][1] < 0
            or snake[0][1] >= height
            or snake[0] in snake[1:]
        ):
            game_over(score)

        screen.fill(BLACK)
        draw_snake(snake)
        draw_apple(apple)

        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, couleur_texte)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        pygame.time.Clock().tick(fps)

def update_snake(snake, direction):
    x, y = snake[0]
    pygame.display.flip()
    
    
    
    with open("scores.txt", "a") as file:
        file.write(f"Score: {score}\n")

afficher_menu()
snake_game()
