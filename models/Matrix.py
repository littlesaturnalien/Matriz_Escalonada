from models.GaussJordan import GaussJordan as GJ
class Matrix():

    def __init__(self,matriz: list[list]) -> None:
        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0])

    def obtener_matriz_transpuesta(self) ->list[list]:
        matriz_transpuesta = [[self.matriz[fila][col] for fila in range(self.filas)] for col in range(self.columnas)]
        return matriz_transpuesta
    
    def obtener_pasos_reduccion(self) ->dict:
        gauss_jordan = GJ(self.matriz)
        pasos = gauss_jordan.gauss_jordan()
        return pasos

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
    

    def __str__(self) -> str:
        matriz : str = ''
        maximo_tamaño_fila = max(len(f'{round(self.matrix[fila][columna], 3)}') for fila in range(self.width) for columna in range(self.length)) + 2
        for fila in range(self.width):
            fila_str = ''
            for columna in range(self.length):
                fila_str += f'{round(self.matrix[fila][columna], 3):<{maximo_tamaño_fila}}'
            matriz += fila_str + '\n'
        return matriz
    
    