import pygame
from pygame.time import Clock
from random import randint
import time

class Player():
    def __init__(self, display) -> None:
        self.speed = 1
        self.player_color = (36, 60, 74)
        self.display = display

        self.player = pygame.Surface((150, 30))
        self.player.fill(self.player_color)
    
        self.player_x = 1000 / 2 - self.player.get_width() / 2
        self.player_y = 700 - 50

    def spawn_player(self):
        return self.player
    
    def move(self, direction):
        if direction == 'left' and self.player_x != 0:
            self.player_x -= self.speed
        elif direction == 'right' and self.player_x != 850:
            self.player_x += self.speed
        

class Fruit():
    speed = 0.3
    def __init__(self) -> None:
        self.fruit = pygame.Surface((30, 30))
        self.fruit.fill((237, 52, 77))
        self.y = randint(-100, 0)
        self.x = randint(0, 1000)
    
    def move(self):
        self.y += self.speed
    

class Game():

    def __init__(self) -> None:
        pygame.init()
        self.clock = Clock()
        self.display = pygame.display.set_mode((1000, 700))
        self.points = 0
        self.font = pygame.font.Font('fonts/Montserrat-VariableFont_wght.ttf', 50)
        pygame.display.set_caption('Frutomania')
        
        self.running = True
        self.start_game()
    
    def start_game(self):

        player = Player(self.display)
        add_fruit_speed = False
        fruits = []

        while self.running:
            pygame.display.update()
            self.display.fill((0, 0, 0))
            self.display.blit(player.player, (player.player_x, player.player_y))
            self.display.blit(
                self.font.render(f'XP: {self.points}', True, (255, 255, 255)),
                (20, 20)

            )

            if self.points % 100 == 0 and self.points != 0 and add_fruit_speed:
                Fruit.speed += 0.02
                add_fruit_speed = False

            if len(fruits) < 3:     
                fruits.append(Fruit())

            
            for fruit in fruits:
                self.display.blit(fruit.fruit, (fruit.x, fruit.y))
                fruit.move()
                if fruit.y >= 950:
                    if self.points > 1000: self.points -= 50
                    elif self.points > 800: self.points -= 40
                    elif self.points > 500: self.points -= 30
                    elif self.points > 300: self.points -= 20
                    elif self.points > 100: self.points -= 10
                    else: self.points -= 5

                    del fruits[fruits.index(fruit)]
                if (player.player_x <= fruit.x <= player.player_x + player.player.get_width() and 
                    player.player_y + player.player.get_height() >=  fruit.y >= player.player_y):
                    self.points += 10
                    add_fruit_speed = True
                    del fruits[fruits.index(fruit)]


            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player.move('left')
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player.move('right')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            


if __name__ == "__main__":
    game = Game()
