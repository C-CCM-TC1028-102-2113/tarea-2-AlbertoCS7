def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if(x<y and y<z):
        print( x, y, z)
    else(y<x and x<z):  ##EL ELSE NO LLEVA CONDICION, SU SINTAXIS ES ELSE: UNICAMENTE
        print( y, x, z)
    else(z<x and x<y): ##EL ELSE NO LLEVA CONDICION, SU SINTAXIS ES ELSE: UNICAMENTE
        print(z, x, y)
    else(z<y and y<x): ##EL ELSE NO LLEVA CONDICION, SU SINTAXIS ES ELSE: UNICAMENTE
        print(z, y, x) 
    else(x<z and z<y)##EL ELSE NO LLEVA CONDICION, SU SINTAXIS ES ELSE: UNICAMENTE
        print(x, z, y)     
    else(y<z and z<x):##EL ELSE NO LLEVA CONDICION, SU SINTAXIS ES ELSE: UNICAMENTE
        print(y, z, x)
    pass


if __name__=='__main__':
    main()
