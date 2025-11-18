# ✅ 중급 난이도 문제 1 — 문자열과 f-string 활용
# second = “Python is fun", second 문자열에 "Python"이 포함되어 있는지 확인하고,
#  "Welcome!"과 합쳐서 출력하는 코드를 작성하시오.
# 조건: f-string 사용

# 출력 예시: "Welcome! Python is fun"

# second = "Python is fun"

second = "Python is fun"
first = "Welcome!"

print(f"{first} {second}")


# ✅ 중급 난이도 문제 2 — while 반복문 응용
# first 변수가 5부터 1까지 감소하도록 while문을 작성하고,
#  first == 2일 때만 "special"을 출력하도록 코드를 작성하시오.
# first = 5

first = 5
while first > 0 :
    if first == 2 :
        print("special")
    first = first - 1


# ✅ 중급 난이도 문제 3 — 리스트 합계 및 평균 계산
# kor와 eng 리스트가 주어졌을 때,
# 각 학생 점수의 총합을 total_scores 리스트로 저장

# 각 학생 점수 평균을 avg_scores 리스트로 저장


# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]


# 출력 예시:
# total_scores = [160, 160, 160, 110, 110]
# avg_scores = [80.0, 80.0, 80.0, 55.0, 55.0]

kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum1, sum2 = 0, 0

total_scores = [0, 0, 0, 0, 0]
avg_scores = [0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(5) :
    # sum1 = kor[i] + sum1
    # sum2 = eng[i] + sum2
    total_scores[i] = kor[i]+eng[i]
    # total_scores[i] = sum1 + sum2 
    avg_scores[i] = total_scores[i] / 2
    print(f"total_scores = {total_scores}")
    print(f"avg_scores = {avg_scores}")


# ✅ 중급 난이도 문제 4 — 누적 합과 조건문 결합
# kor 리스트에서 60점 이상인 점수만 누적 합계를 계산하고 출력하시오.
# 조건: for문 사용, 60점 미만은 제외


# kor = [70, 80, 90, 40, 50]
# sum3 = 0
# 여기에 코드 작성
# 출력 예시: 누적합 = 240

kor = [70, 80, 90, 40, 50]
sum3 = 0

for score in kor :
    if score >= 60 :
        sum3 = score + sum3
    print(f"누적합 = {sum3}")