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

def a(list1):
    duplicated_list = []
    unified_list = []
    for x in range(len(list1)):
        if list1[x] not in unified_list:
            unified_list.append(list1[x])
        if list1[x] == list1[x-1]:
            duplicated_list.append(list1[x])
    print(unified_list)
    print(duplicated_list)
def main():
    list1 = [1,1,2,2,3,3,4,5]
    a(list1)
    
    
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
