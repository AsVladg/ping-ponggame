from pygame import *
import pygame
pygame.font.init()
pygame.display.set_caption("Ping-Pong")

class Heart(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = transform.scale(image.load('heart.png'), (50, 50)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, self.rect)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont('Arial', 80)
        
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def is_clicked(self, pos, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect. y < win_height - 80:
            self.rect.y += self.speed

back = (200, 255, 255) #цвет фона (background)
win_width = 1200
win_height = 800
window = display.set_mode((win_width, win_height))
window.fill(back)
#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
#создания мяча и ракетки
racket1 = Player ('racket.png.png', 10, 200, 15, 50, 150)
racket2 = Player('racket.png.png', 1150, 200, 15, 50, 150)
ball = GameSprite('tenis_ball.png.png', 600, 350, 2, 50, 50)

count1=3
count2=3

font.init()
font = font. Font(None, 85)
losel = font.render('PLAYER 1 LOSE!', True, (150, 50, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (150, 50, 0))
hearts1 = [Heart(50 + i*60, 10) for i in range(3)]
hearts2 = [Heart(win_width - 220 + i*60, 10) for i in range(3)]

speed_x = 4
speed_y = 4

reset = Button(350, 350, 600, 100, "Перезапустить", (100, 255, 100), (150, 200, 150))

# Выносим функции проигрыша наружу
def lose_1():
    global finish
    finish = True
    window.blit(losel, (420, 280))
    reset.draw(window)

def lose_2():
    global finish
    finish = True
    window.blit(lose2, (420, 280))
    reset.draw(window)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        # Обработка клика по кнопке
        if finish and e.type == MOUSEBUTTONDOWN:
            if reset.rect.collidepoint(e.pos):
                # Сброс игры
                finish = False
                racket1.rect.y = 200
                racket2.rect.y = 200
                hearts1 = [Heart(50 + i*60, 10) for i in range(3)]
                hearts2 = [Heart(win_width - 220 + i*60, 10) for i in range(3)]
                ball.rect.x = 600
                ball.rect.y = 350
                speed_x = 4
                speed_y = 4

        if finish and e.type == MOUSEBUTTONDOWN:
            if reset.rect.collidepoint(e.pos):
                # Сброс игры
                finish = False
                racket1.rect.y = 200
                racket2.rect.y = 200
                ball.rect.x = 600
                ball.rect.y = 350
                speed_x = 4
                speed_y = 4

    if not finish:
        window.fill(back)
        
        for heart in hearts1:
            heart.draw()
        for heart in hearts2:
            heart.draw()
        
        # Рисуем счётчики
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1.1
            speed_y *= 1.1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -0.9

        if ball.rect.x < 0:
            if len(hearts1) > 0:
                hearts1.pop()
            ball.rect.x = 600
            ball.rect.y = 350
            speed_x = 4
            speed_y = 4
            if len(hearts1) == 0:
                lose_1()

        if ball.rect.x > win_width:
            if len(hearts2) > 0:
                hearts2.pop()
            ball.rect.x = 600
            ball.rect.y = 350
            speed_x = 4
            speed_y = 4
            if len(hearts2) == 0:
                lose_2()
 

        racket1.reset()
        racket2.reset()
        ball.reset()
        
    if finish:
        window.fill(back)
        window.blit(losel if len(hearts1) == 0 else lose2, (420, 280))
        reset.draw(window)

    display.update()
    clock.tick(FPS)
