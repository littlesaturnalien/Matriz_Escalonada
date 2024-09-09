class GaussJordan():
    def __init__(self, matriz: list[list]) -> None:
        self.matriz = matriz
        self.filas = len(matriz) #Cantidad de filas
        self.columnas = len(matriz[0]) #Cantidad de columnas
        self.filas_pivotes = set() #Para almacenar el índice de filas que contienen pivotes como valores únicos
    
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
        '''Se inicializa el proceso de eliminación Gauss Jordan.
        Se recorren los índices de cada columnas menos la de resultados, es decir, de manera horizontal, para determinar un pivote.
        En caso de que se encuentre una columna pivote, se procede a reducir los elementos de la 
        columna correspondiente a 0, excepto el 1.'''

        for col in range(self.columnas - 1):
            if not self.convertir_a_1(col):
                print(f"No se puede encontrar un pivote adecuado en la columna {col+1}.")
                continue
            self.reduccion_a_cero(col)
                
    def intercambio(self, fila, fila_intercambio) -> None:
        '''Es una función que no devuelve nada.
        Tiene como parámetros el índice de la fila sin pivote y el índice de la fila con pivote para intercambiarlas.'''

        temp = self.matriz[fila]
        self.matriz[fila] = self.matriz[fila_intercambio]
        self.matriz[fila_intercambio] = temp
        print(f"\nF{fila + 1} <--> F{fila_intercambio + 1}\n")
        self.imprimir_matriz()

    
    def pivote(self, col : int) -> int | bool:
        '''Es una función que devuelve un entero (int) o False.
        Parámetro: el índice de la columna para evaluar si contiene un pivote adecuado.

        Mediante un ciclo, se itera por cada valor de la columna evaluada de manera vertical.
        Si un término es distinto que 0 y el índice de su fila no se encuentra en el set() de la clase, 
        se agrega el índice al set(). La función luego retorna ese mismo índice y continúa con las operaciones.
        En caso de no cumplirse niguno de los criterios, se retorna un False.'''

        for fila in range(self.filas):
            if self.matriz[fila][col] != 0 and fila not in self.filas_pivotes:
                return fila
        return False


    def convertir_a_1(self, col : int) -> bool:
        '''Es una función que devuelve True o False.
        Parámetro: el índice de la columna para evaluar si contiene un pivote adecuado.
        
        Primero, se revisa si en la columna hay presente un pivote. En caso de que no, se retorna un False y termina el proceso.
        
        En el caso contrario, con el índice dado de la fila en la que se encuentra el pivote, se obtiene el número pivote en la
        columna en la que se está trabajando. Si el pivote es diferente que 1, la fila que lo contiene se divide con el pivote
        para transformarlo en 1. 
        
        Igualmente, hay otra condicional if que verifica si el índice de la fila con el pivote es distinta al índice de la primera
        fila disponible sin pivote, lo cual da paso a un intercambio entre filas.'''

        pivote_fila = self.pivote(col)
        if pivote_fila is False:
            return False
        
        pivote = self.matriz[pivote_fila][col]
    
        if pivote != 1:
            self.matriz[pivote_fila] = [x / pivote for x in self.matriz[pivote_fila]]
            print(f"\nF{pivote_fila + 1} -> F{pivote_fila + 1} / {int(pivote) if pivote.is_integer() else f'{pivote:.1f}'}\n")
            self.imprimir_matriz()

        for fila in range(self.filas):
            if fila not in self.filas_pivotes:
                fila_sin_pivote = fila
                break
        
        if pivote_fila != fila_sin_pivote:
            self.intercambio(fila_sin_pivote, pivote_fila)
            pivote_fila = fila_sin_pivote

        self.filas_pivotes.add(pivote_fila)
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
            self.matriz[fila] = [self.matriz[fila][i] + (operando * self.matriz[pivote_fila][i]) for i in range(self.columnas)]

            if operando > 0:
                operador = "+"
            else:
                operador = "-"
                operando = -operando
            
            operando_tipo = int(operando) if operando.is_integer() else f"{operando:.1f}"
            
            print(f"\nF{fila + 1} -> F{fila + 1} {operador} {operando_tipo}F{pivote_fila + 1}\n")
            self.imprimir_matriz()
    
    
    def soluciones(self):
        for fila in range(self.filas):
            if any(self.matriz[fila][i] == 0 for i in range(self.columnas - 1)) and self.matriz[fila][-1] != 0:
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
                if self.matriz[fila][col] == 1 and all(self.matriz[fila][i] == 0 for i in range(col)):
                    columnas_pivotes.append(col)
                    break
        
        variables_libres = [i for i in range(self.columnas - 1) if i not in columnas_pivotes]

        for col in range(self.columnas - 1):
            if col in columnas_pivotes:
                for fila in range(self.filas):
                    if self.matriz[fila][col] == 1:
                        resultado = self.matriz[fila][-1]
                        expr = f"X{col+1} = " + ((f"{int(resultado) if resultado.is_integer() else f'{resultado:.1f}'}") 
                                                  if resultado != 0 else "")
                        for i, valor in enumerate(self.matriz[fila][:-1]):
                            if i in variables_libres and valor != 0:
                                if valor > 0:
                                    operador = " -"
                                else:
                                    operador = " +"
                                    valor = -valor
                                expr += f"{operador} ({int(valor) if valor.is_integer() else f'{valor:.1f}'})X{i+1}"
                        print(expr)
            elif col in variables_libres:
                print(f"X{col + 1} es una variable libre")
        

    def imprimir_matriz(self):
        for fila in self.matriz:
            for valor in fila:
                print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
            print()