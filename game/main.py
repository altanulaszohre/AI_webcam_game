import pygame, sys, time
from setting import *
from sprites import BG, Obstacle,Plane,Obstacle
from turtle import Shape, position, shapesize, width
import cv2
import mediapipe


camera = cv2.VideoCapture(0)
mpDraw= mediapipe.solutions.drawing_utils
mpHans= mediapipe.solutions.hands
hands= mpHans.Hands()
mp_drawing_styles = mediapipe.solutions.drawing_styles




class Game:
    def __init__(self):
        pygame.init()
        self.display_surface=pygame.display.set_mode((window_w,window_h))
        pygame.display.set_caption('AUZ')
        self.clock=pygame.time.Clock()
        self.active=True

        self.all_sprites=pygame.sprite.Group()
        self.collision_sprites=pygame.sprite.Group()

        bg_height=pygame.image.load('bg2.jpg').get_height()
        self.scale_factor=window_h/bg_height

        BG(self.all_sprites,self.scale_factor)
        self.plane=Plane(self.all_sprites,self.scale_factor*0.1)
 

        self.obstacle_timer=pygame.USEREVENT+1
        pygame.time.set_timer(self.obstacle_timer,1400)
        

        self.font=pygame.font.Font('vademecum.ttf',30)
        self.score=0
        self.start_offset=0


        self.menu_surf=pygame.image.load('menu.png')
        self.menu_rect=self.menu_surf.get_rect(center=(window_w/2,window_h/2))

    def collision(self):
        if pygame.sprite.spritecollide(self.plane,self.collision_sprites,False):
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type=='obstacle':
                    sprite.kill()
            self.active=False
            self.plane.kill()

    def display_score(self):
        if self.active:
            self.score=(pygame.time.get_ticks()-self.start_offset)//1000
            y=window_h/10
        else:
            y=window_h/2+(self.menu_rect.height/1.5)


        score_surf=self.font.render(str(self.score),True,'darkblue')
        score_rect=score_surf.get_rect(midtop=(window_w/2,y))
        self.display_surface.blit(score_surf,score_rect)

    def run(self):
        last_time=time.time()
        while True:



            success, img=camera.read()
            imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            hlms=hands.process(imgRGB)
            height, width, channel=img.shape


            if(hlms.multi_hand_landmarks):

                for handlandmarks in hlms.multi_hand_landmarks:

                    for fingerNum, landmark in enumerate(handlandmarks.landmark):
                        positionX,positionY=int(landmark.x* width),int(landmark.y*height)
                        #cv2.circle(img,(positionX,positionY),3,(100,255,100),cv2.FILLED)
                        #cv2.putText(img,str(fingerNum),(positionX,positionY),2,1,(255,0,100))
                        

                        if(fingerNum==12):
                            basx=int(landmark.x*width)
                            basy=int(landmark.y*height)

                        if(fingerNum==9):
                            sonx=int(landmark.x*width)
                            sony=int(landmark.y*height)
                    
                    if(basy>sony):
                        if self.active:
                            self.plane.jump()
                        else:
                            self.plane=Plane(self.all_sprites,self.scale_factor*0.1)
                            self.active=True
                            self.start_offset=pygame.time.get_ticks()



            dt=time.time()-last_time
            last_time=time.time()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.active:
                        self.plane.jump()
                    else:
                        self.plane=Plane(self.all_sprites,self.scale_factor*0.1)
                        self.active=True
                        self.start_offset=pygame.time.get_ticks()

                if event.type==self.obstacle_timer and self.active:
                    Obstacle([self.all_sprites,self.collision_sprites],self.scale_factor*0.25)
            
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            self.display_score()


            if self.active:
                self.collision()
            else:
                self.display_surface.blit(self.menu_surf,self.menu_rect)




            pygame.display.update()
            self.clock.tick(framerate)








if __name__ =='__main__':
    game= Game()
    game.run()