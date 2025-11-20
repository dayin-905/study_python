## 작성 프롬프트(json 형식)
```
{
    "persona": {
        "role": "IT 인재 양성 전문가",
        "experience": "30년 차",
        "focus": "파이썬",
        "responsibilities": [
            "파이썬 교육 과정 및 교재 개발",
            "전문적인 인증 시험 설계 및 운영",
            "전 세계 교육 기관과의 파트너십을 통한 교육 표준 확립",
            "파이썬 전문가 양성"
        ]
    },
    "task": {
        "description": "제시된 조건을 따라서 문제를 해결할 것",
        "constraints": [
            "출력 형태는 반드시 json 형식일 것",
            "1번 조건의 json 형식 답변을 vs code에서 디버깅 할 수 있도록 .py 파일도 출력해줄 것",
            "사칙 연산을 수행하는 함수를 구현할 것"
        ],
        "problem": {
            "title": "두 개의 숫자 리스트를 이용해 사칙연산(+, -, *, /)을 수행하는 함수 구현",
            "sub_conditions": [
                "테스트 데이터는 리스트(list) 로만 제공",
                "테스트 데이터 개수는 10개",
                "변수명은 소문자 + _ 조합",
                "함수는 두 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 반환",
                "0으로 나누는 경우는 'division_error' 반환"
            ],
            "code_skeleton": {
                "function": "def calculate_all(num1, num2): ...",
                "test_data_a": [10, 25, 40, 12, 7, 9, 16, 100, 3, 81],
                "test_data_b": [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]
            }
        }
    }
}
```

## json 형식 프롬프트 답변 결과(.py)
import json

def calculate_all(num1, num2):
    """
    두 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 반환합니다.
    0으로 나누는 경우는 나눗셈 결과로 'division_error'를 반환합니다.
    (조건: 변수명은 소문자 + _ 조합)
    """
    # 덧셈 결과
    addition_result = num1 + num2
    # 뺄셈 결과
    subtraction_result = num1 - num2
    # 곱셈 결과
    multiplication_result = num1 * num2
    
    # 0으로 나누는 경우 예외 처리
    if num2 == 0:
        division_result = "division_error"
    else:
        # 일반적인 나눗셈 수행
        division_result = num1 / num2
        
    # (덧셈, 뺄셈, 곱셈, 나눗셈) 결과를 튜플로 반환
    return (addition_result, subtraction_result, multiplication_result, division_result)

# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 테스트 결과 데이터를 저장할 리스트
test_results = []

print("--- [디버깅 콘솔] 테스트 실행 시작 ---")

# 테스트 실행 및 결과 저장
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    results = calculate_all(a, b)
    
    # 콘솔에 실행 결과 출력 (디버깅용)
    print(f"Case {i+1}: {a} and {b} => {results}")
    
    # JSON 출력을 위한 데이터 구조 생성
    result_data = {
        "input_a": a,
        "input_b": b,
        "addition_result": results[0],
        "subtraction_result": results[1],
        "multiplication_result": results[2],
        "division_result": results[3]
    }
    test_results.append(result_data)

# 최종 JSON 결과 생성 (조건 1 충족)
final_json_output = json.dumps(
    {
        "test_case_count": len(test_results),
        "test_data": test_results
    },
    # JSON 가독성을 위한 들여쓰기 설정
    indent=4,
    # 한글 처리를 위한 설정 (선택적)
    ensure_ascii=False
)

print("\n--- [JSON 출력] 최종 결과 (조건 1) ---")
print(final_json_output)

# 참고: VS Code에서 디버깅 시, 'test_results' 리스트에 딕셔너리가 추가되는 과정을 확인해보게.