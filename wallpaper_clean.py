def solution(wallpaper):
    answer = []
    max_x = 0
    max_y = 0
    min_x = len(wallpaper[0])
    min_y = len(wallpaper)
    for idx, row in enumerate(wallpaper) :
        for x, s in enumerate(row) :
            if ("#" == s) :
                if (min_x > x) :
                    min_x = x
                if (min_y > idx) :
                    min_y = idx
                if (max_x < x) :
                    max_x = x
                if (max_y < idx) :
                    max_y = idx
                
    answer = [min_y, min_x, max_y+1, max_x+1]
            
    return answer

wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
print(solution(wallpaper))