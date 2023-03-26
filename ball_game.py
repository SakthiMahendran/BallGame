import pygame
import sys

size = width, height = 1000, 600
speed = [2, 2]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing ball")
ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball_rect = ball_rect.move(speed)

    if ball_rect.left<0 or ball_rect.right > width:
        speed[0] = -speed[0]

    if ball_rect.top<0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill("white")
    screen.blit(ball, ball_rect)
    pygame.display.flip()
