produto = -1
contador = 1
soma = []
valor = 0
troco = 0
resposta = ""
while True:
    resposta = input("Quer fazer uma nova compra? S/N")
    if resposta == "N":
        break
    if resposta == "S":
        while produto != 0:
            produto = float(input("Digite o valor do produto{}:".format(contador)))
            soma.append(produto)
            contador += 1
            print("Produto{}: {}".format(contador,produto))
        total = sum(soma)
        print("Total: {}".format(total))   
        valor = float(input("Qual foi o valor pago ao caixa? "))
        if valor < total:
            print("Faltou dinheiro! Refaça as suas contas!")
            break
    
    troco = valor - total
    print("Total: {}".format(total))
    print("Dinheiro: {}".format(valor))
    print("O troco é: {}".format(troco))
        