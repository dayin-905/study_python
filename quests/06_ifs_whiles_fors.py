# ✅ 문제 1 — 문자열 포맷 오류 수정하기
# 아래 코드는 문자열을 합치는 과정에서 오류가 발생한다.
#  오류를 찾아서 올바른 코드로 수정하시오.
second = "Programming"
first = "Welcome to Python Strings" + {second}   # 오류 발생

print(first)

#  ✓  Edit quests/0600.py: first = "Welcome to Python Str... => first =… │ 
# │                                                                       │ 
# │ 1   second = "Programming"                                            │ 
# │ 2 - first = "Welcome to Python Strings" + {second}   # 오류 발생      │▄
# │ 2 + first = "Welcome to Python Strings" + second                      │█
# │ 3                                                                     │▀
# │ 4   print(first) 

second = "Programming"
first = "Welcome to Python Strings" + second

print(first)

# ✅ 문제 2 — while 조건 오류 찾기
# 아래 코드는 first가 문자열인데, while 조건에서 비교 연산을 수행하려고 한다.
#  발생하는 오류를 설명하고, 정상 작동하도록 수정하시오.
first = "Hello Python"

while first > 0:
    print(first)
    first = first - 1

# │ ✓  Edit quests/0600.py: first = "Hello Python"... => first = 5...     │ 
# │                                                                       │ 
# │ 1 - first = "Hello Python"                                            │ 
# │ 1 + first = 5                                                         │ 
# │ 2                                                                     │ 
# │ 3   while first > 0:                                                  │ 
# │ 4 -     print(first)                                                  │ 
# │ 4 +     print("Hello Python")                                         │▄
# │ 5       first = first - 1   

first = 5

while first > 0:
    print("Hello Python")
    first = first - 1


# ✅ 문제 3 — 리스트 누적 합 오류 찾기
# 아래 코드의 오류를 찾고 올바르게 수정하시오.
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum_all = 0

for k in kor:
    sum_all = sum_all + kor + eng     # 오류 위치

# │ ✓  Edit quests/0600.py: for k in kor:... => sum_all = sum(kor) + sum… │ 
# │                                                                       │ 
# │ 2   eng = [90, 80, 70, 70, 60]                                        │ 
# │ 3   sum_all = 0                                                       │ 
# │ 4                                                                     │ 
# │ 5 - for k in kor:                                                     │ 
# │ 6 -     sum_all = sum_all + kor + eng                                 │ 
# │ 5 + sum_all = sum(kor) + sum(eng)    

kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum_all = 0

sum_all = sum(kor) + sum(eng)
print(sum_all) 


# ✅ 문제 4 — for-range 인덱스 문제 해결
# 아래 코드에서 IndexError가 발생한다.
#  오류 원인을 설명하고 올바른 코드를 작성하시오.
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum_total = 0

for i in range(0, 10):    # 오류 발생
    sum_total = sum_total + kor[i] + eng[i]

# │ ✓  Edit quests/0600.py: for i in range(0, 10):    # 오류... => for i… │ 
# │                                                                       │ 
# │ 3                                                                     │ 
# │ 4   sum_total = 0                                                     │ 
# │ 5                                                                     │ 
# │ 6 - for i in range(0, 10):    # 오류 발생                             │ 
# │ 6 + for i in range(len(kor)):    # Corrected range                    │ 
# │ 7       sum_total = sum_total + kor[i] + eng[i]                       │ 
# │ 8 +                                                                   │ 
# │ 9 + print(sum_total)      

kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum_total = 0

for i in range(len(kor)):    # Corrected range
    sum_total = sum_total + kor[i] + eng[i]

print(sum_total)