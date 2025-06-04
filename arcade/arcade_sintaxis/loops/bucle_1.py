def print_for(asteriscos):
    for i in range(10):
        print(asteriscos, end=' ')

def print_while(asteriscos, veces):
    i = 0
    while i < veces:
        print(asteriscos, end=' ')
        i += 1

if __name__ == '__main__':
    print_for('*')
    print('')
    print_while('*', 10)

