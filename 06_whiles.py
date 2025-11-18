first = 5

# while 문장 구조
# while condition :
#     executable_statements

while first > 0 :
    print(f"while 값 : {first}")
    if first == 3 :
        print("break 실행")
        break
    first = first - 1
print("while 종료")