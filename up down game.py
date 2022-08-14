"""업 다운 게임"""

정답 = 10
while True:
    입력 = int(input(">>> 숫자입력:"))
    if 정답 > 입력:
        print('업')
    elif 정답 < 입력:
        print ("다운")
    else:
        print("정답")
        break