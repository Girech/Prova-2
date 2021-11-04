escolha = ""
contidade = 0
contsono = 0
contpeso = 0
while escolha != "S":
    escolha = input("O que deseja fazer, C-Cadastrar S-Sair: ")
    if escolha == "S":
        print("Saindo!")
        break
    elif escolha != "C" and escolha != "S":
        print("Digite um valor válido")
        break
    else:
        idade = int(input("Digite a sua idade: "))
        if idade < 16 or idade > 69:
            contidade = contidade + 1
        sono = float(input("Quanto tempo de sono você teve nas ultimas 24hrs? "))
        if sono < 6:
            contsono = contsono + 1
        peso = float(input("Digite o seu peso:"))
        if peso < 50:
            contpeso = contpeso + 1
        if contidade > 0:
            print("Você nao pode doar sangue, pois sua idade nao condiz com a faixa de idades permitidas")
        if contpeso > 0:
            print("Você nao pode doar sangue, pois seu peso é menor que 50kg")    
        if contsono > 0:
            print("Você nao pode doar sangue, pois você dormiu menos que 6hrs nas últimas 24hrs")
        if contidade == 0 and contpeso == 0 and contsono == 0:
            print("Doador Aprovado!")

       
