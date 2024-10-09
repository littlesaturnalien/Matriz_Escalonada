import copy
from math import isclose

class GaussJordan():
    def __init__(self, matriz) -> None:
        self.matriz = matriz
        self.filas_pivotes = set()#Para almacenar el índice de filas que contienen pivotes como valores únicos
        self.filas = len(matriz) #Cantidad de filas
        self.columnas = len(matriz[0]) #Cantidad de columnas
        self.config = {}
        self.tolerance = 1e-15

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
                #print(f"\nNo se puede encontrar un pivote adecuado en la columna {col+1}.")
                continue
            self.reduccion_a_cero(col)
        self.soluciones()

        return self.config
                

    def intercambio(self, fila, fila_intercambio) -> None:
        '''Es una función que no devuelve nada.
        Tiene como parámetros el índice de la fila sin pivote y el índice de la fila con pivote para intercambiarlas.'''

        self.matriz[fila],self.matriz[fila_intercambio] = self.matriz[fila_intercambio],self.matriz[fila]
        self.config[f'F{fila + 1} <--> F{fila_intercambio + 1}'] = copy.deepcopy(self.matriz)
    
    def pivote(self, col : int) -> int | bool:
        '''Es una función que devuelve un entero (int) o False.
        Parámetro: el índice de la columna para evaluar si contiene un pivote adecuado.

        Mediante un ciclo, se itera por cada valor de la columna evaluada de manera vertical.
        Si un término es distinto que 0 y el índice de su fila no se encuentra en el set() de la clase,
        la función retorna ese mismo índice y continúa con las operaciones.
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
        fila disponible sin pivote, lo cual da paso a un intercambio entre filas si es necesario. Por último, se actualiza el set()'''

        pivote_fila = self.pivote(col)
        if pivote_fila is False:
            return False
        
        pivote = self.matriz[pivote_fila][col]
    
        if pivote != 1:
            self.matriz[pivote_fila] = [x / pivote for x in self.matriz[pivote_fila]]
            self.config[f"F{pivote_fila + 1} -> F{pivote_fila + 1} / {int(pivote) if pivote.is_integer() else f'{pivote:.5f}'}"] = copy.deepcopy(self.matriz)

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
        '''Parámetros: índice de la columna con pivote
        Teniendo en cuenta que a este punto del programa, ya existe un 1 en la columna a trabajar, el pivote 1 
        se busca mediante un for y se le asigna a la variable pivote_fila el índice de la fila donde se encuentra.
        De este modo, se transforma el resto de números de la columna a 0 (exceptuando la fila pivote).'''

        pivote_fila = None
        for fila in self.filas_pivotes:
            if self.matriz[fila][col] == 1 and all(number !=1 for number in self.matriz[fila][:col]):
                pivote_fila = fila
                break

        for fila in range(self.filas):
            if fila == pivote_fila: continue
            if self.matriz[fila][col] == 0: continue
            operando = self.matriz[fila][col] * -1
            self.matriz[fila] = [
                    0 if isclose(self.matriz[fila][i] + (operando * self.matriz[pivote_fila][i]), 0, abs_tol=self.tolerance) 
                    else self.matriz[fila][i] + (operando * self.matriz[pivote_fila][i]) 
                    for i in range(self.columnas)
                ]

            if operando > 0:
                operador = "+"
            else:
                operador = "-"
                operando = -operando
            
            operando_tipo = int(operando) if operando.is_integer() else f"{operando:.5f}"
            
            self.config[f"F{fila + 1} -> F{fila + 1} {operador} {operando_tipo}F{pivote_fila + 1}"] = copy.deepcopy(self.matriz)
    
    
    def soluciones(self):
        '''Si la matriz tiene una fila con ceros menos en la columna de resultados, no hay solución.
        Si en la matriz hay menos filas no nulas (es decir, con coeficientes) que columnas de incógnitas,
        existen infinitas soluciones.
        Si ninguno de estos casos se cumplen, se asume que la matriz presenta una solución única y los
        resultados de las incógnitas se muestran en pantalla.'''

        '''print("\n\nSOLUCIÓN EN FORMA DE ECUACIONES:\n")
        self.imprimir_ecuaciones()
        print()'''

        for fila in range(self.filas):
            if all(self.matriz[fila][i] == 0 for i in range(self.columnas - 1)) and self.matriz[fila][-1] != 0:
                self.config['La matriz no tiene solucion'] = (copy.deepcopy(self.matriz),'')
                return
            
        filas_no_nulas = [fila for fila in self.matriz if any(f != 0 for f in fila[:-1])]
        if len(filas_no_nulas) < self.columnas - 1:
            self.config['La matriz tiene infinitas soluciones'] = (copy.deepcopy(self.matriz),self.variables_libres())
            self.variables_libres()
            return

        soluciones = []
        for fila in range(self.filas):
            if fila < self.columnas - 1:
                soluciones.append(self.matriz[fila][-1])
        for i, sol in enumerate(soluciones):
            soluciones[i] = f"X{i+1} = {int(sol) if sol.is_integer() else f'{sol:.5f}'}"
        self.config['La matriz tiene una solucion única'] = (copy.deepcopy(self.matriz),soluciones)


    def variables_libres(self):
        '''Se ejecuta cuando la matriz tiene infinitas soluciones.
        En una lista se almacenan las columnas con pivotes (1). Si la lista no contiene el índice
        de una columna, se considera que esa columna tiene una variable libre.'''
        variables = []
        columnas_pivotes = []
        for fila in range(self.filas):
            for col in range(self.columnas - 1):
                if self.matriz[fila][col] !=1: continue
                if any(self.matriz[fila][i] != 0 for i in range(col)): continue
                columnas_pivotes.append(col)
                break
        
        for col in range(self.columnas - 1):
            if col not in columnas_pivotes:
                variables.append(f'X{col+1} es una variable libre')
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
                    expr += f"{operador} {("(" + str(int(valor)) + ")" if valor.is_integer() else f'{valor:.1f}') if valor != 1 else ""}X{i+1}"
                variables.append(expr)
        return variables

    def imprimir_ecuaciones(self):
        for fila in range(self.filas):
            ecuacion = ""
            for col in range(self.columnas - 1):
                valor = self.matriz[fila][col]
                if valor == 0: continue
                if valor > 0 and ecuacion != "":
                    operador = "+"
                elif valor < 0:
                    operador = "-"
                    valor = -valor
                else: operador = ""
                coef = f"{("(" + str(int(valor)) + ")" if valor.is_integer() else f'{valor:.1f}') if valor != 1 else ""}"
                if operador:
                    ecuacion += f" {operador} {coef}X{col + 1}"
                else:
                    ecuacion += f"{coef}X{col + 1}"

            resultado = self.matriz[fila][-1]
            if resultado == 0 and all(self.matriz[fila][i] == 0 for i in range(self.columnas - 1)):
                ecuacion = "0 = 0"
                print(ecuacion)
                continue
            
            ecuacion += f" = {int(resultado) if resultado.is_integer() else f'{resultado:.1f}'}"

            print(ecuacion)
    
    def __str__(self) -> str:
        matriz : str = ''
        maximo_tamaño_fila = max(len(f'{round(self.matriz[fila][columna], 3)}') for fila in range(self.filas) for columna in range(self.columnas)) + 2
        for fila in range(self.filas):
            fila_str = ''
            for columna in range(self.columnas):
                fila_str += f'{round(self.matriz[fila][columna], 3):<{maximo_tamaño_fila}}'
            matriz += fila_str + '\n'
        return matriz

    @staticmethod
    def vxv_get_scalar(row_vector,column_vector):
        scalar = sum([row * column for row,column in zip(row_vector,column_vector)])
        return scalar
    
    @staticmethod
    def mxv_get_scalar(matrix_vectors:list[list],column_vector:list|list[list]) -> list:
        scalar_vector = list()
        if isinstance(column_vector[0],list):
            column_vector = [sum(vector) for vector in column_vector]
        for row in matrix_vectors:
            scalar_product = sum(row[i] * column_vector[i] for i in range(len(column_vector)))
            scalar_vector.append(scalar_product)
        return scalar_vector
    
    @staticmethod
    def obtener_matriz_transpuesta(normal_matrix) ->list[list]:
        matriz_transpuesta = [[normal_matrix[fila][col] for fila in range(len(normal_matrix))] 
                      for col in range(len(normal_matrix[0]))]

        return matriz_transpuesta
                
