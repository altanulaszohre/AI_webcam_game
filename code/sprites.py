from matplotlib.pyplot import sca
import pygame
from scipy import rand
from setting import*
from random import choice,randint


class BG(pygame.sprite.Sprite):

    def __init__(self,groups,scale_factor):
        super().__init__(groups)
        bg_image=pygame.image.load('bg2.jpg').convert()
        full_h=bg_image.get_height()*scale_factor
        full_w=bg_image.get_width()*scale_factor
        full_sized_image=pygame.transform.scale(bg_image,(full_w,full_h))

        self.image=pygame.Surface((full_w*2,full_h))
        self.image.blit(full_sized_image,(0,0))
        self.image.blit(full_sized_image,(full_w,0))
        self.rect=self.image.get_rect(topleft=(0,0))
        self.pos=pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 200*dt
        if self.rect.centerx <= 0:
            self.pos.x=0
        self.rect.x = round(self.pos.x)


class Plane(pygame.sprite.Sprite):
    def __init__(self,groups,scale_factor):
        super().__init__(groups)


        self.import_frames(scale_factor)
        self.frame_index=0
        self.image=self.frames[self.frame_index]


        self.rect=self.image.get_rect(midleft=(window_w/20,window_h/2))
        self.pos=pygame.math.Vector2(self.rect.topleft)

        self.gravity=222
        self.direction=2



    def import_frames(self,scale_factor):
        self.frames=[]
        for i in range(3):
            surf=pygame.image.load(f'plane{i}.png').convert_alpha()
            scaled_surface = pygame.transform.scale(surf,pygame.math.Vector2(surf.get_size())*scale_factor)
            self.frames.append(scaled_surface)


    def a_gravity(self,dt):
        self.direction+=self.gravity*dt
        self.pos.y+=self.direction*dt
        self.rect.y=round(self.pos.y)


    def jump(self):
        self.direction=-200


    

    def update(self,dt):
        self.a_gravity(dt)
    

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,groups,scale_factor):
        super().__init__(groups)
        self.sprite_type='obstacle'

        orientation=choice(('up','down'))
        surf=pygame.image.load('ballon.png').convert_alpha()
        self.image=pygame.transform.scale(surf,pygame.math.Vector2(surf.get_size())*scale_factor)
        x=window_w+randint(100,180)
        if orientation=='up':
            y=window_h+randint(-10,20)
            self.rect=self.image.get_rect(midbottom=(x,y))

        else:
            y=randint(5,70)
            self.rect=self.image.get_rect(midtop=(x,y))



        
        self.pos=pygame.math.Vector2(self.rect.topleft)

    def update(self,dt):
        self.pos.x-=400*dt
        self.rect.x=round(self.pos.x)
        if self.rect.right<=-100:
            self.kill()
