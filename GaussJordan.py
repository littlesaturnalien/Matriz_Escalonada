class GaussJordan():
    def __init__(self, matriz: list[list]) -> None:
        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0])
        self.filas_pivotes = set()
    
    @staticmethod
    def crear_matriz(cantFilas: int, cantColum: int) -> list[list[float]]:
        matriz = []
        print("\nOJO: Separa con espacios y escribe 0 cuando falte una variable.")
        for fila in range(cantFilas):
            while True:
                try:
                    print(f"Ingrese los {cantColum} valores para la fila {fila + 1}:")
                    entrada = input(" ----> ")
                    print()
                    caracteres_validos = set("0123456789.- ")
                    if not all(char in caracteres_validos for char in entrada):
                        raise ValueError("Entrada inválida. Usa solo números, puntos" 
                                         " decimales, signos negativos y espacios.")
                    contenido = list(map(float, entrada.split()))
                    if len(contenido) != cantColum:
                        raise ValueError(f"Debes introducir exactamente {cantColum} números.")
                    matriz.append(contenido)
                    break
                except ValueError as Error:
                    print(Error)
        return matriz
    
    def gauss_jordan(self):
        for col in range(self.columnas - 1):
            if not self.convertir_a_1(col):
                print(f"No se puede encontrar un pivote adecuado en la columna {col+1}.")
                continue
            self.reduccion_a_cero(col)
                
    def intercambio(self, fila, fila_intercambio) -> None:
        #No es necesario crear variables temporales
        self.matriz[fila],self.matriz[fila_intercambio] = self.matriz[fila_intercambio],self.matriz[fila]
        print(f"\nF{fila + 1} <--> F{fila_intercambio + 1}\n")
        self.imprimir_matriz()
        self.filas_pivotes.remove(fila)
        self.filas_pivotes.add(fila_intercambio)
    
    def pivote(self, col : int) -> int | bool:
        for fila in range(self.filas):
            if self.matriz[fila][col] != 0 and fila not in self.filas_pivotes:
                self.filas_pivotes.add(fila)
                return fila
        return False


    def convertir_a_1(self, col : int) -> bool:
        pivote_fila = self.pivote(col)
        if pivote_fila is False:
            return False
        
        pivote = self.matriz[pivote_fila][col]
    
        if pivote == 1: return True

        self.matriz[pivote_fila] = [x / pivote for x in self.matriz[pivote_fila]]
        print(f"\nF{pivote_fila + 1} -> F{pivote_fila + 1} / {int(pivote) if pivote.is_integer() else f'{pivote:.1f}'}\n")
        self.imprimir_matriz()

        if pivote_fila != col and pivote_fila not in self.filas_pivotes:
            self.intercambio(col, pivote_fila)

        return True

    
    #Cuando hay columna pivote
    def reduccion_a_cero(self, col : int):
        pivote_fila = None
        for fila in self.filas_pivotes:
            if self.matriz[fila][col] == 1:
                pivote_fila = fila
                break

        for fila in range(self.filas):
            if fila == pivote_fila: continue
            if self.matriz[fila][col] == 0: continue
            operando = self.matriz[fila][col] * -1
            operando_tipo = int(operando) if operando.is_integer() else f"{operando:.1f}"
            self.matriz[fila] = [self.matriz[fila][i] + (operando * self.matriz[pivote_fila][i]) for i in range(self.columnas)]

            if operando > 0:
                operador = "+"
            else:
                operador = "-"
                operando_tipo = -operando_tipo

            print(f"\nF{fila + 1} -> F{fila + 1} {operador} {operando_tipo}F{pivote_fila + 1}\n")
            self.imprimir_matriz()
    
    
    def soluciones(self):
        for fila in range(self.filas):
            if all(self.matriz[fila][i] == 0 for i in range(self.columnas - 1)) and self.matriz[fila][-1] != 0:
                print("\nLa matriz no tiene solución.")
                return
            
            filas_no_nulas = [fila for fila in self.matriz if any(f != 0 for f in fila[:-1])]
            if len(filas_no_nulas) < self.columnas - 1:
                print("\nLa matriz tiene infinitas soluciones.\n")
                self.variables_libres()
                return

        print("\nLa matriz tiene una solución única:\n")
        soluciones = []
        for fila in range(self.filas):
            if fila < self.columnas - 1:
                soluciones.append(self.matriz[fila][-1])
        for i, sol in enumerate(soluciones):
            print(f"X{i+1} = {int(sol) if sol.is_integer() else f'{sol:.1f}'}")

    def variables_libres(self):
        columnas_pivotes = []
        for fila in range(self.filas):
            for col in range(self.columnas - 1):
                if self.matriz[fila][col] !=1: continue
                if any(self.matriz[fila][i] != 0 for i in range(col)): continue
                columnas_pivotes.append(col)
                break

        for col in range(self.columnas - 1):
            if col not in columnas_pivotes:
                print(f'X{col+1} es una variable libre')
                continue
            for fila in range(self.filas):
                if self.matriz[fila][col] != 1: 
                    continue
                resultado = self.matriz[fila][-1]
                expr = f"X{col+1} = " + ((f"{int(resultado) if resultado.is_integer() else f'{resultado:.1f}'}") 
                                          if resultado != 0 else "")
                for i, valor in enumerate(self.matriz[fila][:-1]):
                    if i in columnas_pivotes: continue
                    if valor == 0: continue
                    operador, valor = (" -",valor) if valor > 0 else(" +",-valor)
                    expr += f"{operador} ({int(valor) if valor.is_integer() else f'{valor:.1f}'})X{i+1}"
                print(expr)
        

    def imprimir_matriz(self):
        for fila in self.matriz:
            for valor in fila:
                print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
            print()