import pygame
SCREEN_TITLE = "CrossIT"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans',75)
class Game:
    TICK_RATE = 60
    

    def __init__(self,image_path,title,width,height):
        self.title = title
        self.width = width
        self.height = height
        self.game_screen  = pygame.display.set_mode((width,height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image,(width,height))

    def run_game_loop(self,level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('player1.png', 375,700,50,50)
        enemy_0 = NonPlayerCharacter('goomba.png',20,600,50,50)
        enemy_0.SPEED *= level_speed

        enemy_1 = NonPlayerCharacter('black.png',self.width-40,400,50,50)
        enemy_1.SPEED *= level_speed

        enemy_2 = NonPlayerCharacter('br.png',20,200,50,50)
        enemy_2.SPEED *= level_speed
        treasure = GameObject('treasure.png',375,50,50,50)
        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image,(0,0))
            treasure.draw(self.game_screen)
            player_character.move(direction, self.height)
            player_character.draw(self.game_screen)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if level_speed > 1:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)
            if level_speed > 2:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)
        #pygame.draw.rect(game_screen, BLACK_COLOR, [350,350,100,100]) 
        #pygame.draw.circle(game_screen, BLACK_COLOR, (400,300),50)
        #game_screen.blit(player_image, (375,375))
            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You Lose!',True,BLACK_COLOR)
                self.game_screen.blit(text,(275,350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You Win!',True,BLACK_COLOR)
                self.game_screen.blit(text,(275,350))
                pygame.display.update()
                clock.tick(1)
                break
            pygame.display.update()
            clock.tick(self.TICK_RATE)
        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return
class GameObject:
    def __init__(self,image_path,x,y,width,height):
        
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width,height))
        self.x_pos = x
        self.y_pos = y
         
        self.width = width
        self.height = height
    def draw(self,background):
        background.blit(self.image,(self.x_pos,self.y_pos))
class PlayerCharacter(GameObject):

    SPEED = 5
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path,x,y,width,height)
    def move(self,direction,max_height):
        if direction>0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40
    def detect_collision(self,other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True
        #background.blit(self.image,(self.x_pos,self.y_pos))
        
class NonPlayerCharacter(GameObject):

    SPEED = 8
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path,x,y,width,height)
    def move(self,max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width-40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED
        
                       
pygame.init()

new_game = Game('background.jpg',SCREEN_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT)
new_game.run_game_loop(1)





pygame.quit()
quit()
