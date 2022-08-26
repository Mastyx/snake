import pygame, sys, random, time

DARK = (0, 0, 0)
WHITE = (255, 255, 255)
MYCOLOR1 = (0, 100, 100) 
RED = (255, 0 ,0 )
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SIZE = 20
class Apple:
    def __init__(self, surface):
        self.parent_screen = surface 
        self.apple_size = SIZE
        self.x =  random.randint(1, 50)*self.apple_size 
        self.y =  random.randint(1, 40)*self.apple_size
    def draw(self):
        pygame.draw.rect(self.parent_screen, RED, [self.x, self.y, self.apple_size, self.apple_size],0,8)
    def apple_move(self):
        self.x = random.randint(1, 50)*self.apple_size
        self.y = random.randint(1, 40)*self.apple_size
        
            
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
                    [self.x[i], self.y[i], self.block_size, self.block_size],0,3)

    
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
        self.snake = Snake(self.surface, 10)
        self.apple = Apple(self.surface)
        self.surface.fill(MYCOLOR1)

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
            self.snake.movement_direction()
            self.apple.draw()
            pygame.display.update()
            time.sleep(0.2)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
