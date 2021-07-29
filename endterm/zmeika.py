import pygame 

import random 
 
pygame.init() 
 
pygame.font.init() 
font = pygame.font.SysFont("Verdana", 30) 
font_small = pygame.font.SysFont("Verdana", 20) 
game_over = font.render("Game Over", True, (0, 0, 0)) 
 
score = 0 
level = 0 
 
screen_size = (1080, 720) 
screen = pygame.display.set_mode(screen_size) 
 
pygame.display.set_caption('ZMEIKA') 
 
FPS = 60
d = 3 
 
running = True 
 
color_change1 = random.randint(0, 255) 
color_change2 = random.randint(0, 255) 
color_change3 = random.randint(0, 255) 
 
class Snake: 
    def __init__(self): 
        self.size = 1 
        self.elements = [[100, 100]] 
        self.radius = 10
        self.dx = d
        self.dy = 0 
        self.grow = False 
        self.dir = 'right' 
        self.need_to_grow = 5
 
    def draw(self): 
         
        for element in self.elements[1 : ]: 
            color_change1 = random.randint(0, 255) 
            color_change2 = random.randint(0, 255) 
            color_change3 = random.randint(0, 255) 
            pygame.draw.circle(screen, (color_change1, color_change2, color_change3), element, self.radius) 
         
        pygame.draw.circle(screen, (255, 255, 255), (self.elements[0][0], self.elements[0][1]), self.radius) 
     
 
    def move(self): 
        global running 
        if self.need_to_grow > 0: 
            self.need_to_grow -= 1 
            self.grow = True 
 
        self.elements.insert(0, [self.elements[0][0] + self.dx, self.elements[0][1] + self.dy])     
         
        if not self.grow: 
            self.elements.pop() 
        else: 
            self.grow = False 
            self.size += 1 
         
        if self.elements[0] in self.elements[1 : ]: 
            running = False 
 
class Fruit: 
 
    def __init__(self): 
        self.radius = 10 
        self.generate() 
     
    def draw(self): 
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius) 
 
 
    def generate(self): 
        global snake 
        self.x = random.randint(10, screen_size[0] - 10) 
        self.y = random.randint(10, screen_size[1] - 10) 
 
         
 
        for i in range(snake.size): 
            if(abs(snake.elements[i][0] - self.x) <= self.radius + snake.radius and abs(snake.elements[i][1] - self.y) <= self.radius + snake.radius): 
                self.generate() 
 

snake = Snake() 
fruit = Fruit() 
clock = pygame.time.Clock() 
 
 
while running: 
    Ticks = clock.tick(FPS) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
            FPS.sleep(2) 
            screen.fill() 
            screen.blit(game_over, (30, 250)) 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: 
                running = False 
            if event.key == pygame.K_LEFT and snake.dir != 'right': 
                snake.dx = -d 
                snake.dy = 0 
                snake.dir = 'left' 
            if event.key == pygame.K_RIGHT and snake.dir != 'left': 
                snake.dx = d 
                snake.dy = 0 
                snake.dir = 'right' 
            if event.key == pygame.K_UP and snake.dir != 'down': 
                snake.dx = 0 
                snake.dy = -d 
                snake.dir = 'up' 
            if event.key == pygame.K_DOWN and snake != 'up': 
                snake.dx = 0; 
                snake.dy = d 
                snake.dir = 'down' 
            if event.key == pygame.K_1: 
                snake.need_to_grow = 5 
    if snake.elements[0][0] < 0: 
        snake.elements[0][0] = screen_size[0] 
    if snake.elements[0][0] > screen_size[0]: 
        snake.elements[0][0] = 0 
    if snake.elements[0][1] < 0: 
        snake.elements[0][1] = screen_size[1] 
    if snake.elements[0][1] > screen_size[1]: 
        snake.elements[0][1] = 0 
 
 
    if(abs(snake.elements[0][0] - fruit.x) <= (fruit.radius + snake.radius) and abs(snake.elements[0][1] - fruit.y) <= (fruit.radius + snake.radius)): 
        snake.need_to_grow = 5 
        score += 10 
        if score%10==0: 
            FPS += 50 
            level += 1 
        fruit.generate() 
     
 
    scoretext = font.render("Score = "+str(score), 1, (207, 38, 233)) 
    leveltext = font.render("Level = "+str(level), 1, (207, 38, 233)) 
     
    snake.move() 
    screen.fill((0, 0, 0)) 
    screen.blit(scoretext, (5, 10)) 
    screen.blit(leveltext, (5, 40)) 
    snake.draw() 
    fruit.draw() 
    pygame.display.flip()
