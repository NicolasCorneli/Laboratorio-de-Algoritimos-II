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

#2. Crie uma função que receba uma frase e retorne em um objeto as letras com a quantidade de vezes com que elaestá presente na frase. Exemplo: ‘Joao’ => { ‘j’: 1,‘o’: 2,‘a’: 1 }

def count_numbers(my_word):
    count_dict = {}
    for word in my_word:
        for letter in word:
            
            if letter in count_dict:
                count_dict[word] = count_dict[word] + 1
            else:
                count_dict[word] = 1
            
    return count_dict
    
    
def main():
    my_word = "aabbcb"
    result = count_numbers(my_word)
    
    print(result)
    
    
main()
#3. Faça um programa que leia nomes de alunos e suas respectivas notas até que o nome ’oooo’ seja informado, após
#o fim da leitura, imprima o nome do aluno que possui a maior nota. Obs.: Use dicionário para resolver essa questão.
def a(dic):
    x = "a"
    while x != "OOOO":
        x = input("Digite seu nome:").upper()
        if x == "OOOO":
            break
        y = float(input("Digite sua nota:"))
        dic[x] = y
    return dic
def fmore(dic):
    more = 0
    y = 0
    z = 0
    for x in dic:
        y = y + 1 
        if more < dic[x]:
            z = z + 1
            more = dic[x]
    y = y - z
    name = list(dic.items())[y][0]
    print("O aluno",name,"teve a maior nota")

def main():
    dic = {}
    dic = a(dic)
    fmore(dic)
main()
#AGENDA
#Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou
#mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:
#createContact – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber
#como argumentos o nome e os telefones.
#includePhone– essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista
#na agenda, você deve perguntar se a pessoa deseja incluí-lo. Caso a resposta seja afirmativa, use a função
#anterior para incluir o novo nome.
#deletePhone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas
#um telefone, ela deve ser excluída da agenda.
#deleteContact – essa função exclui uma pessoa da agenda.
#getPhones – essa função retorna os telefones de uma pessoa na agenda.


