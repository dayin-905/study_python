# def function_name(param_first, ..., param_last):
#     execute codes (변수 + 약속어) # 실행할 코드 
#     return result_value

# 🔹 문제 1
# 섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오.

# def to_celsius(t1, t2, t3):
#     avg_celsius = (t1 + t2 + t3) / 3
#     return avg_celsius

# print(to_celsius(77, 95, 50))
# print(to_celsius(32, 68, 104))
# print(to_celsius(2, 100, 37))

# avg = to_celsius
# print(f"평균 섭씨 온도: {avg}")


# 🔹 문제 2
# 이름과 좋아하는 언어 2개를 받아 아래 형식으로 출력하는 함수를 작성하시오.
# 홍길동님의 선호 언어는 Python, Java 입니다.

# def favorite_language(name, lang1, lang2):
#     print(f"{name}님의 선호 언어는 {lang1}, {lang2} 입니다.")

# print(favorite_language("홍길동", "Python", "Java"))
# print(favorite_language("김철수", "C", "C++"))
# print(favorite_language("이영희", "JavaScript", "Ruby"))

# 🔹 문제 3
# 점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수를 작성하시오.

# def sum_scores(score_list):
#     sum = 0
#     for score in score_list:
#         if score >= 60:
#         sum += score
#     return sum

# print(sum_scores([70, 55, 90, 40, 80]))  
# print(sum_scores([60, 60, 60, 60, 60]))
# print(sum_scores([50, 40, 30, 20, 10]))


# 🔹 문제 4
# 문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수 combine(str1, str2) 작성.

# def combine(str1, str2):
#     sentence = str1 + " " + str2 # 띄어쓰기가 key point
#     return sentence 
# print(combine("안녕하세요.", "반갑습니다."))
# print(combine("Hello.", "nice to meet you."))
# print(combine("Hi.", "how are you?"))


# 🔹 문제 5
# 온도 리스트를 받아 모두 섭씨로 변환해 새로운 리스트로 반환하는 함수 작성.
def to_celsius_list(tempf_list):
    list_length = len(tempf_list)
    celsius_list = list(range(list_length)) 

    for i in range(list_length):
        tempf = tempf_list[i]
        celsius = (tempf - 32) * 5 / 9
        celsius_list[i] = celsius
    return celsius_list

print(to_celsius_list([77, 68, 86, 32, 212]))