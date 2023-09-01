line = input()
answer = 0
if line[:2] == "0x" :
    answer = int(line, 16)
else :
    answer = hex(int(line))

print(answer)
