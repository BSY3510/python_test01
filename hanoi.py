def hanoi1(n, start, destination, term, l) :
    if n == 1 :
        l.append([start, destination])
        l[0] += 1
        return l
    else :
        hanoi1(n-1, start, term, destination, l)
        hanoi1(1, start, destination, term, l)
        hanoi1(n-1, term, destination, start, l)

def main1() :
    n = 3
    l = []
    count = 0
    l.append(count)
    hanoi1(n, 1, 3, 2, l)
    print(l[1:])
    print(l[0])

main1()

def hanoi2(n, start, destination, term) :
    if n == 1 :
        print(str(start) + "->" + str(destination), end = "  ")
    else :
        hanoi2(n-1, start, term, destination)
        hanoi2(1, start, destination, term)
        hanoi2(n-1, term, destination, start)

def main2() :
    n = 3
    hanoi2(n, 1, 3, 2)
    
main2()
