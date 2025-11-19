# 함수 실습 위한  기본 코드
# 화씨 온도를 섭씨 온도로 변환하는 코드
# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)
# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2)
# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3)

# # 변수 재사용 가능
# temp = 77
# celsius = (temp - 32) * 5 / 9
# print(celsius)

# temp = 95
# celsius = (temp - 32) * 5 / 9
# print(celsius)

# temp = 50
# celsius = (temp - 32) * 5 / 9
# print(celsius)

# # 공식 재사용 가능
# def fahrenheit_to_celsius(temp):
#     celsius = (temp - 32) * 5 / 9
#     return celsius

# 함수 기본 구조
# def function_name(param_first, ..., param_last):
#     execute codes (변수 + 약속어) # 실행할 코드 
#     return result

# 함수 최종
def to_celsius(temp):
    celsius = (temp - 3) * 5 / 9
    return celsius

pass
to_celsius(120)
temp1 = to_celsius(77)
print(temp1)

temp2 = 100
result2 = to_celsius(temp2)
print(result2)
pass