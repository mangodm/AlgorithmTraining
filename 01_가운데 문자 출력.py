# 1. 가운데 글자 가져오기
## 문제 설명: 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

def solution(s):
    if len(s)%2==0:
        return s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        return s[int(len(s)/2)]

## 풀이 1) 간결

def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1] # //(몫 연산자)를 활용한 연산: 굳이 if/else 쓰지 않고 처리

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
print(string_middle("powe"))
