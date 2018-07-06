# 2. 두 정수 사이의 합
'''
1. 문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

2. 제한 조건
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.
'''

# 나의 풀이:
def solution(a, b):
    if a > b:
        sum = 0
        my_list = list(range(b, a + 1))
        for i in my_list:
            sum += i
        return sum
    else:
            sum = 0
            my_list = list(range(a, b + 1))
            for i in my_list:
                sum += i
            return sum

# 다른 풀이 1) a, b = b, a 활용
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a # 뭐가 a이고 b인지는 중하지 않으니 변경해버리는 것.

    return sum(range(a,b+1))  # 위에서의 변환을 통해 식을 한번만 써서 함수를 간편하게 정의 가능

# 다른 풀이 2) 절대값 활용
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))

# 수와 관련한 문제에서 고려할 요소: 1) 짝수/홀수 2) 몫 연산자 3) 나머지 연산자 4) 절대값 