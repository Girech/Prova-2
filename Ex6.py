roberto = 0
jose = 0
jessica = 0
lara = 0
nulo = 0
branco = 0
voto = -1
while voto != 0:
    voto = int(input("Escolha seu candidato(a), 1-Roberto 2-José 3-Jéssica 4-Lara 5-Nulo 6-Branco 0-Finalizar: "))
    if voto == 0:
        print("Finalizando!")
        print("Roberto recebeu, {} votos!".format(roberto))
        print("José recebeu, {} votos!".format(jose))
        print("Jéssica recebeu, {} votos!".format(jessica))
        print("Lara recebeu, {} votos!".format(lara))
        print("Houveram {} votos nulos.".format(nulo))
        print("Houveram {} votos em branco.".format(branco))
        break
    elif voto == 1:
        roberto += 1
    elif voto == 2:
        jose += 1
    elif voto == 3:
        jessica += 1
    elif voto == 4:
        lara += 1
    
