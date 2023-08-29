#BINGO

import random

def numero():
    bingo = []
    usedvalues = []
    
    for line in range(5):
        bingo.append([])
        
        for coluna in range(5):
            num = random.randint(0,99)
            
            while num in usedvalues:
                num = random.randint(0,99)
            if num not in usedvalues:
                bingo[line].append(num)
                usedvalues.append(num)
    return bingo
    
def main():
    bingo = numero()
    print(bingo)
main()

#2. Escreva um programa que calcule e imprima a soma de todos os elementos abaixo da diagonal principal de uma matriz.
















#3. Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico.
c100 = 0
c50 = 0
c20 = 0
c10 = 0

value = int(input("Digite um valor: "))

if value %10 != 0:
    print("Digite outro valor")

while value != 0:
    if value >= 100:
        value = value - 100
        c100 = c100 + 1
    elif value >= 50:
        value = value - 50
        c50 = c50 + 1
    elif value >= 20:
        value = value - 20
        c20 = c20 + 1
    elif value >= 10:
        value = value - 10
        c10 = c10 + 1
print("A quantidade de notas de 100 é:",c100,"de 50 é:",c50,"de 20 é:",c20,"de 10 é:",c10)

#4. Dado uma matriz de números inteiros positivos de dimensões n x n, onde n >= 5, encontre o maior produto de uma seqüência de 5 números consecutivos (a seqüência pode estar na vertical, na horizontal ou na diagonal principal).


