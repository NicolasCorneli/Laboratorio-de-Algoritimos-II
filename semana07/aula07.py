list1 = [2,1,0,6,5,4,3,7,9,8]
for i in range(len(list1)):
    print(list1)
    for x in range(len(list1)):
        if list1[i] < list1[x]:
            v = list1[i]
            z = list1[x]
            list1[i] = z
            list1[x] = v
print(list1)

matrix = [[5,9,8],[4,3,7],[1,2,6]]
for line in range(len(matrix)):
    for column in range(len(matrix[line])):
        min_line = line
        min_column = column
        
        for line_aux in range(line,len(matrix)):
            start = column if line == line_aux else 0
            for column_aux in range(column, len(matrix[line_aux])):
                if matrix[line_aux][column_aux] < matrix[min_line][min_column]:
                    min_line =  line_aux
                    min_column = column_aux
        #Armazena o menor valor            
        min_value = matrix[min_line][min_column]
        #Armazena na posição do menor valor o valor atual
        matrix[min_line][min_column] = matrix[line][column]
        #Armazena no valor atual o menor valor
        matrix[line][column] = min_value
        
print(matrix)
