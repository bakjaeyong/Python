import random

tries = 0      #시도 횟수
guess = 0      # 추측값
answer = random.randint(1, 100) # 1과 100사이의 난수

print('1부터 100사이의 숫자를 맞춰라')

while guess != answer:
    guess = int(input("숫자를 입력하세요: "))
    tries = tries + 1
    if guess < answer:
        print("입력한 숫자가 정답보다 낮음")
    elif guess > answer:
        print("입력한 숫자가 정답보다 높음")

if guess == answer:
    print('축하합니다. 시도횟수=', tries)
else:
    print("정답은", answer)
    #랜덤 숫자 맞추기 게임 3월 31일 수업내용