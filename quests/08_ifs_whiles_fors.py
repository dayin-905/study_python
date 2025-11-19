✅ 문제 1 — return 누락 오류
아래 함수는 섭씨 변환 후 값을 반환해야 한다.
 현재 코드에서 발생하는 오류를 찾고 수정하시오.
def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    # return 문이 없음

result = to_celsius(77)
print(result)

