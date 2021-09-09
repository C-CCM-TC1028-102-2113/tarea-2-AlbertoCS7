
def main():
    #Escribe tu código debajo de esta línea
    edad = int(input("Dime tu edad: "))
    

    if (edad>=18):
        identificacion = str(input("¿Tienes identificacion? (s/n): "))
        if (identificacion=="s"):
            print("Trámite de licencia concedido :)") 
        elif (identificacion=="n"):
             print("No cumples los requisitos")    
        else:
             print("Respuesta incorrecta")
   
    else:
        print("No cumples requisitos")
    pass


if __name__ == '__main__':
    main()
