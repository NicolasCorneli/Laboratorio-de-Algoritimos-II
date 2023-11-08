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
    
    
