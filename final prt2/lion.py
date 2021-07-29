import pygame, random, time
pygame.init()

WIDTH, HEIGHT = 600, 400     
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry lion')
FPS = pygame.time.Clock()

color = {                   # цвет
    'red' : (255, 0, 0),
    'white' : (255, 255, 255),
    'black' : (0, 0, 0),
    'green' : (0, 255, 0),
    'yellow' : (255, 255, 0),
    'blue' : (0, 0, 255)
}
 
speed, score = 10, 0         # начальная скорость и начальный score
font = pygame.font.SysFont('bookantiqua', 20)

px, py = 80, 200   # начальная позиция синего игрока
class Player(pygame.sprite.Sprite):
    def move(self):
        global px, py, speed
        keys = pygame.key.get_pressed()                     # движение синего игрока, и px > ... py < ... для того чтобы не выходил за рамки
        if keys[pygame.K_LEFT] and px > 0: px -= speed
        elif keys[pygame.K_RIGHT] and px < 590: px += speed
        elif keys[pygame.K_UP] and py > 0: py -= speed
        elif keys[pygame.K_DOWN] and py < 390: py += speed

    def draw(self):
        pygame.draw.rect(screen, color['blue'], (px, py, 10, 10))    # рисовка синего игрока

red_points = []                                       # массив для координат красных врагов
for i in range(0, 510, 100):                            # рандомные координаты для красных
    for _ in range(10):
        x, y = random.randint(i, i + 100), random.randint(0, HEIGHT)
        red_points.append([x, y])

class Enemy(pygame.sprite.Sprite):
    def draw(self):
        for i in red_points:
            pygame.draw.rect(screen, color['red'], (i[0], i[1], 15, 10))     # рисовка красных

    def move(self):
        global red_points
        for i in range(len(red_points)):                      ### плавное движение вниз красных
            red_points[i][1] += 1
    
    def spawn(self):
        global red_points
        for i in range(len(red_points)):
            if red_points[i][1] >= HEIGHT: red_points[i][1] -= HEIGHT   # красные доконца упали вниз, заново падает сверху

food_points = []                        # массив для зеленой еды и генерация рандомных позиций снизу
for i in range(10):
    food_points.append([random.randint(0, WIDTH / 2), random.randint(0, HEIGHT- 30)])
    food_points.append([random.randint(WIDTH / 2, WIDTH - 30), random.randint(0, HEIGHT - 30)])

vibr = {1 : 'L', 2 : 'R', 3 : 'U', 4 : 'D'}       # дискшинари с направлениями

class Food(pygame.sprite.Sprite):
    def draw(self):
        for i in food_points:
            pygame.draw.rect(screen, color['green'], (i[0], i[1], 15, 10))           #рисуем зеленых
    
    def move(self):                                         # def move чтобы зеленые дрожали
        global food_points, vibr
        for i in range(len(food_points)):
            x = random.randint(1, 4)                        # выбираем одну из 4х направлени
            if vibr[x] == 'L' and food_points[i][0] > 0: food_points[i][0] -= 1         # двигаем рандомно на одно направление тем самым они дрожат
            elif vibr[x] == 'R' and food_points[i][0] < 585: food_points[i][0] += 1
            elif vibr[x] == 'U' and food_points[i][1] > 0: food_points[i][1] -= 1
            elif vibr[x] == 'D' and food_points[i][1] < 390: food_points[i][1] += 1

def appetit():                      # тесты на хавчики
    global food_points, red_points, score
    i = 0                           # кушаем зеленых
    while i < len(food_points):
        if food_points[i][0] - 10 < px < food_points[i][0] + 15 and food_points[i][1] - 10 < py < food_points[i][1] + 10:       # чекаем не касались ли они друг друга
            score += 1              ### каснулся зеленого: score в плюс, код снизу убираем координату этого зеленого
            food_points.pop(i)
        else: i += 1

    i = 0
    while i < len(red_points):      # кушаем красных
        if red_points[i][0] - 10 < px < red_points[i][0] + 15 and red_points[i][1] - 10 < py < red_points[i][1] + 10:   # чек на косание на красного
            score -= 1              ### коснулся красного: score в минус, код снизу убираем координату этого красного
            red_points.pop(i)
        else: i += 1

blue = Player() # плеер это игрок синий
red = Enemy()   # енеми это враг красный
green = Food()     # фуд это еда зеленая

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(color['white'])     # заливаем экран белым

    if len(food_points) != 0:       # пока еда есть, играем в игру
        screen.blit(font.render(f'SCORE: {score}', 0, color['black']), (5, 375))    # внизу слева пишется какой сейчас score

        blue.draw()  # поечередно вызываем функций для игрового процесса
        blue.move()
        red.draw()
        red.move()
        red.spawn()
        green.draw()
        green.move()
        appetit()
    else:                           # еда кончился, пишем что игру вы закончили и результат игры
        font = pygame.font.SysFont('bookantiqua', 80)
        screen.blit(font.render('You finished', 0, color['black']), (70, 100))
        font = pygame.font.SysFont('bookantiqua', 40)
        screen.blit(font.render(f'your score: {score}', 0, color['black']), (180, 200))

    pygame.display.update()
    FPS.tick(30)

