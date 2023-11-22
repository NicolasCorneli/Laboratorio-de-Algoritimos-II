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
    file_content_line = my_file.readline().rstrip("\n")
    line_count = 0
    
    while file_content_line != "":
        line_count = line_count + 1
        
        if word == file_content_line:
            print(line_count)
        
        file_content_line = my_file.readline().rstrip("\n")
    
    my_file.close()
    
def main():
    verify_word()


main()

#3. Crie um programa que pede ao usuário para digitar o nome de um arquivo. Em
#seguida, o programa deve criar uma cópia desse arquivo com o nome
#"copia_nomeoriginal" (por exemplo, se o arquivo original for "exemplo.txt", a cópia deve ser "copia_exemplo.txt").

def copying_archives():
    archive = input("Digite o nome do arquivo que deseja copiar: ")
    copy_archive = f"copy_{archive}.txt"
    my_file = open(f"{archive}.txt","r")
    my_copy_file = open(copy_archive,"w")
    content = my_file.read()
    my_copy_file.write(content)
    my_copy_file = open(copy_archive,"r")
   
    print(my_copy_file.read())
    
    
    
    my_file.close()
    my_copy_file.close()
    
def main():
    copying_archives()
    
main()


#4. Faça uma função que leia um arquivo texto contendo uma lista de endereços IP
#e gere dois outros arquivos, um contendo os endereços IP válidos e outro contendo
#os endereços inválidos. O formato de um endereço IP é num1.num.num.num, onde
#num1 vai de 1 a 255 e num vai de 0 a 255.

def verify_ips():
    ips_file = open("ips.txt","r")
    valid_ips = []
    invalid_ips = []
    
    for ip in ips_file:
        try:
            nums = ip.split(".")
            if len(nums) != 4:
                return False
    
            for index, num in enumerate(nums):
                if index == 0:
                    assert int(index) >= 1 and int(index) <= 255
                else:
                    assert int(index) >= 0 and int(index) <= 255
        
            return True
            
        except BaseException:
            return False
        
        if is_valid == True:
            valid_ips.append(ip)
        else:
            invalid_ips.append(ip)
        
    valid_ips_file = open("valid_ips.txt","w")
    invalid_ips_file = open("invalid_ips.txt","w")
    valid_ips_file.writelines(valid_ips).rstrip('\n')
    invalid_ips_file.writelines(invalid_ips).rstrip('\n')
    valid_ips_file.close()
    invalid_ips_file.close()
    
    print("Validos: ", is_valid)
    print("Invalidos: ", invalid_ips)

def main():
    verify_ips()
    
main()




#5. Crie um programa que lê um arquivo de texto e escreve suas linhas de trás para
#frente. Ou seja, a última linha do arquivo original será a primeira linha no novo
#arquivo, e assim por diante.    

def reversing_archives(reversed_file_list):
    archive = input("Digite o nome do arquivo: ")
    
    my_file = open(f"{archive}.txt","r")
    
    content = my_file.read()
    
    split_content = content.split()
    
    for x in range(len(split_content)):
        reversed_file_list.append(split_content[-1-x])
    
    print(reversed_file_list)
    
    my_file.close()
        
    
def main():
    reversed_file_list = []
    reversing_archives(reversed_file_list)
    
main()

#6. Faça um programa contendo uma função que recebe como argumentos os
#nomes de dois arquivos. O primeiro arquivo contém nomes de alunos e o segundo
#arquivo contém as notas dos alunos. No primeiro arquivo, cada linha corresponde
#ao nome de um aluno e no segundo arquivo, cada linha corresponde às notas dos
#alunos (uma ou mais). Assuma que as notas foram armazenadas como strings, e
#estão separadas umas das outras por espaços em branco. Leia os dois arquivos e
#gere um terceiro arquivo que contém o nome do aluno seguido da média de suas notas.

    
    def opening_archives(names,grades,dic):
    names_file = open(f"{names}.txt","r")
    grades_file = open(f"{grades}.txt","r")
    names_grades_file = open("studentsgrades.txt","w")
    
    
    names_content = names_file.readline()
    grades_content = grades_file.readline()
    
    while names_content and grades_content != "":
        
        names_content = names_file.readline()
        grades_content = grades_file.readline()
    
        names_grades_file.write(names_content)
        names_grades_file.write(grades_content)
        
        dic[names_content] = grades_content
    
    names_grades_file = open("studentsgrades.txt","r")
    
    print(names_grades_file.read())
    print(dic)


def main():
    names = input("Digite o nome do arquivo que contém os nomes dos alunos: ")
    grades = input("Digite o nome do arquivo que contém as notas dos alunos: ")
    dic = {}
    opening_archives(names,grades,dic)
    
main()
