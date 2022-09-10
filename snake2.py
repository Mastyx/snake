import pygame, sys, random, time

DARK = (0, 0, 0)
WHITE = (255, 255, 255)
MYCOLOR1 = (0, 100, 100) 
MYCOLOR2 = (200, 100, 10)
RED = (255, 0 ,0 )
GREEN = (0,255,0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SIZE = 20
class Apple:
    def __init__(self, surface):
        self.parent_screen = surface 
        self.apple_size = SIZE
        self.x =  random.randint(1, 50-1)*self.apple_size 
        self.y =  random.randint(1, 40-1)*self.apple_size
        print(self.x, self.y)
    def draw(self):
        pygame.draw.rect(self.parent_screen, RED, [self.x, self.y, self.apple_size, self.apple_size],0,8)
    def apple_move(self):
        self.x = random.randint(1, 50-1)*self.apple_size
        self.y = random.randint(1, 40-1)*self.apple_size
        print(self.x, self.y)
            
class Snake:
    def __init__(self, surface, length):
        self.parent_screen = surface
        self.velocity = SIZE
        self.block_size = SIZE
        self.direction = "down"
        self.length = length
        self.x = [SIZE]*length
        self.y = [SIZE]*length

    def draw(self):
        for i in range(self.length):
            pygame.draw.rect(self.parent_screen, 
                    WHITE, 
                    [self.x[i], self.y[i], self.block_size, self.block_size],0,2)
            pygame.draw.rect(self.parent_screen, GREEN, 
                    [self.x[0], self.y[0], self.block_size, self.block_size],0,2) 
    def move_right(self):
        self.direction = "right"
    def move_left(self):
        self.direction = "left"
    def move_up(self):
        self.direction = "up"
    def move_down(self):
        self.direction = "down"
    
    def movement_direction(self):
        for i in range(self.length-1, 0, -1):
            #ciclo inverso da self.lenght-1 a 0 passo -1
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "right":
            self.x[0] += self.velocity
        if self.direction == "left":
            self.x[0] -= self.velocity
        if self.direction == "up":
            self.y[0] -= self.velocity
        if self.direction == "down":
            self.y[0] += self.velocity

        self.draw()

    def increase_lenght(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)



class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)
        self.surface.fill(MYCOLOR1)
        self.font = pygame.font.SysFont("arial",30)
        self.speed = 0.2


        pygame.display.update()

    def pause(self):
        pause = True
        while pause: 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p: 
                        pause = False 

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)
        game.run()

    def game_over(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = False
                    if event.key == pygame.K_RETURN:
                        self.reset()
                        
            self.surface.fill(MYCOLOR2)
            font1 = pygame.font.SysFont("arial", 40)
            line1 = font1.render(f"GAME OVER", True, GREEN)
            self.surface.blit(line1, [(SCREEN_WIDTH/2-150), (SCREEN_HEIGHT/2-100)])
            font2 = pygame.font.SysFont("inconsolata", 30)
            line2 = font2.render("Press RETURN for RESTART or ESC for EXIT", True, WHITE)
            self.surface.blit(line2, [SCREEN_WIDTH/2-250, SCREEN_HEIGHT/2])

            pygame.display.update()


    def run(self):

        running = True
        while running:
            self.surface.fill(MYCOLOR1)
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()
                    if event.key == pygame.K_a:
                        self.snake.increase_lenght()
                    if event.key == pygame.K_r:
                        self.reset() 
                    if event.key == pygame.K_p:
                        msg = "Pausa [p] per ricominciare"
                        msg_pause = self.font.render(msg, True, WHITE)
                        self.surface.blit(msg_pause,(20, 20))
                        pygame.display.update()
                        self.pause()
                elif event.type == pygame.QUIT:
                    running = False

            self.snake.movement_direction()
            self.apple.draw()
            #collisione con la mela 
            if self.is_collision(
                    self.snake.x[0], self.snake.y[0],
                    self.apple.x, self.apple.y):
                self.snake.increase_lenght()
                self.apple.apple_move()
                if self.snake.length%10 == 0:
                    self.speed -= 0.02
                    print (f"{self.snake.length} - -  {self.speed} ")
            #Collisione con la coda o se stesso 
            for i in range(2, self.snake.length):
                if self.is_collision(self.snake.x[0], self.snake.y[0],
                                self.snake.x[i], self.snake.y[i]):
                    print("Collisione con se stesso")
                    running = False
            #Collisione fuori limite
            if self.snake.x[0] < 0 or self.snake.x[0] > SCREEN_WIDTH-SIZE:
                running = False
            if self.snake.y[0] < 0 or self.snake.y[0] > SCREEN_HEIGHT-SIZE:
                running = False

            #punteggio
            score = self.font.render(f"Score : {self.snake.length}", True, WHITE)
            self.surface.blit(score, (800,10))
            pygame.draw.rect(self.surface, RED, [0,0,SCREEN_WIDTH, SCREEN_HEIGHT], 1)

            pygame.display.update()
            time.sleep(self.speed)
            
        self.game_over()
#        pygame.quit()
#        sys.exit()

if __name__ == '__main__':
    game = Game()


game.run()
