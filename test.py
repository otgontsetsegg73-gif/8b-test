import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  
    screen.fill((255, 255, 255)) 
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 100, 100))
    pygame.draw.circle(screen, (0, 255, 0), (300, 300), 50)

    pygame.draw.polygon(screen, (255, 255, 0), [(250, 50), (300, 150), (200, 150)])  


  
    pygame.display.flip()
  