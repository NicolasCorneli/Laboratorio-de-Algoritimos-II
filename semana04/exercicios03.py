#1.Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da camisa que está
#usando como valor. Após, imprima o resultado de forma amigável.

def dictionary(dic):
    dic["João"] = "Roxo"
    dic["Igor"] = "Branco"
    dic["Jonathan"] = "Preto"
    dic["Bruno"] = "Verde"
    dic["Nicolas"] = "Preto"
    return dic
def answer(dic):
    print("A cor de camisa que João está usando é:",dic["João"])
    print("A cor de camisa que Igor está usando é:",dic["Igor"])
    print("A cor de camisa que Jonathan está usando é:",dic["Jonathan"])
    print("A cor de camisa que Bruno está usando é:",dic["Bruno"])
    print("A cor de camisa que Nicolas está usando é:",dic["Nicolas"])
    
def main():
    dic = {}
    dic = dictionary(dic)
    answer(dic)
    
main()

#2.Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo como seu valor
#uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?). Após,
#imprima o resultado de forma amigável.

def dictionary(dic):
    dic["Segunda"] = ["Foil"]
    dic["Terça"] = ["Laboratório de Algoritimos II"]
    dic["Quarta"] = []
    dic["Quinta"] = ["Probabilidade e Estatística"]
    dic["Sexta"] = ["Fundamentos de economia e administração"]
    dic["Sábado"] = ["Organização e Arquitetura de Computadores"]
    dic["Domingo"] = []
    return dic
def answers(dic):
    print("Segunda-feira, hoje é dia de",dic["Segunda"])
    print("Terça-feira,hoje temos",dic["Terça"])
    print("Quarta-feira",dic["Quarta"])
    print("Quinta-feira, dia de",dic["Quinta"])
    print("Sexta-feira, aulinha de",dic["Sexta"])
    print("Sábado, começando o dia com",dic["Sábado"])
    print("Finalmente Domingo...",dic["Domingo"])

def main():
    dic = {}
    dic = dictionary(dic)
    answers(dic)
main()
