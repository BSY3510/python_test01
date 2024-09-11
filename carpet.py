def solution(brown, yellow):
    # yellow의 약수를 찾아 가능한 가로와 세로 경우의 수를 계산
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            y_w = yellow // i  # 노란 타일의 가로
            y_h = i            # 노란 타일의 세로
            
            # 전체 카펫의 가로와 세로 계산 (가로는 y_w + 2, 세로는 y_h + 2)
            width = y_w + 2
            height = y_h + 2
            
            # 전체 타일 수가 brown과 yellow의 합과 같은지 확인
            if width * height == brown + yellow:
                return [width, height]

    return []

brown = 24
yellow = 24
print(solution(brown, yellow))