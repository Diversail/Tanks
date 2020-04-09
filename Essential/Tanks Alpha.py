import pygame,time,random
pygame.init()
xb=800
yb=450
pygame.display.set_icon(pygame.image.load('A5.png'))
pygame.display.set_caption('Tanks!')
screen=pygame.display.set_mode([xb,yb])
T1=pygame.image.load('A3.png')
T2=pygame.image.load('A1.png')
T3=pygame.image.load('A.png')
T4=pygame.image.load('A2.png')
T5=pygame.image.load('A4.png')
T6=pygame.image.load('A6.png')
T7=pygame.image.load('A5.png')
T8=pygame.image.load('A7.png')
Wall=pygame.image.load('Wall.png')
Wall2=pygame.image.load('Wall1.png')
Wall4=pygame.image.load('Wall2.png')
Wall3=pygame.image.load('Wall3.png')
RBullet=pygame.image.load('RedBullet.png')
BBullet=pygame.image.load('BlueBullet.png')
x=700
y=50
x1=50
y1=50
y3=0
x3=0
x2=0
y2=0
width=40
height=40
v=4
velb = 14
Tank=T1
Tank1=T6
i=0
g=0
g1=0
i1=0
rr=0
r=0
ll=0
l=0
d=0
dd=0
u=0
uu=0
p=0
f=0
d=0
o=0
wr=0
wb=0
def main():
    global x,y,x1,y1,wr,wb,Tank,Tank1,g,g1,i1,i,y3,x3,y2,x2,rr,r,ll,l,u,uu,d,dd,p,o,f,d
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        keys = pygame.key.get_pressed()
        if x+45>=x1>=x and y1-40<y<y1+40:
            rr=1
        if x1+45>=x>=x1 and y-40<y1<y+40:
            r=1
        if x-45<=x1<=x and y1-40<y<y1+40:
            ll=1
        if x1-45<=x<=x1 and y-40<y1<y+40:
            l=1
        if y-40>=y1>=y-45 and x1-40<x<x1+40:
            uu=1
        if y1-40>=y>=y1-45 and x-40<x1<x+40:
            u=1
        if y+45>=y1>=y+40 and x1-40<x<x1+40:
            dd=1
        if y1+45>=y>=y1+40 and x-40<x1<x+40:
            d=1
        if keys[pygame.K_UP] and y>v+38 and uu==0:
            y-=v
            Tank=T4
        if keys[pygame.K_DOWN] and y<413-v-width and dd==0:
            y+=v
            Tank=T3
        if keys[pygame.K_LEFT] and x>v+38 and ll==0:
            x-=v
            Tank=T1
        if keys[pygame.K_RIGHT] and x<760-v-width and rr==0:
            x+=v
            Tank=T2
        if keys[pygame.K_w] and y1>v+38 and u==0:
            y1-=v
            Tank1=T8
        if keys[pygame.K_s] and y1<413-v-width and d==0:
            y1+=v
            Tank1=T7
        if keys[pygame.K_a] and x1>v+38 and l==0:
            x1-=v
            Tank1=T5
        if keys[pygame.K_d] and x1<760-v-width and r==0:
            x1+=v
            Tank1=T6
        if keys[pygame.K_SPACE]:
            x3=x1
            y3=y1
            g=1
            if Tank1==T8: #up
                y3+=8
                x3+=17
                i=1
            if Tank1==T7: #down
                y3+=31
                x3+=17
                i=2
            if Tank1==T6: #right
                x3+=30
                y3+=19
                i=3
            if Tank1==T5: #left
                x3+=4
                y3+=19
                i=4
        if keys[pygame.K_RCTRL]:
            x2=x
            y2=y
            g1=1
            if Tank==T4: #up down
                y2+=8
                x2+=17
                i1=1
            if Tank==T3:
                y2+=31
                x2+=17
                i1=2
            if Tank==T2:
                x2+=30
                y2+=19
                i1=3
            if Tank==T1:
                x2+=4
                y2+=19
                i1=4
        if g1==1:
            if i1==1:
                y2-=velb
                screen.blit(BBullet,(x2,y2))
            if i1==2:
                y2+=velb
                screen.blit(BBullet,(x2,y2))
            if i1==3:
                x2+=velb
                screen.blit(BBullet,(x2,y2))
            if i1==4:
                x2-=velb
                screen.blit(BBullet,(x2,y2))
        if g==1:
            if i==1:
                y3-=velb
                screen.blit(RBullet,(x3,y3))
            if i==2:
                y3+=velb
                screen.blit(RBullet,(x3,y3))
            if i==3:
                x3+=velb
                screen.blit(RBullet,(x3,y3))
            if i==4:
                x3-=velb
                screen.blit(RBullet,(x3,y3))
        p=40<x3<760
        o=40<y3<410
        f=40<x2<760
        d=40<y2<410
        if o==False or p==False:
            g=0
            y3=-30
            x3=-30
        if d==False or f==False:
            g1=0
            y2=-30
            x2=-30
        if x<x3<x+40 and y+40>y3>y:
            wr+=1
            x=random.randint(50,710)
            y=random.randint(50,370)
            g=0
            y3=-30
            x3=-30
            if wr>9:
                screen.fill((255,255,255))
                font = pygame.font.SysFont("Times New Roman", 30)
                text = font.render("Red has won! Game reset.", True, (128, 128, 0))
                screen.blit(text,(0,0))
                pygame.display.update()
                pygame.time.delay(3000)
                wr=0
                wb=0
        if x1<x2<x1+40 and y1+40>y2>y1:
            wb+=1
            x1=random.randint(50,710)
            y1=random.randint(50,370)
            g1=0
            y2=-30
            x2=-30
            if wb>9:
                screen.fill((255,255,255))
                font = pygame.font.SysFont("Times New Roman", 30)
                text = font.render("Blue has won! Game reset.", True, (128, 128, 0))
                screen.blit(text,(0,0))
                pygame.display.update()
                pygame.time.delay(3000)
                wb=0
                wr=0
        rr=0
        r=0
        l=0
        ll=0
        d=0
        dd=0
        u=0
        uu=0
        screen.blit(Wall,(0,0))
        screen.blit(Wall2,(40,0))
        screen.blit(Wall3,(760,0))
        screen.blit(Wall4,(40,410))
        screen.blit(Tank,(x,y))
        screen.blit(Tank1,(x1,y1))
        pygame.display.update()
    pygame.quit()
    sys.exit
    


if __name__ == '__main__':
    main()
