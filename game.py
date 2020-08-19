
# import pygame module in this program 
import pygame 
import random

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,   0,   0)
GREEN = (0,   255,   0)
BLUE = (0,   0,   255)

block_height = 25
no_of_blocks = 9
colors = [RED,GREEN,BLUE]

block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

def generate_blocks(rows,no_of_blocks,colors):
    bw_blocks_space = 2
    for j in range(rows):
        selected_color = random.choice(colors)
        block_y = (block_height * j) + ((j+1) * 5) 

        for i in range(no_of_blocks):
            # This represents a block
            block_width = (screen_width - no_of_blocks * bw_blocks_space ) / no_of_blocks
            block = Blocks(selected_color, block_width, block_height)

            # Set a random location for the block
            block.rect.x = (i * block_width ) + i*bw_blocks_space
            block.rect.y = block_y
            # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)
    
class Blocks(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()

        # making block data
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


# create a surface object, image is drawn on it. 
screen_width = 800
screen_height = 560
image = pygame.image.load('./galaxy.jpeg') 

pygame.init() 

screen = pygame.display.set_mode((screen_width, screen_height )) 
  
# set the pygame window name 
pygame.display.set_caption('Bricks Breaker') 
  
# create a surface object, image is drawn on it. 
image = pygame.image.load('./galaxy.jpeg') 
stick = pygame.image.load('./player.png') 
stick = pygame.transform.scale(stick, (130, 15))


generate_blocks(4,9,colors) 

# Create a RED player block
player = Blocks(RED,10, 30)
# all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Limit to 60 frames per second
clock.tick(60)

score = 0
 
# infinite loop 
while not done : 
  

    # (0, 0) coordinate. 
    screen.blit(image, (0, 0))
    screen.blit(stick, (screen_width / 2, screen_height - 30)) 
 
    all_sprites_list.draw(screen)


    for event in pygame.event.get() : 
 
        if event.type == pygame.QUIT : 
            pygame.quit()   
            quit() 
  
        # Draws the surface object to the screen.   
        pygame.display.update()
  