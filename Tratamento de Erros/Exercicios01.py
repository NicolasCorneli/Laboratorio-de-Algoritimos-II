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

class InvalidMonthException(BaseException):
    pass
def get_month_name(month):
    try:
        months = ("January","February","March","April","May","June","July","August","September","October","November","December")
        return months[month - 1]
    except IndexError:
        print("[ERRO] O mês acessado não existe!")
    except BaseExceptions as error:
        print(f"[ERRO] Ocorreu um erro:{error}")
        
        
def main():
    while True:
        try:
            month = int(input("Digite o mês: "))
            month_name = get_month_name(month)
        
            if month > 12 or month < 1:
                raise InvalidMonthException()
        
            print(f"Nome do mês: {month_name}")
        except ValueError:
            print("[ERRO] Você deve digitar somente números inteiros!")
        except InvalidMonthException:
            print("[ERRO] O mês informado não existe")
        except BaseExceptions as error:
            print(f"[ERRO] Ocorreu um erro:{error}")

main()


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
