nome1 = input("Digite o nome do produto 1: ")
preço1 = float(input("Digite o preço do produto 1: "))
nome2 = input("Digite o nome do produto 2: ")
preço2 = float(input("Digite o preço do produto 2: "))
nome3 = input("Digite o nome do produto 3: ")
preço3 = float(input("Digite o preço do produto 3: "))
produtos = {nome1 : preço1, nome2 : preço2, nome3 : preço3}
while True:
    print("Tabela de preços",produtos)
    qtd1 = int(input("Quantas unidades de {} vão ser compradas: ".format(nome1)))
    qtd2 = int(input("Quantas unidades de {} vão ser compradas: ".format(nome2)))
    qtd3 = int(input("Quantas unidades de {} vão ser compradas: ".format(nome3)))
    total1 = preço1 * qtd1
    total2 = preço2 * qtd2
    total3 = preço3 * qtd3
    valorfinal = total1+total2+total3
    print("O valor a ser pago é: {}".format(valorfinal))

    valorpago = float(input("Quanto foi o valor pago ao caixa?"))
    if valorpago < valorfinal:
        print("Faltou dinheiro! Refaça as suas contas!")
        break
    troco = valorpago - (total1 + total2 + total3) 

    print("Lojas Giordano:")
    print("Total de {}: R${}".format(nome1,total1))
    print("Total de {}: R${}".format(nome2,total2))
    print("Total de {}: R${}".format(nome3,total3))
    print("Total: R${}".format(valorfinal))
    print("Dinheiro do cliente: R${}".format(valorpago))
    print("Troco: R${}".format(troco))

