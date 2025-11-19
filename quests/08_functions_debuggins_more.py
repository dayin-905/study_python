## 시간 문제로 웹 gemini 사용했습니다..

✅ 문제 6 — 함수 내부 변수 오타
아래 함수는 섭씨 값으로 변환해 반환해야 하지만, 내부 변수의 오타로 인해 오류가 발생한다.
 오류를 찾고 해결하시오.
def to_celsius(temp):
    celsiu = (temp - 32) * 5 / 9   # 오타
    return celsius

print(to_celsius(77))

--- 정답 ---

def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9  # 🌟 수정: 오타 (celsiu -> celsius) 수정
    return celsius

print(to_celsius(77))


✅ 문제 7 — return 위치 오류
아래 프로그램은 반복문 안에서 함수를 호출하지만,
 함수 내부의 return 위치가 잘못되어 의도한 값이 계산되지 않는다.
 오류를 수정하시오.
def to_celsius(temp):
    if temp > 0:
        celsius = (temp - 32) * 5 / 9
    return             # 잘못된 위치
        celsius

print(to_celsius(50))

--- 정답 ---

def to_celsius(temp):
    if temp > 0:
        celsius = (temp - 32) * 5 / 9
    
    # 🌟 수정: return 문을 마지막에, 올바른 들여쓰기로 수정
    # (temp가 0 이하일 경우 celsius가 정의되지 않으므로, if문 밖에서 정의하거나 if문이 불필요하면 제거해야 하지만, 
    #  원 문제의 구조를 최대한 유지하고 return 위치만 수정했습니다.)
    return celsius # temp > 0 조건이 참일 때만 celsius가 정의됨

print(to_celsius(50))


✅ 문제 8 — 함수 재사용 시 논리 오류
아래 코드는 temp 값을 3개 변환하려고 하지만,
 변수 재사용과 return 값 처리에서 오류가 발생한다.
 오류를 찾고 해결하시오.
def to_celsius(temp):
    celsius = (temp - 3) * 5 / 9
    return celsius

temp = 77
result1 = to_celsius(temp)

temp = 95
result2 = to_celsius()    # 오류: 인자 없음

temp = 50
result3 = to_celsius(temp)

print(result1, result2, result3)

--- 정답 ---

def to_celsius(temp):
    # 🌟 수정: 공식 오류 (temp - 3 -> temp - 32) 수정
    celsius = (temp - 32) * 5 / 9
    return celsius

temp = 77
result1 = to_celsius(temp)

temp = 95
# 🌟 수정: 인자가 누락된 함수 호출에 temp 값을 인자로 전달
result2 = to_celsius(temp)

temp = 50
result3 = to_celsius(temp)

print(result1, result2, result3)


✅ 문제 9 — 리스트 값 변환 시 타입 오류
아래 코드는 리스트의 모든 값을 to_celsius()로 변환하려 하지만,
 리스트를 잘못 전달해서 오류가 발생한다.
 오류를 고치시오.
def to_celsius(temp):
    return (temp - 3) * 5 / 9

temps = [77, 95, 50]

value = to_celsius(temps)   # 리스트 전체 전달 -> 오류
print(value)

--- 정답 ---

def to_celsius(temp):
    return (temp - 32) * 5 / 9 # 🌟 논리 오류 방지를 위해 공식 수정 (3 -> 32)

temps = [77, 95, 50]

# 🌟 수정: 리스트의 각 요소를 개별적으로 함수에 전달
value1 = to_celsius(temps[0])
value2 = to_celsius(temps[1])
value3 = to_celsius(temps[2])

# 변환된 값들을 리스트 형태로 출력
print([value1, value2, value3])

✅ 문제 10 — 함수 반환값을 활용한 조건문 오류
아래 코드에서 조건 검사 부분이 잘못되어 조건이 항상 False가 된다.
 의도: 변환된 섭씨 값이 20보다 크면 "warm" 출력


 오류를 수정하시오.
def to_celsius(temp):
    return (temp - 32) * 5 / 9

if to_celsius > 20:       # 함수 호출 누락
    print("warm")
else:
    print("cold")

--- 정답 ---

def to_celsius(temp):
    return (temp - 32) * 5 / 9

# 🌟 수정: to_celsius 함수에 원하는 온도(77)를 인자로 넣어 호출
if to_celsius(77) > 20: 
    print("warm")
else:
    print("cold")