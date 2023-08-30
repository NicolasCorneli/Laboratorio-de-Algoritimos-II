#1. Escreva uma função que recebe uma lista de números e crie um dicionário que seja estruturado como sendo o
#número a chave e a quantidade de vezes que o número está presente o valor. Exemplo: [1, 2, 3, 4, 5, 4, 3] => { 1: 1, 2:
#1, 3: 2, 4: 2, 5: 1 }

def count_numbers(my_list):
    count_dict = {}
    for number in my_list:
        if number in count_dict:
            count_dict[number] = count_dict[number] + 1
        else:
            count_dict[number] = 1
            
    return count_dict
    
    
def main():
    my_list = [1,2,3,4,5,4,3]
    result = count_numbers(my_list)
    
    print(result)
    
    
main()
