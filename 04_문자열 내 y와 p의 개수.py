'''
문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.
'''

# 나의 풀이: 노가다 - p / P + y / Y 개수 세서 같은지 비교 후 True False 반환
def solution(s):
    p_count = 0
    y_count = 0
    for i in range(0, len(s)):
        if s[i] == 'p': # 이렇게 하지 않고 if s[i] == 'p' or s[i] == 'P' 도 작동하는 듯
            p_count += 1
        if s[i] == 'P':
            p_count += 1
        if s[i] == 'y':
            y_count += 1
        if s[i] == 'Y':
            y_count += 1
    if p_count == y_count:
        return True
    else:
        return False
print(solution('pychontjiosdYPfioqpwe'))

## 나의 풀이 개선점

def solution(s):
    p_count = 0
    y_count = 0
    for i in range(0, len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p_count += 1
        if s[i] == 'y' or s[i] == 'Y':
            y_count += 1
    if p_count == y_count:
        return True
    else:
        return False
print(solution('pychontjiosdYPfioqpwe'))

# 다른 풀이 1) count 함수 활용

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y') # 대/소문자 같게 취급할 땐 lower
                                                        # 문자열 메소드 count 활용하여 집계
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )