from math import nan as NaN

dato = ['', 'u', 'x','','m','','g','','','y','u']             # 1
liga = [NaN, 9, None, NaN, 6, NaN, 1, NaN, NaN, 10, 2]        # 1
print(f"Vector Dato: {dato}")                                 # 1
print(f"Vector Liga: {liga}")                                 # 1

primero = 4                                                   # 1
actual = primero                                              # 1

while(actual != None):                                        # n+1
    print(dato[actual])                                       # n
    actual = liga[actual]                                     # n