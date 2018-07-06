'''
문제 설명
문자열 s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수, solution을 완성하세요.
예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
'''

# 나의 풀이: 중첩 if-else 활용
def solution(s):
    if len(s) == 4:
        if s.isnumeric() == True:
            return True
        else:
            return False
    else:
        return False

# 다른 풀이: isdigit 메소드 & len() 활용
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6) # and 연산자면 둘 다 만족하는 경우 True 나머지는 False
    # 들어온 문자열이 digit으로 되어 있느냐 + s의 길이가 4 혹은 6이냐
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )
