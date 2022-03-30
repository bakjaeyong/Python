#한 변의 크기와 변의 수를 입력받아 다각형 그리기

#1. 변의 크기와 변의 수를 입력받는다.

#2. 변을 그리면서 회전해야 할 각도를 계산.

#3. 계산된 결과를 가지고 다각형을 그린다.

import turtle

t=turtle.Turtle()
t.shape("turtle")

a = int(input('몇 각형을 그릴까요?'))

for i in range(a):
    t.forward(200)
    t.left(360/a)
    


