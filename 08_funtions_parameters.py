# 함수 사용
# def function_name(param_first, ..., param_last):
#     execute codes (변수 + 약속어) # 실행할 코드 
#     return result_value

# 점수 총합 함수 작성
# kor = 60
# eng = 70
# math = 80

# sum = kor + eng

# def get_sum(korean, english):
#     # 실행할 코드
#     summation = korean + english
#     return summation

# sum = get_sum(kor, eng)
# print(f"총점: {sum}")

# Parameter 증가하기
# kor = 60
# eng = 70
# math = 80

# sum = kor + eng

# def get_sum(korean, english, mathematics):
#     # 실행할 코드
#     summation = korean + english + mathematics
#     return summation

# sum = get_sum(kor, eng, math)
# print(f"총점: {sum}")

# sum = get_sum(kor, eng)
# print(f"총점: {sum}")

# 만약 math 변수를 사용하지 않는다면?
# sum = get_sum(kor, eng, 0)

# 조금 더 깔끔하게(잘 쓴 함수는 함수 안에서 하는 게 많음.)
# def get_sum(korean, english, mathematics=0):
#     # 실행할 코드
#     summation = korean + english + mathematics
#     return summation

# sum = get_sum(kor, eng)
# print(f"총점: {sum}")

# for문 함수 작성
kor_scores = [90, 80, 70, 60, 50]
eng_scores = [85, 75, 65, 55, 45]
math_scores = [88, 78, 68, 58, 48]

lenght = len(kor_scores)
len_list = range(lenght)

# range_len = range(len(kor_scores)) # 0, 1, 2, 3, 4
# pass
# for i in range(len(kor_scores)):
#     kor = kor_scores[i]
#     eng = eng_scores[i]
#     math = math_scores[i]
#     total = get_sum(kor, eng, math)
#     print(f"{i+1}번 학생 총점: {total}")

# def function_name(param_first, ..., param_last):
#     execute codes (변수 + 약속어) # 실행할 코드 
#     return result_value

def get_for_sum(korean_scores, english_scores, mathmatics_scores):

    for i in range(len(korean_scores)):
        kor = korean_scores[i]
        eng = english_scores[i]
        math = mathmatics_scores[i]
        total = get_sum(kor, eng, math)
        print(f"{i+1}번 학생 총점: {total}")

    return 0

get_for_sum(kor_scores, eng_scores, math_scores)
