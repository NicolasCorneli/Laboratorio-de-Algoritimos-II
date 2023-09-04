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
#3.Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário
#contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes e exiba de forma amigável.

def some_movies(movies,dictionary_villains):
    dictionary_villains["1"] = "Ghost Face","1996"
    dictionary_villains["2"] = "Anton Chigurh","2007"
    dictionary_villains["3"] = "Dr.Octopus","2004"
    dictionary_villains["4"] = "Antonio Montana","1983"
    dictionary_villains["5"] = "Joker","2008"
    
    movies["Scream"] = dictionary_villains["1"] 
    movies["No country for old men"] = dictionary_villains["2"] 
    movies["Spider-Man 2"] = dictionary_villains["3"]
    movies["Scarface"] = dictionary_villains["4"] 
    movies["Batman"] = dictionary_villains["5"]
    return movies,dictionary_villains

def prints(movies,dictionary_villains):
    print(movies)

def main():
    movies = {}
    dictionary_villains = {}
    movies,dictionary_villainsvillains = some_movies(movies,dictionary_villains)
    prints(movies,dictionary_villains)

main()
#4.Escreva um programa em Python que verifique se uma chave existe ou não em um dicionário. Se a chave existir no
#dicionário, imprima Verdadeiro. Caso contrário, imprima Falso.

def dictionary(dic):
    dic["Key1"] = "1"
    dic["Key2"] = "2"
    dic["Key3"] = "3"
    return dic
    
def ifs(dic):
    if "Key1" in dic:
        print("True")
    else:
        print("False")
    
def main():
    dic = {}
    dic =  dictionary(dic)
    ifs(dic)
main()
#5.Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário,
#onde a chave é a vogal considerada.

def whatever(dic,counterA,counterE,counterI,counterU,counterO): 
    text = input("Digite o que quiser: ").upper()
    for x in text:
        for y in x:
            if y == "A":
                counterA = counterA + 1
                dic["A"] = counterA
            elif y == "E":
                counterE = counterE + 1
                dic["E"] =  counterE
            elif y == "I":
                counterI = counterI + 1
                dic["I"] =  counterI
            elif y == "U":
                counterU = counterU + 1
                dic["U"] =  counterU
            elif y == "O":
                counterO = counterO + 1
                dic["O"] =  counterO
    return dic
def main():
    dic = {}
    counterA = 0
    counterE = 0
    counterI = 0
    counterU = 0
    counterO = 0
    dic = whatever(dic,counterA,counterE,counterI,counterU,counterO)
    print("A quantide de vogais é:",(dic))
main()
