from datetime import datetime
import random

# Função para salvar os dados em um arquivo
def salvar_dados():
    with open("dados_usuario.txt", "w") as arquivo:
        arquivo.write(f"{nome}\n")
        arquivo.write(f"{usuario}\n")
        arquivo.write(f"{senha}\n")
        arquivo.write(f"{reais}\n")
        arquivo.write(f"{bitcoin}\n")
        arquivo.write(f"{ethereum}\n")
        arquivo.write(f"{ripple}\n")

# Função para carregar os dados de um arquivo
def carregar_dados():
    global nome, usuario, senha, reais, bitcoin, ethereum, ripple
    try:
        with open("dados_usuario.txt", "r") as arquivo:
            nome = arquivo.readline().strip()
            usuario = arquivo.readline().strip()
            senha = arquivo.readline().strip()
            reais = float(arquivo.readline().strip())
            bitcoin = float(arquivo.readline().strip())
            ethereum = float(arquivo.readline().strip())
            ripple = float(arquivo.readline().strip())
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Utilizando valores padrão.")

carregar_dados()


nome = "Leonardo Silva"
usuario = '10645497877'
senha = '041205'
valor_bitcoin = 324970.14
valor_ethereum = 15217.81
valor_ripple = 2.61
taxa_bitcoin_compra = 0.02
taxa_ethereum_compra = 0.01
taxa_ripple_compra = 0.01
taxa_bitcoin_venda = 0.03
taxa_ethereum_venda = 0.02
taxa_ripple_venda = 0.01
transacoes = []




def consulta_saldo():
    while True:
        verifica = input('Digite sua senha de login: ')
        if senha == verifica:
            print("Permissão concedida")
            break
        else:
            print("Senha incorreta")
    print("Você está consultando seu saldo")

    print(f"Nome: {nome}")
    print(f"CPF: {usuario}", "\n" )
    print(f'Reais: {reais}')
    print(f'Bitcoin: {bitcoin}')
    print(f'Ethereum: {ethereum}')
    print(f'Ripple: {ripple}')
    consulta_1()

def consulta_extrato():
    global reais, bitcoin, ethereum, ripple, transacoes
    if 'reais' not in globals():
        reais = 0
        
    if 'bitcoin' not in globals():
        bitcoin = 0
        
    if 'ethereum' not in globals():
        ethereum = 0
        
    if 'ripple' not in globals():
        ripple = 0
        
    print("Você está consultando seu extrato")
    print("Nome:", nome)
    print("CPF:", usuario)
    for transacao in transacoes:
        data_hora, tipo, valor, moeda, cotacao, taxa, reais, bitcoin, ethereum, ripple = transacao
        print(data_hora.strftime("%d-%m-%Y %H:%M"), tipo, valor, moeda, "CT: ", cotacao, "TX:" ,taxa , "REAL:", "{:.2f}".format(reais), "BTC: ", "{:.2f}".format(bitcoin), "ETH:", "{:.3f}".format(ethereum), "XRP:", "{:.1f}".format(ripple))
    consulta_1()

def depositar():
    global reais
    if 'reais' not in globals():
        reais = 0
    
    print("Você está no Depósito")
    deposito = float(input("Qual o valor que você deseja depositar: "))
    if deposito <= 0:
        print("Deposite um valor válido")
    else: 
        reais += deposito
        print("Depósito realizado com sucesso")
        print(f"Seu saldo é de R$: {reais}")
        transacoes.append((datetime.now(), '+', deposito, "REAL", 0, 0, reais, bitcoin, ethereum, ripple))
    consulta_1()

def saque():
    global reais
    if 'reais' not in globals():
        reais = 0
    print("Você está no Saque")
    saque = float(input("Digite o valor que você deseja sacar: "))
    if saque <= 0:
        print("Saque inválido")
    else:
        reais -= saque
        print("Saque foi realizado com sucesso")
        print(f"Você está com R$: {reais}")
        transacoes.append((datetime.now(), '-', saque, "REAL", 0, 0, reais, bitcoin, ethereum, ripple))
    consulta_1()

def compra_cript():
    global reais
    if 'reais' not in globals():
        reais = 0
        
    global bitcoin
    if 'bitcoin' not in globals():
        bitcoin = 0
        
    global ethereum
    if 'ethereum' not in globals():
        ethereum = 0
        
    global ripple
    if 'ripple' not in globals():
        ripple = 0
        
    while True:
        verifica = input('Digite sua senha de login: ')
        if senha == verifica:
            print("Permissão concedida")
            break
        else:
            print("Senha incorreta")
    
    print("Você está em Compras de Criptomoedas")
    print("1. Bitcoin")
    print("2. Ethereum")
    print("3. Ripple")
    direcionamento_compra_cript = int(input("Digite o número da criptomoeda que deseja comprar: "))

    valor_compra_cript = float(input("Digite o valor em reais do valor em que deseja adquirir: "))
    
    if direcionamento_compra_cript == 1:
        if valor_compra_cript <= reais:
            valor_compra_cript * 0.02
            bitcoin = valor_compra_cript / valor_bitcoin
            reais -= valor_compra_cript
            print(f'Quantidade de Bitcoin comprada foi de: {bitcoin}')
            transacoes.append((datetime.now(), '+', valor_compra_cript, "BTC", valor_bitcoin, taxa_bitcoin_compra, reais, bitcoin, ethereum, ripple))
        else:
            print("Ação inválida")
        
    elif direcionamento_compra_cript == 2:
        if valor_compra_cript <= reais:
            valor_compra_cript * 0.01
            ethereum = valor_compra_cript / valor_ethereum
            reais -= valor_compra_cript
            print(f'Quantidade de Ethereum comprada foi de: {ethereum}')
            transacoes.append((datetime.now(), '+', valor_compra_cript, "ETH", valor_ethereum, taxa_ethereum_compra, reais, bitcoin, ethereum, ripple))
        else:
            print("Ação inválida")
        
    elif direcionamento_compra_cript == 3:
        if valor_compra_cript <= reais:
            valor_compra_cript * 0.01
            ripple = valor_compra_cript / valor_ripple
            reais -= valor_compra_cript
            print(f'Quantidade de Ripple comprada foi de: {ripple}')
            transacoes.append((datetime.now(), '+', valor_compra_cript, "XRP", valor_ripple, taxa_ripple_compra, reais, bitcoin, ethereum, ripple))
        else:
            print("Ação inválida")
    
    consulta_1()

