import time 
print ('attendi la prossima domanda ')
time.sleep(2)
print('ecco la domanda')


#  generare i numeri casuali 
import random
print(random.random())
print(random.randint(1,10))

# disegno a matita 
import turtle
x= turtle.Turtle()
x.pencolor('red')
x.speed(5) # posso dare una velocita al disegno
x.forward(200)
x.right(90)
x.forward(200)
x.right(90)
x.forward(200)
x.right(90)
x.forward(200)
# usando i cicli 
for i in range (50):

    x.forward(100)
    x.left(123)


