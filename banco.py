import time

def data_e_hora(operacao, valor):
    return (f'{time.strftime("%a, %d %m(%b) %y, %H : %M", time.localtime())} -- {operacao} - R${valor}')

def deposito():
    while True:
            valor_deposito = input("Digite o valor a ser depositado: ")
            valor_deposito = valor_deposito.replace(',', '.')

            try:
                valor_deposito = float(valor_deposito)
                saldo_conta += valor_deposito
                lista_extrato += [data_e_hora('Depósito', valor_deposito)]
                break
            
            except ValueError:
                print("Digite apenas números e [,] ou [.] Tente novamente")
                continue

def saque():
    while True:
        valor_saque = input('Digite o valor que será sacado: ')
        valor_saque = valor_saque.replace(',', '.')

        try:
            valor_saque = float(valor_saque)

            if valor_saque > saldo_conta:
                print("Você não tem saldo suficiente. O saque não será efetuado")
                break

            elif limite_saque_atual >= LIMITE_SAQUE:
                print("Você atingiu o limite diário máximo de saques. O saque não será efetuado")
            
            elif valor_saque > 500:
                print("O limite máximo de saque é de R$500,00. O saque não será efetuado")

            saldo_conta += (valor_saque * -1)
            lista_extrato += [data_e_hora('Saque', valor_saque)]
            limite_saque_atual += 1
            break

        except ValueError:
            print("Digite apenas números e [,] ou [.] Tente novamente")
            continue
        
def extrato():
    for item in lista_extrato:
        print (item, sep='\n')
    print(f'Saldo Atual: R${saldo_conta:.2f}')
        
saldo_conta = 0.00
lista_extrato = []
limite_saque_atual = 0
LIMITE_SAQUE = 3

menu = '''
Digite [1] para DEPÓSITO
Digite [2] para SAQUE
Digite [3] para EXTRATO
Digite [4] para SAIR

==> '''
while True:
    escolha = int(input(menu))

    if escolha == 1:
        deposito()
        
    elif escolha == 2:
        saque()   
         

    elif escolha == 3:
        extrato()
       
    elif escolha == 4:
        print ("SAINDO...")
        break

    else:
        print('Por favor, digite um valor válido. Tente novamente')