# ------------------------------------------------------------------------------------- #

def venda_cript():
    global reais
    if 'reais' not in globals():
        reais = 0
        
    global bitcoin
    if 'bitcoin' not in globals():
        bitcoin = 0
        
    global ethereum
    if 'ethereum' not in globals():
        ethereum = 0
        
    global ripple
    if 'ripple' not in globals():
        ripple = 0
        
    while True:
        verifica = input('Digite sua senha de login: ')
        if senha == verifica:
            print("Permissão concedida")
            break
        else:
            print("Senha incorreta")
    
    print("Você está em Vendas de Criptomoedas")
    print("1. Bitcoin")
    print("2. Ethereum")
    print("3. Ripple")
    direcionamento_venda_cript = int(input("Digite o número da criptomoeda que deseja vender: "))

    valor_venda_cript = float(input("Digite o valor em criptomoedas em que deseja vender: "))
    
    
    if direcionamento_venda_cript == 1:
        if valor_venda_cript <= bitcoin:
            valor_venda_cript * 0.03
            reais = valor_venda_cript * valor_bitcoin
            bitcoin -= valor_venda_cript
            print(f'Quantidade de Bitcoin vendida foi de: {bitcoin}')
            transacoes.append((datetime.now(), '-', valor_venda_cript, "BTC", valor_bitcoin, taxa_bitcoin_venda, reais, bitcoin, ethereum, ripple))
        else:
            print("Valor inválido")
        
    
    if direcionamento_venda_cript == 2:
        if valor_venda_cript <= ethereum:
            valor_venda_cript * 0.02
            reais = valor_venda_cript * valor_ethereum
            ethereum -= valor_venda_cript
            print(f'Quantidade de Ethereum vendida foi de: {ethereum}')
            transacoes.append((datetime.now(), '-', valor_venda_cript, "ETH", valor_ethereum, taxa_ethereum_venda, reais, bitcoin, ethereum, ripple))
        else:
            print("Valor inválido")
        
    
    if direcionamento_venda_cript == 3:
        if valor_venda_cript <= ripple:
            valor_venda_cript * 0.01
            reais = valor_venda_cript * valor_ripple
            ripple -= valor_venda_cript
            print(f'Quantidade de Ripple vendida foi de: {ripple}')
            transacoes.append((datetime.now(), '-', valor_venda_cript, "XRP", valor_ripple, taxa_ripple_venda, reais, bitcoin, ethereum, ripple))
        else:
            print("Ação inválida")
       
    consulta_1()

def nova_cotacao(valor_atual):
    variacao = random.uniform(-0.05, 0.05)  # Variação entre -5% e +5%
    return valor_atual * (1 + variacao)

def att_cotacao():
    # Atualizar as cotações com variações aleatórias
    nova_cotacao_bitcoin = nova_cotacao(valor_bitcoin)
    nova_cotacao_ethereum = nova_cotacao(valor_ethereum)
    nova_cotacao_ripple = nova_cotacao(valor_ripple)

    # Exibir as novas cotações
    print("Nova cotação do Bitcoin:", round(nova_cotacao_bitcoin, 2))
    print("Nova cotação do Ethereum:", round(nova_cotacao_ethereum, 2))
    print("Nova cotação do Ripple:", round(nova_cotacao_ripple, 2))

def sair():
    print("Você saiu")

def consulta_1():
    print("1. Consultar saldo")
    print("2. Consultar extrato")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Comprar criptomoedas")
    print("6. Vender criptomoedas")
    print("7. Atualizar cotação")
    print("8. Sair")
    direcionamento = int(input('Digite o número da ação em que deseja ir: '))
    if direcionamento == 1:
        consulta_saldo()
    elif direcionamento == 2:
        consulta_extrato()
    elif direcionamento == 3:
        depositar()
    elif direcionamento == 4:
        saque()
    elif direcionamento == 5:
        compra_cript()
    elif direcionamento == 6:
        venda_cript()
    elif direcionamento == 7:
        att_cotacao()
    elif direcionamento == 8:
        sair()
    elif direcionamento >= 9:
        print("Número inválido")

carregar_dados()

while True:
    login = input('Digite seu login: ')
    password = input('Digite sua senha: ')

    if login == usuario and senha == password:
        print('Seja Bem-Vindo')
        break
    elif login != usuario:
        print('Nome de usuário incorreto')
    else:
        print('Senha incorreta')

# Direcionamento do usuário
direcionamento = consulta_1()

# Salvar os dados antes de encerrar o programa
salvar_dados()
