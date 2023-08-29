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
