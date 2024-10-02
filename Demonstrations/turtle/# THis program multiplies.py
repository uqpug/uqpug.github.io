import turtle as t


t.color("red","yellow")
t.begin_fill()


while True:
    t.forward(200)
    t.right(100)
    if abs(t.pos()) < 1:
        break

t.end_fill()

t.mainloop()