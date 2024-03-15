import pygame, random,base64

your_code = base64.b64encode(b"""
screen = pygame.display.set_mode((1280, 720),pygame.SCALED | pygame.FULLSCREEN)
pygame.font.init()
running = True
e = [0,0,0,0,0,0]
class players(pygame.sprite.Sprite):
    def __init__(self,x,y,size): 
        pygame.sprite.Sprite.__init__(self);self.image = pygame.Surface((size[0],size[1]));self.color =(255,255,255);self.rect = self.image.get_rect();self.rect.center = (x,y)
    def update(self): 
        pygame.draw.circle(screen, self.color, (self.rect.centerx, self.rect.centery), self.rect.width/2);screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render("Score: %s Timer %s" %(e[0],e[1]), True, (255,0,255)), (1, 1))
        if(e[2]< 200):e[2] += 1
        else:e[1] += 1;e[2] = 0
    def reset(self): e[0] += 1;self.rect.center = (random.randint(self.rect.width,1280-self.rect.width),random.randint(self.rect.width,720-self.rect.width));self.rect.size = (random.randint(1,100),random.randint(1,100));self.color = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
cir = players(100,100,(200,200))
while running:  
    screen.fill((1, 1, 1))
    cir.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cir.rect.collidepoint(pygame.mouse.get_pos()): cir.reset()
    pygame.display.flip()""");exec(base64.b64decode(your_code))    