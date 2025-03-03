import turtle as t
import time


for θ in range(90, 180, 10):
    t.teleport(100,100)
    t.write("θ = " + str(θ))
    t.teleport(0,0)
    t.color("red","yellow")
    t.speed(0)
    t.begin_fill()
    while True:
        t.forward(200)
        t.right(θ)
        if abs(t.pos()) < 1:
            break

    t.end_fill()
    time.sleep(0.5)    
    t.clearscreen()


