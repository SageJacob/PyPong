import pygame, random
from pygame.locals import *

class Player:
    def __init__(self):
        self.y = 90

class Ball:
    def __init__(self):
        self.x = width // 2
        self.rise = 7 + velocity // 3
        self.run = 1 + velocity // 3
        self.y = height // 2

def collision(ball, paddles):
    for paddle in paddles:
        if ball.x > paddle[0] and ball.x < paddle[0] + 10 and ball.y > paddle[1] and ball.y < paddle[1] + 60:
            return True
    return False

def reset(ball, flag):
    ball.x = width // 2
    ball.rise = 7 + velocity // 3
    ball.run = 1 + velocity // 3
    if flag == 1:
        ball.run = -ball.run
    ball.y = height // 2

def funny_AI(player2, ball, flag):
    if ball.x < width // 2 + 10 and ball.x > width // 2 - 10:
        if player2.y < height // 2:
            player2.y += velocity
        if player2.y > height // 2:
            player2.y -= velocity
    else:
        if ball.y < player2.y + 30:
            if player2.y> 0:
                player2.y -= velocity
        if ball.y > player2.y + 30:
            if player2.y < height - 60:
                player2.y += velocity
        if ball.x <= 0 or ball.x >= 400:
            if ball.x <= 0: flag = 1
            reset(ball, flag)
            flag = 0

pygame.init()
width, height = 400, 300
velocity, flag = 15, 0
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smile, you're beautiful!")
player1 = Player()
player2 = Player()
ball = Ball()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if player1.y > 0:
            player1.y -= velocity
    if pressed[pygame.K_DOWN]:
        if player1.y < height - 60:
            player1.y += velocity
    pygame.display.flip()
    pygame.display.update()
    screen.fill((0,0,0))
    paddles = [(15, player2.y, 10, 60), (375, player1.y, 10, 60)]
    for paddle in paddles:
        pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.circle(screen, (180, 180, 180), (ball.x, ball.y), 5)
    ball.y += ball.rise
    ball.x += ball.run
    if collision(ball, paddles):
        ball.run = -ball.run
    if ball.y <= 0 or ball.y > height:
        ball.rise = -ball.rise
    funny_AI(player2, ball, flag)
