def get_user_input():
    while True:
        try:
            A = float(input('Area: '))
            break
        except ValueError:
            print('Please enter a number!')
    while True:
        try:
            E = float(input('Efficiency: '))
            break
        except ValueError:
            print('Please enter a number!')
    while True:
        try:
            T = float(input('Temperature Coefficient: '))
            break
        except ValueError:
            print('Please enter a number!')
    while True:
        try:
            N = float(input('NOCT: '))
            break
        except ValueError:
            print('Please enter a number!')
    return A, E, T, N

#print(get_user_input())
