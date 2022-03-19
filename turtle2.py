import turtle as t

t.shape("turtle")
t.speed(11)
t.pensize(20)

#black cicle draw
t.circle(100)

t.up()
t.forward(240)
t.down()
t.pencolor('red')
t.circle(100)

t.up()
t.backward(480)
t.down()
t.pencolor('blue')
t.circle(100)

t.up()
t.right(40)       ## 오른쪽으로 40만큼 ##
t.forward(75)     ## 앞으로 75방향만큼 맞추어서 네번째 오륜기 모양을 완성 ##
t.down()
t.pencolor('yellow')  ## 컬러는 노란색으로 ##
t.circle(100)

t.up()
t.right(108)      ## 다시 오른쪽으로 108만큼 ##
t.backward(300)   ## 뒤로 300방향을 주어 다섯번째 오륜기 모양을 완성 ##
t.down()
t.pencolor('green')  ## 컬러는 초록색으로 ##
t.circle(100)

t.done()
