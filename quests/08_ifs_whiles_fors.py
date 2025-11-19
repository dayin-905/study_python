# ✅ 문제 1 — return 누락 오류
# 아래 함수는 섭씨 변환 후 값을 반환해야 한다.
#  현재 코드에서 발생하는 오류를 찾고 수정하시오.
# def to_celsius(temp):
#     celsius = (temp - 32) * 5 / 9
#     # return 문이 없음

# result = to_celsius(77)
# print(result)
                                                     
#     4 def to_celsius(temp):                                                                                                           
#    5     celsius = (temp - 32) * 5 / 9                                                                                               
#    6     return celsius # Added the return statement                                                                                ▄
#    7                                                                                                                                █
#    8 result = to_celsius(77)                                                                                                        █
#    9 print(result)    

# def to_celsius(temp):
#     celsius = (temp - 32) * 5 / 9
#     return celsius

# result = to_celsius(77)
# print(result)


# ✅ 문제 2 — 매개변수 이름 오류
# 아래 프로그램은 실행 시 오류가 발생한다.
#  오류 위치를 찾고 올바르게 수정하시오.

# def convert(temp):
#     return (temps - 3) * 5 / 9   # 오타: temps

# print(convert(95))

# │ ✓  Edit quests/08_ifs_whiles_fors.py: # ✅ 문제 2 — 매개변수 이름 오류... => # ✅ 문제 2 — 매개변수 이름 오류...                 │ 
# │                                                                                                                                  │ 
# │ 26   # ✅ 문제 2 — 매개변수 이름 오류                                                                                            │ 
# │ 27   # 아래 프로그램은 실행 시 오류가 발생한다.                                                                                  │ 
# │ 28   #  오류 위치를 찾고 올바르게 수정하시오.                                                                                    │ 
# │ 29 - # def convert(temp):                                                                                                        │ 
# │ 30 - #     return (temps - 3) * 5 / 9   # 오타: temps                                                                            │▄
# │ 31 -                                                                                                                             │█
# │ 32 - print(convert(95))                                                                                                          │▀
# │ 33 -                                                                                                                             │ 
# │ 29   def convert(temp):                                                                                                          │ 
# │ 35 -     return (temp - 3) * 5 / 9   # 오타: temps                                                                               │ 
# │ 30 +     return (temp - 32) * 5 / 9                                                                                              │ 
# │ 31                                                                                                                               │ 
# │ 32   print(convert(95)) 


# def convert(temp):
#     return (temp - 32) * 5 / 9

# print(convert(95))

# ✅ 문제 3 — 함수 호출 인자 오류
# 아래 코드는 함수 호출이 잘못되어 있다.
#  오류를 설명하고 고치시오.

# │ ✓  Edit quests/08_ifs_whiles_fors.py: value = to_celsius()... => value = to_celsius(77) # Fixed...                               │ 
# │                                                                                                                                  │ 
# │ 37   def to_celsius(temp):                                                                                                       │ 
# │ 38       return (temp - 32) * 5 / 9                                                                                              │ 
# │ 39                                                                                                                               │ 
# │ 40 - value = to_celsius()                                                                                                        │ 
# │ 40 + value = to_celsius(77) # Fixed: Provided the 'temp' argument                                                                │ 
# │ 41   print(value)        

# def to_celsius(temp):
#     return (temp - 32) * 5 / 9

# value = to_celsius(77) # Fixed: Provided the 'temp' argument
# print(value)


# ✅ 문제 4 — 타입 오류(TypeError)
# 아래 코드는 문자열을 함수에 전달하여 오류가 발생한다.
#  이 오류가 왜 발생하는지 설명하고 해결하시오.

# def to_celsius(temp):
#     return (temp - 3) * 5 / 9

# print(to_celsius("77"))

# │ ✓  Edit quests/08_ifs_whiles_fors.py: def to_celsius(temp):... => def to_celsius(temp):...                                       │ 
# │                                                                                                                                  │ 
# │ 45   # 아래 코드는 문자열을 함수에 전달하여 오류가 발생한다.                                                                     │ 
# │ 46   #  이 오류가 왜 발생하는지 설명하고 해결하시오.                                                                             │ 
# │ 47   def to_celsius(temp):                                                                                                       │ 
# │ 48 -     return (temp - 3) * 5 / 9                                                                                               │ 
# │ 48 +     return (temp - 32) * 5 / 9                                                                                              │ 
# │ 49                                                                                                                               │ 
# │ 50 - print(to_celsius("77"))                                                                                                     │ 
# │ 50 + print(to_celsius(77)) # Passing an integer instead of a string 

# def to_celsius(temp):
#     return (temp - 32) * 5 / 9

# print(to_celsius(77)) # Passing an integer instead of a string

# ✅ 문제 5 — 반복 구조 + 함수 사용 오류
# 아래 코드는 여러 값을 함수로 변환하려 하지만 오류가 발생한다.
#  오류 원인을 찾고 고치시오.(Option : for 문을 함수화)

# def to_celsius(temp):
#     return (temp - 3) * 5 / 9

# temps = [77, 95, 50]
# results = []

# for t in temps:
#     result = to_celsius(temp)   # 변수명 오류
#     print(results)

# │ ✓  Edit quests/08_ifs_whiles_fors.py: def to_celsius(temp):... => def to_celsius(temp):...                                       │ 
# │                                                                                                                                  │ 
# │ 104   #  오류 원인을 찾고 고치시오.(Option : for 문을 함수화)                                                                    │ 
# │ 105                                                                                                                              │ 
# │ 106   def to_celsius(temp):                                                                                                      │ 
# │ 107 -     return (temp - 3) * 5 / 9                                                                                              │ 
# │ 107 +     return (temp - 32) * 5 / 9 # Fixed formula                                                                             │ 
# │ 108                                                                                                                              │ 
# │ 109   temps = [77, 95, 50]                                                                                                       │ 
# │ 110   results = []                                                                                                               │ 
# │ 111                                                                                                                              │ 
# │ 112   for t in temps:                                                                                                            │ 
# │ 113 -     result = to_celsius(temp)   # 변수명 오류                                                                              │ 
# │ 114 -     print(results)                                                                                                         │ 
# │ 113 +     result = to_celsius(t)   # Fixed: Changed 'temp' to 't'                                                                │ 
# │ 114 +     results.append(result)   # Added: Appending result to the list                                                         │▄
# │ 115                                                                                                                              │█
# │ 116 + print(results) # Fixed: Printing the results list outside the loop 

def to_celsius(temp):
    return (temp - 3) * 5 / 9

temps = [77, 95, 50]
results = []

for t in temps:
    result = to_celsius(temp)  
    print(results)