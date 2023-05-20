def dimensoesObjeto():
    while True:
        # Criei a função "Try" para caso acontece um erro de digitação, por parte do usuário
        try:
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            altura = float(input("Digtie a altura do objeto (em cm): "))
            # Cálculo total dos pedidos
            volume = comprimento * largura * altura
            print(f"O valor do objeto é (em cm³): {volume}")
            if volume < 1000:
                return 10
            elif 1000 >= volume < 10000:
                return 20
            elif 10000 >= volume < 30000:
                return 30
            elif 30000 >= volume < 100000:
                return 50
            else:
                print("Não aceitamos objetos com dimensões tão grandes")
                print("Entre com as dimensões novamente")
            # Caso o usuário digite um valor superior à 100000, não é aceito e pede novamente ás informações do pedido
                continue
            # Se o usuário digitar um caractere, imprime a imagem abaixo informando que foi informado uma dimensão não numérico
        except ValueError:
            print("Você digitou alguma dimensão do objeto não numérico")
            print("Por favor entre com as dimensões desejados novamente")


def pesoObjeto():
    while True:
        # Criei a função "Try" para caso acontece um erro de digitação, por parte do usuário
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            if peso == 0.1:
                return 1
            elif 0.1 >= peso < 1:
                return 1.5
            elif 1 >= peso < 10:
                return 2
            elif 10 >= peso < 30:
                return 3
            else:
                print("Não aceitamos objetos tão pesados")
                print("Entre com o peso desejado novamente")
            # Caso o usuário digite um valor superior à 30, não é aceito e pede novamente ás informações do pedido
                continue
        # Se o usuário digitar um caractere, imprime a imagem abaixo informando que foi informado uma dimensão não numérico
        except ValueError:
            print("Você digitou peso do objeto com valor não numérico")
            print("Por favor entre com o peso desejado novamente")


def rotasObjeto():
    while True:
        rota = input("Selecione a rota\n"
                     "BR - De Brasília para Rio de Janeiro\n"
                     "BS - De Brasília para São Paulo\n"
                     "RB - De Rio de Janeiro para Brasília\n"
                     "RS - De Rio de Janeiro para São Paulo\n"
                     "SR - De São Paulo para Rio de Janeiro\n"
                     "SB - De São Paulo para Brasília\n"
                     " ")
        if rota == "RS":
            return 1
        elif rota == "SR":
            return 1
        elif rota == "BS":
            return 1.2
        elif rota == "SB":
            return 1.2
        elif rota == "BR":
            return 1.5
        elif rota == "RB":
            return 1.5
        # Se o usuário digitar uma rota diferente das mencionadas, imprime ás mensagens abaixo
        else:
            print("Você digitou uma rota que não existe")
            print("Por favor entre com a rota desejada novamente")
        # Função "continue" é para retornar ao "while True", e assim poder informar ás rotas novamente, de forma correta
            continue


print("Bem Vindo a Companhia de Logística Lucas Lima de Ávila")
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rotas = rotasObjeto()
# Criei a variável "total" para realizar à soma das dimensões, peso e rotas
total = dimensoes * peso * rotas
print(f"Total a pagar (R$): {total:.2f} (dimensões: {dimensoes} * peso: {peso} * rotas: {rotas})")
