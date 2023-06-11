import pygame
import sys

# General setup
pygame.init()

# Setting up main window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Rectangles (two paddles and a ball)
ball = pygame.Rect(screen_width/2 - 15/2, screen_height/2 - 15/2, 15, 15)
paddle1 = pygame.Rect(screen_width - 20, screen_height/2 - 70/2, 10, 70)
paddle2 = pygame.Rect(10, screen_height/2 - 70/2, 10, 70)

# Game Variables
ball_speed = [2, 2]
paddle_speed = 2
score2 = 0
score1 = 0

# Font for score display
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)  # Use size 72 for end game messages

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ball movement
    ball.move_ip(ball_speed)
    if ball.left < 0:
        winner_text = big_font.render("Player 2 Wins", True, (255, 0, 0))
        screen.blit(winner_text, (screen_width/2 - winner_text.get_width()/2, screen_height/2 - winner_text.get_height()/2))
        pygame.display.flip()
        pygame.time.wait(3000) # delay to allow players to see the message
        pygame.quit()
        sys.exit()
    if ball.right > screen_width:
        winner_text = big_font.render("Player 1 Wins", True, (255, 0, 0))
        screen.blit(winner_text, (screen_width/2 - winner_text.get_width()/2, screen_height/2 - winner_text.get_height()/2))
        pygame.display.flip()
        pygame.time.wait(3000) # delay to allow players to see the message
        pygame.quit()
        sys.exit()
    if ball.top < 0 or ball.bottom > screen_height:
        ball_speed[1] *= -1

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle1.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN]:
        paddle1.move_ip(0, paddle_speed)
    if keys[pygame.K_w]:
        paddle2.move_ip(0, -paddle_speed)
    if keys[pygame.K_s]:
        paddle2.move_ip(0, paddle_speed)

    # Keeping paddles on the screen
    if paddle1.top < 0:
        paddle1.top = 0
    if paddle1.bottom > screen_height:
        paddle1.bottom = screen_height
    if paddle2.top < 0:
        paddle2.top = 0
    if paddle2.bottom > screen_height:
        paddle2.bottom = screen_height

    # Collision detection and score update
    if ball.colliderect(paddle1):
        ball_speed[0] *= -1
        score2 += 1
        # Increase ball speed and paddle speed if score is less than 10
        if(score2 <= 10):
            ball_speed[0] *= 1.1
            paddle_speed *= 1.05
    if ball.colliderect(paddle2):
        ball_speed[0] *= -1
        score1 += 1
        # Increase ball speed and paddle speed if score is less than 10
        if(score1 <= 10):
            ball_speed[0] *= 1.1
            paddle_speed *= 1.05

    # Visuals
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (200, 200, 200), paddle1)
    pygame.draw.rect(screen, (200, 200, 200), paddle2)
    pygame.draw.ellipse(screen, (200, 200, 200), ball)
    pygame.draw.aaline(screen, (200, 200, 200), (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Render score
    score_text = font.render(f"Player 1: {score1} - Player 2: {score2}", True, (200, 200, 200))
    screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)