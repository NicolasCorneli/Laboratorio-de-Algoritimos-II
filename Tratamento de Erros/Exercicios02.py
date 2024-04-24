#1. Crie uma função chamada find_element que aceita uma lista e um índice como
#entrada e retorna o elemento na posição do índice fornecido. Se o índice estiver fora
#dos limites da lista, lance uma exceção IndexError com uma mensagem indicando
#que o índice é inválido.

def find_element(greek_alphabet):
    try:
        number = int(input("Digite um número de 0 a 23: "))
        if number < 0 or number > 23:
            raise IndexError
        print(greek_alphabet[number])
    except IndexError:
        print(f"O indice {number} é inválido")
    except BaseException as error:
        print(f"[ERRO] Ocorreu um erro {error}")    
      
def main():
    greek_alphabet = ["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Tetha","Iota","Kappa","Lamba","Mu","Nu","Xi","Omicron","Pi","Rho","Sigma","Tau","Upsilon","Phi","Chi","Psi","Omega"]
    find_element(greek_alphabet)

main()
        
#2. Escreva uma função calculate_square_root que aceite um número como entrada e
#retorne a raiz quadrada desse número. Se o número for negativo, lance uma exceção
#personalizada chamada NegativeNumberError com uma mensagem indicando que a
#raiz quadrada de números negativos não é real. Para calcular a raiz utilize o operador
#de exponenciação **. Exemplo: raiz = 81 ** (1/2)

class NegativeNumberError(BaseException):
    pass
def calculate_square_root(number):
    try:
        if number < 0:
            raise NegativeNumberError
        else:    
            raiz = number **(1/2)
            print(raiz)
    except NegativeNumberError:
        print(f"[ERRO] A raiz quadrada de números negativos não é real")
    except BaseException as error:
        print(f"[ERRO] Ocorreu um erro: {error}")
def main():
    number = float(input("Digite um número: "))
    calculate_square_root(number)
main()
    
#3. Imagine que você está implementando um sistema para avaliação de um produto. O
#produto pode através de números inteiros de 0 até 10. Crie uma função que, ao ser
#chamada, solicite ao usuário um número inteiro e verifique através da declaração
#assert se o número está dentro do range permitido. Se não estiver, lance uma exceção
#AssertionError com uma mensagem indicando que o número está fora do intervalo
#permitido.

def zero_to_ten(number):
    try:
        assert number >= 0 and number <= 10
        print("Obrigado pela avaliação!")
    except AssertionError:
        print("[ERRO] O número está fora do intervalo (0 a 10)")
    except BaseException as error:
        print(f"[ERRO] Ocorreu um erro: {error}")
        
def main():
    number = 0
    try:
        number = int(input("De uma nota para o produto (0 a 10): "))
    except ValueError:
        print("Digite um número inteiro dentro do intervalo mencionado")

    zero_to_ten(number)
main()
