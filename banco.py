import time

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

def data_e_hora(operacao, valor):
    return (f'{time.strftime("%a, %d %m(%b) %y, %H : %M", time.localtime())} -- {operacao} - R${valor}')

def deposito(valor, extrato, /):
    extrato += [data_e_hora('Depósito', valor)]
    return valor, extrato
            
def saque(*, valor, extrato, conta, limite_saque, limite_max_saque):
    global limite_saque_atual
    
    if valor > conta:
        print("Você não tem saldo suficiente. O saque não será efetuado")
        raise KeyError
     
    elif limite_saque >= limite_max_saque:
        print ("Você atingiu o limite diário máximo de saques. O saque não será efetuado")
        raise KeyError 
    
    elif valor > 500:
        print("O limite máximo de saque é de R$500,00. O saque não será efetuado")
        raise KeyError 
    
    limite_saque_atual += 1
    extrato += [data_e_hora('Saque', valor)]
    return (valor * -1), extrato
        
def extrato(saldo, /, *, extrato):
    for item in extrato:
        print (item, sep='\n')
    print(f'Saldo Atual: R${saldo:.2f}')
        

while True:
    escolha = int(input(menu))
    
    if escolha == 1:
        try:
            valor_deposito, lista_extrato = deposito(
            float(input(
                "Qual o valor do depósito? ->").replace(',', '.'))
            , lista_extrato)
            saldo_conta += valor_deposito
        except ValueError:
            print("Digite apenas números e [,] ou [.] Tente novamente")
            continue
        
    elif escolha == 2:
        try:
            valor_saque, lista_extrato = saque(valor= float(input(
                "Qual o valor do saque? ->".replace(',', '.')))
            , extrato= lista_extrato, conta = saldo_conta, limite_saque = limite_saque_atual, limite_max_saque = LIMITE_SAQUE)
            saldo_conta += valor_saque

        except ValueError:
            print("Digite apenas números e [,] ou [.] Tente novamente")
            continue
        except:
            continue
        
    elif escolha == 3:
        extrato(saldo_conta, extrato=lista_extrato)
       
    elif escolha == 4:
        print ("SAINDO...")
        break

    else:
        print('Por favor, digite um valor válido. Tente novamente')