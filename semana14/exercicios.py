#1. Crie um arquivo contendo uma lista de números separados por vírgulas. Escreva
#um programa que lê esses números do arquivo e calcula a média deles.

def calculate_avg():
    my_file = open("exercicio-01.txt","r")
    file_content = my_file.read()
    number_list = file_content.split(",")
    sum_of_numbers = 0
    for number in number_list:
        sum_of_numbers = sum_of_numbers + int(number)
    
    return sum_of_numbers / len(number_list)

def main():
    result = calculate_avg()
    print(result)

main()
