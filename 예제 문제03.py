line = input()
l = line.split()

num_s = l[0]
num_l = l[1]
count = 1
max_count = 1

if num_s.isdigit() and num_l.isdigit() :
    num_s = int(num_s)
    num_l = int(num_l)
else :
    num_s = None
    num_l = None

for i in range(num_s, num_l+1) :
    count = 1
    while True :
        try :
            if not i or i == 1 :
                break
            if i%2 == 0 :
                i = i/2
            else :
                i = i * 3 + 1
            count += 1
        except EOFError :
            break
    if count > max_count :
        max_count = count
    
print(num_s, num_l, max_count)
