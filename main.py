from GaussJordan import GaussJordan as GJ

def main():
    filas = int(input("Ingresa la cantidad de filas de la matriz: "))
    columnas = int(input("Ingresa la cantidad de columnas de la matriz: "))
    matriz = GJ.crear_matriz(filas, columnas)
    
    print("\nSISTEMA DE ECUACIONES INGRESADO\n")
    matriz_aumentada = GJ(matriz)
    matriz_aumentada.imprimir_ecuaciones()

    print("\nMATRIZ A RESOLVER:\n")
    for fila in matriz:
        for valor in fila:
            print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
        print()
    
    matriz_aumentada.gauss_jordan()
    matriz_aumentada.soluciones()

if __name__ == '__main__':
    main()