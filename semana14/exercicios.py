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

#2. Crie um arquivo de texto contendo várias linhas de texto. Escreva um programa
#que solicita ao usuário uma palavra e verifica se essa palavra está presente no
#arquivo. Se estiver, o programa deve imprimir a linha em que a palavra foi
#encontrada.

def verify_word():
    word = input("Digite uma palavra: ")
    my_file = open("exercicio-02.txt","r")
    file_content_line = my_file.readline()
    line_count = 0
    
    while file_content_line != "":
        line_count = line_count + 1
        
        if word == file_content_line:
            print(line_count)
        
        file_content_line = my_file.readline()
    
    my_file.close()
    
def main():
    verify_word()


main()

#3. Crie um programa que pede ao usuário para digitar o nome de um arquivo. Em
#seguida, o programa deve criar uma cópia desse arquivo com o nome
#"copia_nomeoriginal" (por exemplo, se o arquivo original for "exemplo.txt", a cópia deve ser "copia_exemplo.txt").
