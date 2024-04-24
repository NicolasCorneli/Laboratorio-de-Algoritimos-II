#matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]
for line in range(len(matriz)):
    for column in range(len(matriz[line])):
        print(matriz[line][column], end=" ")
    print(end="\n")
#EXEMPLO 1

def scale(matriz,scale_value):
    result = []
    for line in range(len(matriz)):
        result.append([])
        for column in range(len(matriz[line])):
            result[line].append(matriz[line][column] * scale_value)
           
    return result        
def main():
    matriz = [[5,32,5],[3,76,43],[20,27,83]]
    result = scale(matriz,5)
    print(result)

main()
#EXEMPLO 2
def diagonal_multiplicator(matriz):
    result = 1
    for line in range(len(matriz)):
        for column in range(len(matriz[line])):
            if line == column:
                result = result * matriz[line][column]
                
    return result  
    
def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    result = diagonal_multiplicator(matriz)
    print(result)
    
main()

#Invertendo uma Lista em Python sem Usar Métodos Interno
def invert_list(list1):
    reverse = list1[::-1]
    return reverse

def main():
    list1 = [1,2,3,4,5,6,7,8,9]
    reverse = invert_list(list1)
    print(reverse)
main()
    
#Crie um método que receba uma lista com elementos duplicados. Ela deve gerar uma lista com os elementos que estava duplicados e uma lista com os elementos unificados.
def organizator(my_list):
    uniq_list = []
    duplicated_list = []
    for item in my_list:
        if item not in uniq_list:
            uniq_list.append(item)
        else:
            duplicated_list.append(item)
    return uniq_list, duplicated_list

def main():
    my_list = [1,2,2,3,4,5,6,1,7]
    uniq_list, duplicated_list = organizator(my_list)
    print(uniq_list)
    print(duplicated_list)
main()
# A partir de uma matriz 3 x 3 numérica, percorra a matriz e some os maiores valores de cada linha.

def a(matriz):
    final_list = []
    for line in range(len(matriz)):
        total = 0
        number = matriz[line][0]
        for column in range(len(matriz[line])):
            if matriz[line][column] > number:
                number = matriz[line][column]
                total = total + number
        final_list.append(total)
    print(final_list)
def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    a(matriz)
    
main()
#A partir de uma matriz 3 x 3 numérica, percorra a matriz e calcule o valor médio total da matriz e de cada linha.

def average_line(matriz):
    final_average_list = []
    for line in range(len(matriz)):
        average = 0
        for column in range(len(matriz[line])):
            average = average + matriz[line][column]
            RealAverage = average / 3
        final_average_list.append(RealAverage)
    print(final_average_list)
    
def all_matriz_average(matriz):
    final_matriz_list = []
    average = 0
    for line in range(len(matriz)):
        for column in range(len(matriz[line])):
            average = average + matriz[line][column]
            RealAverage = average / 9
    final_matriz_list.append(RealAverage)
    print(final_matriz_list)
def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    average_line(matriz)
    all_matriz_average(matriz)
main()
#Escreva uma função que recebe duas matrizes como entrada e retorna uma nova matriz que é a soma das duas matrizes. Ambas matrizes devem possuir o tamanho de 3 x 3.

def matrizes(matriz1,matriz2):
    matriz3 = []
    for line in range(len(matriz1)):
        for column in range(len(matriz1[line])):
            sum1 = matriz1[line][column] + matriz2[line][column]
            matriz3.append(sum1)
    print(matriz3)
       
def main():
    matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
    matriz2 = [[9,8,7],[6,5,4],[3,2,1]]
    matrizes(matriz1,matriz2)
main()
