#Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar

def impar_ou_par():
    num = int(input('insira o numero para descobrir se ele e impar ou par: '))
    
    if num %2  == 0:
        print(f"O numero {num} é par")
    else:
        print(f"O numero {num} é impar")
        
impar_ou_par()