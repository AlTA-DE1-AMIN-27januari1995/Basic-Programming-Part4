def draw_xyz(N):
    count = 1
    for i in range(N):
        for j in range(N):
            if count % 3 == 0:
                # untuk kelipatan tiga cetak 'X'
                print('X', end = ' ')
            elif count % 2 == 0:
                # untuk kelipatan dua (genap) cetak 'Z'
                print('Z', end = ' ')
            else:
                # untuk kelipatan ganjil cetak 'Y'
                print('Y', end = ' ')
            count += 1
        print()

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """