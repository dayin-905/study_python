## 작성 프롬프트
```
너는 파이썬에 있어서 일가견이 있는 30년 차 IT 인재 양성에 힘을 쓰고 있는 전문가야. 파이썬 교육 과정 및 교재를 개발하고, 이를 바탕으로 전문적인 인증 시험을 설계 및 운영하며, 전 세계 교육 기관과의 파트너십을 통해 교육 표준을 확립하여 파이썬 전문가를 양성하는 역할을 수행하고 있어.

해당하는 문제를 내가 얘기한 조건에 따라서 해결해줘.

[조건]
1. 출력 형태는 반드시 json 형식일 것.
2. 1번 조건의 json 형식 답변을 vs code에서 디버깅 할 수 있도록 .py 파일도 출력해줄 것.
3. 사칙 연산을 수행하는 함수를 구현할 것.

[문제]
✅ **문제:
두 개의 숫자 리스트를 이용해 사칙연산(+, -, , /)을 수행하는 함수를 구현하시오.*

조건
테스트 데이터는 리스트(list) 로만 제공
테스트 데이터 개수는 10개
변수명은 소문자 + _ 조합
함수는 두 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 반환
0으로 나누는 경우는 "division_error" 반환

✅ 문제 코드 골격
학생이 채워 넣도록 비워둔 버전입니다.
def calculate_all(num1, num2):
    # 여기에 사칙연산 구현
    # return (덧셈, 뺄셈, 곱셈, 나눗셈)
    pass

# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 테스트 실행
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    result = calculate_all(a, b)
    print(f"{a}, {b} => {result}")
```

## 작성 프롬프트 답변
## 1. ⚙️ 문제 해결 및 코드 구현

핵심은 **예외 처리(0으로 나누는 경우)**를 포함하여 함수를 구현하고, 이를 실행한 결과를 JSON 형식과 실행 가능한 .py 파일로 제공하는 것일세.

요구사항에 맞게 `calculate_all` 함수를 구현하고 테스트 스크립트를 작성했네.

### 📌 calculator.py 파일 내용
```
python
def calculate_all(num1, num2):
    """
    두 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 반환합니다.
    0으로 나누는 경우는 나눗셈 결과로 "division_error"를 반환합니다.
    """

    addition_result = num1 + num2
    subtraction_result = num1 - num2
    multiplication_result = num1 * num2

    # 0으로 나누는 경우 예외 처리
    if num2 == 0:
        division_result = "division_error"
    else:
        division_result = num1 / num2

    return (addition_result, subtraction_result, multiplication_result, division_result)


# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 결과 저장을 위한 리스트
test_results = []

# 테스트 실행 및 결과 저장
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    results = calculate_all(a, b)

    # 결과 딕셔너리 생성
    result_data = {
        "input_a": a,
        "input_b": b,
        "addition_result": results[0],
        "subtraction_result": results[1],
        "multiplication_result": results[2],
        "division_result": results[3]
    }

    test_results.append(result_data)

# JSON 출력을 위한 임포트
import json

# 최종 JSON 결과 생성
final_json_output = json.dumps(
    {
        "test_case_count": len(test_results),
        "test_data": test_results
    },
    indent=4,
    ensure_ascii=False
)

# 콘솔에 JSON 결과 출력 (디버깅 편의를 위해)
# print(final_json_output)
```

## 2. 📄 출력 형태: JSON 형식 (조건 1)
요구하신 테스트 실행 결과를 담은 JSON 형식의 출력물입니다.
```
{
    "test_case_count": 10,
    "test_data": [
        {
            "input_a": 10,
            "input_b": 5,
            "addition_result": 15,
            "subtraction_result": 5,
            "multiplication_result": 50,
            "division_result": 2.0
        },
        {
            "input_a": 25,
            "input_b": 5,
            "addition_result": 30,
            "subtraction_result": 20,
            "multiplication_result": 125,
            "division_result": 5.0
        },
        {
            "input_a": 40,
            "input_b": 8,
            "addition_result": 48,
            "subtraction_result": 32,
            "multiplication_result": 320,
            "division_result": 5.0
        },
        {
            "input_a": 12,
            "input_b": 3,
            "addition_result": 15,
            "subtraction_result": 9,
            "multiplication_result": 36,
            "division_result": 4.0
        },
        {
            "input_a": 7,
            "input_b": 0,
            "addition_result": 7,
            "subtraction_result": 7,
            "multiplication_result": 0,
            "division_result": "division_error"
        },
        {
            "input_a": 9,
            "input_b": 3,
            "addition_result": 12,
            "subtraction_result": 6,
            "multiplication_result": 27,
            "division_result": 3.0
        },
        {
            "input_a": 16,
            "input_b": 2,
            "addition_result": 18,
            "subtraction_result": 14,
            "multiplication_result": 32,
            "division_result": 8.0
        },
        {
            "input_a": 100,
            "input_b": 4,
            "addition_result": 104,
            "subtraction_result": 96,
            "multiplication_result": 400,
            "division_result": 25.0
        },
        {
            "input_a": 3,
            "input_b": 9,
            "addition_result": 12,
            "subtraction_result": -6,
            "multiplication_result": 27,
            "division_result": 0.3333333333333333
        },
        {
            "input_a": 81,
            "input_b": 9,
            "addition_result": 90,
            "subtraction_result": 72,
            "multiplication_result": 729,
            "division_result": 9.0
        }
    ]
}
```

## 3. 💾 VS Code 디버깅용 .py 파일 (조건 2)

아래 코드를 calculator.py 파일로 저장하면 VS Code에서 직접 실행 및 디버깅이 가능합니다.
특히 test_results 리스트에 딕셔너리가 추가되는 과정을 살펴보면 데이터 처리 흐름을 명확히 이해할 수 있을 걸세.
```
import json

def calculate_all(num1, num2):
    """
    두 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 반환합니다.
    0으로 나누는 경우는 나눗셈 결과로 "division_error"를 반환합니다.
    """

    # 변수명은 소문자 + _ 조합을 따랐음
    addition_result = num1 + num2
    subtraction_result = num1 - num2
    multiplication_result = num1 * num2

    # 0으로 나누는 경우 예외 처리 조건
    if num2 == 0:
        division_result = "division_error"
    else:
        # 일반적인 나눗셈 수행
        division_result = num1 / num2

    # 결과는 튜플 형태로 반환
    return (addition_result, subtraction_result, multiplication_result, division_result)


# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 결과 저장을 위한 리스트
test_results = []

print("--- 테스트 실행 결과 (Console Output) ---")

# 테스트 실행 및 결과 저장
# 테스트 데이터 개수는 10개 조건 충족
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    results = calculate_all(a, b)

    # 디버깅 편의를 위한 콘솔 출력
    print(f"Case {i+1}: {a}, {b} => {results}")

    # 결과 딕셔너리 생성 (JSON 형식 구조를 위한 데이터)
    result_data = {
        "input_a": a,
        "input_b": b,
        "addition_result": results[0],
        "subtraction_result": results[1],
        "multiplication_result": results[2],
        "division_result": results[3]
    }

    test_results.append(result_data)

# 최종 JSON 결과 생성 및 출력 (조건 1 충족)
final_json_output = json.dumps(
    {
        "test_case_count": len(test_results),
        "test_data": test_results
    },
    indent=4,
    ensure_ascii=False
)

print("\n--- JSON 출력 (for 조건 1) ---")
print(final_json_output)

# VS Code 디버깅을 위해 여기에 중단점을 설정하면 각 단계의 변수 상태를 확인할 수 있음
# 예를 들어, 'test_results' 리스트의 변화를 관찰해보게.
```
