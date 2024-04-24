def menu():
    try:
        print("1- Depositar dinheiro") 
        print("2- Sacar dinheiro") 
        print("3- Verificar saldo bancário") 
        print("4- Histórico de movimentações") 
        print("5- Sair")
        opc = int(input("Digite a opção desejada: "))
        return opc
    except ValueError:
        print("Você não digitou um valor válido")
    except TypeError:
        print("Digite um valor válido")
    except BaseException as error:
        print(f"Ocorreu um erro: {error}")
    
def deposition(bank_account):
    try:
        deposit = float(input("Digite o quanto deseja depositar: "))
        if deposit <= 0:
            print("Deposite um valor válido")
        else:
            bank_account["balance"] = bank_account["balance"] + deposit
            bank_account["historic"].append(draw_out)
            print("Valor depositado com sucesso")
        return bank_account
    except ValueError:
        print("Você não digitou um valor válido")
    except TypeError:
        print("Digite um valor válido")
    except BaseException as error:
        print(f"Ocorreu um erro: {error}")

def withdraw(bank_account):
    try:
        draw_out = float(input("Digite o quanto deseja sacar: "))
        if draw_out > bank_account["transaction_limit"]:
            print("Digite um valor abaixo de",bank_account["transaction_limit"])
        elif draw_out <= 0:
            print("Digite um valor válido para sacar")
        else:
            bank_account["balance"] = bank_account["balance"] - draw_out
            bank_account["historic"].append(-draw_out)
            print("Valor retirado com sucesso")
        return bank_account
    except ValueError:
        print("Você não digitou um valor válido")
    except TypeError:
        print("Digite um valor válido")
    except BaseException as error:
        print(f"Ocorreu um erro: {error}")    

def view_current_balance(bank_account):
    print("Seu saldo atual é: ",bank_account["balance"])

def view_historic(bank_account):
    print("Seu histórico de movimentações é: ", bank_account["historic"])
    
    
def main():
    bank_account = {"balance": 0,"transaction_limit": 1000,"historic":[] }
    while True:
        opc = menu()
        if opc == 1:
            bank_account = deposition(bank_account)
        elif opc == 2:
            bank_account = withdraw(bank_account)
        elif opc == 3:
            view_current_balance(bank_account)
        elif opc == 4:
            view_historic(bank_account)
        elif opc == 5:
            print("Até mais!")
            break
main()
