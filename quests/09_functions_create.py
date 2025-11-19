# def function_name(param_first, ..., param_last):
#     execute codes (변수 + 약속어) # 실행할 코드 
#     return result_value

# 🔹 문제 1
# 섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오.

# 섭씨 온도
t1 = 90
t2 = 20
t3 = 50

sum = t1 + t2 + t3

def to_celsius(temp1, temp2, temp3):
    avg_celsius = (temp1 + temp2 + temp3) / 3
    return avg_celsius

avg = to_celsius(t1, t2, t3)
print(f"평균 섭씨 온도: {avg}")


