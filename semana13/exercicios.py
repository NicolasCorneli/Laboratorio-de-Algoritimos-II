#4. Crie uma função chamada find_element que aceita uma lista e um índice como
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
        
#3. Escreva uma função calculate_square_root que aceite um número como entrada e
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
    
