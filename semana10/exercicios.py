#1. Crie um programa que receba através de input dois números e retorne sua divisão.
def division(val1,val2):
    try:
        return val1/val2
    except ZeroDivisionError:
        print("[ERRO] Você não pode dividir um número por zero!")
        raise
    except BaseException as error:
        print(f"[ERRO] Ocorreu um erro: {error}")
        
def input_int(message):
    while True:
        try:
            value = int(input(message))
            
            return value
        except ValueError:
            print("[ERRO] O número digitado é inválido!")
        except BaseException as error:
            print(f"[ERRO] Ocorreu um erro: {error}")


def main():
    try:
        
        number_one = input_int("Digite o primeiro valor: ")
        number_two = input_int("Digite o segundo valor: ")
    
        result = division(number_one,number_two)
    
        print(f"resultado:{result}")
    
    except ValueError:
        print("[ERRO] Número informado inválido!")
    except BaseException as error:
        print(f"[ERRO] Ocorreu um erro: {error}")
        
main()

#2. Crie um programa que receba através de um input o valor numérico de um mês e retorne seu valor escrito. Lembre
#de tratar as exceções do seu programa. Exemplo: 1 -> Janeiro, 12 -> Dezembro








#3. Crie uma função que recebe um ano através de um input e defina se o mesmo é bissexto ou não. Utilize as seguintes
#regras: Um ano bissexto é divisível por 4, mas não por 100, ou então se é divisível por 400. Exemplo: 1988 é bissexto pois
#é divisível por 4 e não é por 100; 2000 é bissexto porque é divisível por 400.
def year():
    while True:
        try:
            leap_year = int(input("Digite um ano: "))
            if leap_year % 4 == 0 and leap_year % 100 != 0:
                print("Esse ano é bissexto")
            else:
                print("Esse ano não é bissexto")
        except ValueError:
            print("[ERRO] Digite um valor válido!")
        except BaseException as error:
            print(f"[ERRO] Ocorreu um erro: {error}")

def main():
    year()
    
main()


#4. O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos. Faça
#o programa que lê o valor de N e M e informa o número de combinações possíveis.


