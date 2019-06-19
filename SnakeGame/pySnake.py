import turtle
import time
import random

delay=0.1

score=0
Hscore=0



# screen 

wn=turtle.Screen()
wn.title("First Snake game @Sandesh ghimire")
wn.bgcolor("Blue")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake 

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="stop"

#food

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
food.direction="stop"

segments=[]


#scoring

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score: 0  High Score: 0", align="center", font=("roman",24,"normal"))


def Gup():
    if head.direction !="down":
        head.direction= "up"
        
def Gdown():
    if head.direction !="up":
        head.direction="down"
        
def Gleft():
    if head.direction !="right":
        head.direction="left"
        
def Gright():
    if head.direction !="left":
        head.direction="right"
        
        
        

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    elif head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
        
    elif head.direction=="left":
        x=head.xcor()
        head.setx(x+20)
        
    elif head.direction=="right":
        x=head.xcor()
        head.setx(x-20)
    


wn.listen()

wn.onkeypress(Gup,"w")
wn.onkeypress(Gdown,"s")
wn.onkeypress(Gleft,"d")
wn.onkeypress(Gright,"a")




while True:
    wn.update()
    
    #colision check
    if head.xcor() >290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        
        for segment in segments:
            segment.goto(1000,1000)
            
        segments.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, Hscore),align="center", font=("roman",24,"normal"))
    
    
    
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        
        
        #adding segment
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)
        
        #delayy
        delay -=0.001
        
        score += 10
        
        if score > Hscore:
            Hscore=score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, Hscore),align="center", font=("roman",24,"normal"))
        
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
            
        
        
    
    move()
    
    #body collision check
    
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            for segment in segments:
                segment.goto(1000,1000)
            
            segments.clear()
            score=0
            
            delay = 0.1
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, Hscore),align="center", font=("roman",24,"normal"))
        
    time.sleep(delay)
wn.mainloop()