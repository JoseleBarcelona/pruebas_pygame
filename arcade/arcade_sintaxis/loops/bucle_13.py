for i in range(10):
    # Imprime los espacios del principio
    for j in range(10-i):
        print (" ",end=" ")
    # Cuenta hacia adelante
    for j in range(1,i+1):
        print (j,end=" ")
    # Cuenta atrás
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Fila siguiente
    print()

for i in range(10):
    # Imprime los espacios del principio
    for j in range(i+2):
        print (" ",end=" ")
    # Cuenta atrás
    for j in range(1,9-i):
        print (j,end=" ")
    # Fila siguiente
    print()

'''
                  1 
                1 2 1 
              1 2 3 2 1 
            1 2 3 4 3 2 1 
          1 2 3 4 5 4 3 2 1 
        1 2 3 4 5 6 5 4 3 2 1 
      1 2 3 4 5 6 7 6 5 4 3 2 1 
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1 
    1 2 3 4 5 6 7 8 
      1 2 3 4 5 6 7 
        1 2 3 4 5 6 
          1 2 3 4 5 
            1 2 3 4 
              1 2 3 
                1 2 
                  1 
'''