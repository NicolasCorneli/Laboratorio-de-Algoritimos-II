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

