#Imagine que você está criando um programa para gerenciar o estoque de produtos em uma loja. Você pode usar um dicionário para rastrear os produtos, suas quantidades e preços. Deve permitir:
#Adicionar um produto: Solicite o nome do produto, quantidade em estoque e preço unitário. Armazene essas informações em um dicionário dentro do dicionário estoque. Caso o produto já exista, deve somente incrementar o estoque com a quantidade informada.
#Buscar um produto: Solicite o nome do produto e exiba as informações disponíveis, incluindo quantidade em estoque e preço unitário.
#Visualizar todos os produtos: Mostre uma lista de todos os produtos disponíveis, juntamente com suas quantidades e preços.
#Vender um produto: Solicite o nome do produto vendido e a quantidade vendida. Atualize a quantidade em estoque e calcule o valor total da venda.
#Relatório de Vendas: Mostre um relatório que liste todas as vendas realizadas, incluindo o nome do produto, a quantidade vendida e o valor total da venda.

def menu():
    print("1 - add produto")
    print("2 - buscar produto")
    print("3 - vizualisar todos os produtos")
    print("4 - vender produto")
    print("5 - relatorio de vendas")
    print("6 - sair")
    opt = int(input("digite uma opt: "))
    return opt

def add_product(my_dict):
    name_product = input("digite o nome de algum produto: ").upper()
    
    if name_product not in my_dict:
        value = float(input("digite o valor do seu produto: "))
        amount = int(input("digite quantos deseja adicionar no estoque: "))
        my_dict[name_product] = {"value": value, "amount": amount}
        print("seu produto foi adicionado com sucesso")
    else:
        print("o produto ja esta em estoque!, quantos voce gostaria de adicionar? ")
        amount = int(input("digite a quantidade que voce deseja adicionar a mais: "))
        my_dict[name_product]["amount"] = my_dict[name_product]["amount"] + amount
    return my_dict
    
def search_product(my_dict):
    name_product = input("qual produto deseja buscar: ").upper()
    
    if name_product in my_dict:
        print("produto:" , name_product)
        print("valor:" , my_dict[name_product]["value"])
        print("estoque:", my_dict[name_product]["amount"])
    else:
        print("o ", name_product, "nao foi buscado")
        
def sell_product(my_dict,my_dict2):
    sell_quantity = 0
    value_total = 0
    name_product = input("qual produto deseja vender: ").upper()
    if name_product in my_dict:
        sell = int(input("quantos produtos voce gostaria de vender?"))
        if sell <= my_dict[name_product]["amount"] :
            
            my_dict[name_product]["amount"] -= sell
            price_total = my_dict[name_product]["value"] * sell
            print("o valor total foi de:", price_total)
            
            if name_product not in my_dict2:
                my_dict2[name_product] = {"quantidade vendida": sell, "total do valor vendido": price_total}
            else:
                my_dict2[name_product]["quantidade vendida"] += sell
                my_dict2[name_product]["total do valor vendido"] += price_total
        else:
            print("esse produto esta em falta no estoque")
    else:
        print("esse produto não encontra-se no estoque!")
    return my_dict, my_dict2
    
def sales_report(my_dict,my_dict2):
    print(my_dict2)
    
def main():
    my_dict = {}
    my_dict2 = {}
    while True:
        opt = menu()
        if opt == 1:
            my_dict = add_product(my_dict)
        elif opt == 2:
            search_product(my_dict)
        elif opt == 3:
            print(my_dict)
        elif opt == 4:
            my_dict,my_dict2 = sell_product(my_dict,my_dict2)
        elif opt == 5:
            sales_report(my_dict,my_dict2)
        elif opt == 6:
            break
    
main()
