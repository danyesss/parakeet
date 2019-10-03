from graph import *
import math
windowSize(649, 918)
canvasSize(649, 918)
def elips(x1,y1,x2,y2):
    a=(x2-x1)/2
    b=(y2-y1)/2
    kost=[]
    for fi in range(1,360,1):
        y=int(b*math.sin(fi*math.pi/180)+y1+b)
        x=int(a*math.cos(fi*math.pi/180)+x1+a)
        kost.append((x,y))
    obj=polygon(kost)

def dog(x, a, y, b):
    penColor('gray')
    brushColor('gray')
    elips(x*125+a,y*194+b,x*263+a,y*283+b)
    brushColor('gray')
    elips(x*147+a,y*248+b,x*191+a,y*334+b)
    brushColor('gray')
    elips(x*137+a,y*232+b,x*103+a,y*307+b)
    brushColor('gray')
    elips(x*125+a,y*311+b,x*80+a,y*296+b)
    brushColor('gray')
    elips(x*186+a,y*329+b,x*130+a,y*342+b)
    brushColor('gray')
    elips(x*224+a,y*191+b,x*314+a,y*260+b)
    brushColor('gray')
    elips(x*274+a,y*232+b,x*333+a,y*299+b)
    brushColor('gray')
    elips(x*309+a,y*274+b,x*329+a,y*335+b)
    brushColor('gray')
    elips(x*326+a,y*334+b,x*271+a,y*352+b)
    brushColor('gray')
    elips(x*216+a,y*225+b,x*276+a,y*180+b)
    brushColor('gray')
    elips(x*248+a,y*208+b,x*267+a,y*293+b)
    brushColor('gray')
    elips(x*267+a,y*289+b,x*223+a,y*299+b)
    brushColor('gray')
    elips(x*164+a,y*225+b,x*114+a,y*217+b)  
    
    penColor('black')
    brushColor('gray')
    polygon([[x*178+a, y*230+b],  [x*178+a, y*138+b], [x*87+a, y*138+b], [x*87+a, y*230+b], [x*178+a, y*230+b]])   
    brushColor('gray')
    elips(x*92+a,y*153+b,x*73+a,y*192+b)
    brushColor('gray')
    elips(x*194+a,y*154+b,x*176+a,y*190+b)    
    brushColor('white')
    elips(x*97+a,y*162+b,x*127+a,y*176+b)
    brushColor('white')
    elips(x*137+a,y*162+b,x*167+a,y*176+b)
    brushColor('black')
    circle(x*112+a, y*169+b, 6*abs(x))
    brushColor('black')
    circle(x*152+a,y*169+b, 6*abs(x))  
    polyline([[x*148+a, y*210+b], [x*147+a, y*193+b],[x*142.5+a, y*188+b], [x*132.5+a, y*185+b],[x*122.5+a,y*188+b],[x*118+a,y*193+b],[x*117+a, y*210+b]])
    brushColor('white')
    polygon([[x*147+a, y*193+b],[x*142.5+a, y*188+b], [x*144.5+a, y*182+b],[x*147+a, y*193+b]])
    polygon([[x*122.5+a,y*188+b],[x*118+a,y*193+b], [x*120.5+a, y*182+b],[x*122.5+a,y*188+b]])
    

brushColor(114, 198, 219)
polygon([(0,0), (0,1000), (1500,1000), (1500,0)])
brushColor(104,216,116)
polygon([(0,350), (0,1000), (1500,1000), (1500,350)])

brushColor(193,141,49)
for i in range(25):
    polygon([(150 + 35 * i, 30), (150 + 35 * i,350), (150 + 35 * (i + 1),350), (150 + 35 * (i + 1),30)])

for i in range(16):
    polygon([(25 * i,200), (25 * i,450), (25 * (i + 1),450), (25 * (i + 1),200)])
    
for i in range(14):
    polygon([(23 * i,350), (23 * i,600), (23 * (i + 1),600), (23 * (i + 1),350)])

for i in range(25):
    polygon([(350 + 30 * i,300), (350 + 30 * i,550), (350 + 30 * (i + 1),550), (350 + 30 * (i + 1),300)])

dog(-0.9, 660, 0.9, 290);
brushColor(193,141,49)
d_bud = -90
polygon([(300,400-d_bud), (300,500-d_bud), (400,550-d_bud), (400,430-d_bud)])
polygon([(400,550-d_bud), (400,430-d_bud), (450,400-d_bud), (450,500-d_bud)])
polygon([(300,400-d_bud), (370,300-d_bud), (400,430-d_bud)])
polygon([(370,300-d_bud), (400,430-d_bud), (450,400-d_bud), (410,290-d_bud)])
brushColor("black")
circle(350, 470-d_bud, 20)

x = -1
y = 1
a = 370
b = 200
##


dog(1, -20, 1, 340);
dog(-1.2, 370, 1.2 , 500);
dog(3, 100, 3, 400);

penSize(2)
brushColor('#FFFFFF')
d_ring = - 50
d_ringy = 0
elips(300-d_ring,530-d_bud-d_ringy,280-d_ring,520-d_bud-d_ringy)
elips(286-d_ring,525-d_bud-d_ringy,276-d_ring,550-d_bud-d_ringy)
d_ring = -35
d_ringy = -25
elips(300-d_ring,530-d_bud-d_ringy,280-d_ring,520-d_bud-d_ringy)

##
run()