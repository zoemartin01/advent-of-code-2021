with open('input.txt', 'r') as f:
    l = f.readlines()
    c = 0


    for i in range(1, len(l)):
        if int(l[i]) > int(l[i - 1]):
            c += 1
    
    print(c)