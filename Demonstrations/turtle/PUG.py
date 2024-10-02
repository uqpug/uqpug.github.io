import turtle as t

# Draw the word PUG

# PUG
t.color("#266e39", "#d4fade")

# Move left
t.pu()
t.bk(200)
t.pd()

# P
t.begin_fill()
t.left(90)
t.fd(200)
t.right(90)
t.fd(50)
t.right(45)
t.fd(33*(2**0.5))
t.right(45)
t.fd(33)
t.right(45)
t.fd(33*(2**0.5))
t.right(45)
t.fd(50)
t.end_fill()

# Move to U
t.pu()
t.left(90)
t.fd(100)
t.left(135)
t.fd(200*(2**0.5))
t.pd()

# U
t.right(135)
t.fd(150)
t.left(45)
t.fd(50*(2**0.5))
t.left(45)
t.fd(50)
t.left(45)
t.fd(50*(2**0.5))
t.left(45)
t.fd(150)

# Move to G
t.pu()
t.right(90)
t.fd(150)
t.pd()

# G
t.fd(50)
t.bk(50)
t.right(135)
t.fd(50*(2**0.5))
t.left(45)
t.fd(100)
t.left(45)
t.fd(50*(2**0.5))
t.left(45)
t.fd(50)
t.left(90)
t.fd(50)
t.right(90)
t.bk(25)
t.fd(50)

t.mainloop()
