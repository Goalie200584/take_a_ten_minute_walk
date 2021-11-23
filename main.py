def is_valid_walk(walk):
    loc = [0, 0]      # [x, y]
    # walk = [dir, dir, dir, dir]

    for dir in walk:
        if dir == 'n':
            loc[1] += 1
        elif dir == 's':
            loc[1] -= 1
        elif dir == 'w':
            loc[0] -= 1
        elif dir == 'e':
            loc[0] += 1
        else:
            print('You crazy')

    if loc == [0,0] and len(walk) == 10:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))