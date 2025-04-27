from pygame import*

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
  def__init__(self, player_image, player_x, player_y, player_speed, wight, height):
    super().__init__()
    self.image = transform.scale(image.load(player_image), (wight, height))
    self.speed = player_speed
    self.rect = self.image.get_ rect)
    self.rect.x = player_x
    self.rect.y = player_)
  def reset(self):
    window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
  def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys|K_DOWN] and self.rect.y < win_height - 80: 
      self.rect.y += self.speed
  def update_|(self):
    keys = key.get_pressed)
  if keys[K_w] and self.rect.y > 5:
    self.rect.y -= self.speed
  if keys[K_s] and self.rect. y < win _height - 80:
    self.rect.y += self.speed
#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
win_ width = 600
win_height = 500
window = display.set_ mode((win_width, win_height))
window.fill(back)
#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
#создания мяча и ракетки
racketl = Player (racket.png, 30, 200, 4, 50, 150)
racket = Player(racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font. init()
font = font. Font(None, 35)
losel = font.render('PLAYER | LOSE!', True, (180, 0, O))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
speed _x = 3
speed _y = 3
while game:
  for e in event.get():
    if e.type = QUIT:
      game = False
  if finish != True:
    window.fill(back)
    racket1.update_l()
    racket2.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
  if sprite.collide_rectracket1, ball) or sprite.collide _rect(racket2, ball):
    speed_x *= -1
    speed_y *= 1
#если мяч достигает границ экрана, меняем направление его движения
  if ball.rect.y > win_height-50 or ball.rect.y < 0:
    speed_y *= -1
#если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
  if ball.rect.x < 0:
    finish = True
    window.blit(losel, (200, 200))
    game_over = True
#Несли мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
  if ball.rect.x > win_ width:
    finish = True
    window.blit(lose2, (200, 200))
    game_over = True
  racketl.reset()
  racket2.reset()
  ball.reset()
display.update()
clock.tick(FPS)
