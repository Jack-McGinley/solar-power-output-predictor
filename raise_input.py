def get_user_input():
    """
    Function to get user input for solar panel parameters: Area, Efficiency,
    Temperature Coefficient, and NOCT. Ensures that inputs are valid floats.
    Returns: A tuple containing the values (Area, Efficiency, Temperature Coefficient, NOCT)
    """
    while True: #pass user inputs with error handling, allow users to input until try is successful
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
    return A, E, T, N #return the user inputs as a tuple

#print(get_user_input())