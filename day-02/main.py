with open('input.txt', 'r') as f:
    h = 0
    d = 0

    for s in f.readlines():
        (x, y) = s.replace('\n', '').split(' ', 1)
        if x == 'forward':
            h += int(y)
        elif x == 'down':
            d += int(y)
        elif x == 'up':
            d -= int(y)
        
    print(f'horizontal: {h} - depth: {d} - combined: {h * d}')