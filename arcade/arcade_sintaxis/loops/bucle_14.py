for i in range(10):
    # Imprimimos espacios al principio de la línea
    for j in range(10-i):
        print (" ",end=" ")
    # Cuenta hacia arriba
    for j in range(1,i+1):
        print (j,end=" ")
    # Cuenta atrás
    for j in range(i-1,0,-1):
        print (j,end=" ")
    #Fila siguiente
    print()

for i in range(10):
    #Imprimimos espacios al principio de la línea
    for j in range(i+2):
        print (" ",end=" ")
    # Cuenta hacia arriba
    for j in range(1,9-i):
        print (j,end=" ")
    # Cuenta atrás
    for j in range(7-i,0,-1):
        print (j,end=" ")
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
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 
      1 2 3 4 5 6 7 6 5 4 3 2 1 
        1 2 3 4 5 6 5 4 3 2 1 
          1 2 3 4 5 4 3 2 1 
            1 2 3 4 3 2 1 
              1 2 3 2 1 
                1 2 1 
                  1 
                    
                      
'''