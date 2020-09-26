import turtle

branch = turtle.Turtle()
branch.left(90)
branch.speed(150)

def cria(i):
    if i < 10:
        return
    else:
        branch.forward(i)
        branch.left(30)
        cria(3 * i / 4)
        branch.right(60)
        cria(3 * i / 4)
        branch.left(30)
        branch.backward(i)
        
cria(100)
turtle.done()




