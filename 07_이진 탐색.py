# 이진 탐색(binary search) 알고리즘

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high: # 만약 탐색 범위를 좁히지 못했으면 계속 실행
        mid = (low + high) // 2 # 가운데 숫자를 확인
        guess = list[mid]

        if guess == item: # 아이템을 찾은 경우 
            return mid
        if guess > item: # 추측한 숫자가 너무 큰 경우
            high = mid - 1
        else: # 추측한 숫자가 너무 작은 경우
            low = mid + 1

    return None # 지정한 아이템이 없는 경우 None을 반환


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
