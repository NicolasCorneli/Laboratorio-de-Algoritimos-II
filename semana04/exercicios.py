#1
def d():
    dicionario = {}
    dicionario["name"] = input("digite seu nome: ")
    dicionario["age"] = int(input("digite sua idade: "))
    dicionario["gender"] = input("digite seu genero: ")
    dicionario["city"] = input("digite sua cidade: ")
    dicionario["state"] = input("digite seu estado: ")
    print(dicionario["name"])
    return dicionario
def main():
    dicionario = d()
    print(dicionario)
main()
#2
buy_list = {}
leave = "yes"
while leave != "no":
    product_name = input("Digite o nome do produto: ")
    quantity = int(input("Digite a quantidade: "))
    
    if product_name in buy_list:
        buy_list[product_name] = buy_list[product_name] + quantity
    else:
        buy_list[product_name] = quantity
    print(buy_list)
    leave = input("Continuar comprando? :")
print()
