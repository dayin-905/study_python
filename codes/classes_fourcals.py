# Python function

# 클래스(class) 문법
# class class_name():
#     # 속성(변수)
#     # 메서드(함수)

# 사칙연산 class 제작
class FourCal:
    # 메서드(함수)
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            return "0으로 나눌 수 없습니다."
        return a / b

# Class
if __name__ == "__main__":
    forucal = FourCal() # FourCal클래스를 forucal에 담기. (인스턴스) 생성
    print(f"3 + 5 = {forucal.add(3, 5)}") # 함수와 클래스를 구분 짓는 온점 추가
    print(f"10 + 4 = {forucal.sub(10, 4)}")
    print(f"2 + 6 = {forucal.mul(2, 6)}")
    print(f"8 + 2 = {forucal.div(8, 2)}")

pass
# main이라는 함수를 호출하는 것.



# 기본 함수 구조
# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mul(a, b):
#     return a * b
# def div(a, b):
#     if b == 0:
#         return "0으로 나눌 수 없습니다."
#     return a / b


# print(f"3 + 3 = {add(3, 5)}")
# print(f"10 + 4 = {sub(10, 4)}")
# print(f"2 + 6 = {mul(2, 6)}")
# print(f"8 + 2 = {div(8, 2)}")