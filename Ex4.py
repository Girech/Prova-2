escolha = ""
while escolha != "S":
    escolha = input("O que deseja fazer, C-Cadastrar S-Sair: ")
    if escolha == "S":
        print("Saindo!")
        break
    elif escolha != "C" and escolha != "S":
        print("Digite um valor válido")
        break
    else:
        nome = input("Digite o seu nome: ")
        if len(nome) < 3:
            print("O nome deve ter pelo menos 3 caracteres")
            break
        else:
            idade = int(input("Digite a sua idade: "))
            if idade < 18 or idade > 110:
                print("A idade deve ser entre 18 e 110 anos")
                break
            else:
                salario = float(input("Digite o seu salário: "))
                if salario < 1045:
                    print("O salário deve ser de no minimo R$1045,00")
                    break
                else:
                    sexo = input("Digite o seu sexo, F-Feminino M-Masculino: ")
                    if sexo != "F" and sexo != "M":
                        print("Digite um valor valido")
                        break
                    else:
                        estadocivil = input("Digite o seu estado civil, S-Solteiro C-Casado V-Viúvo D-Divorciado: ")
                        if estadocivil != "S" and estadocivil != "C" and estadocivil != "V" and estadocivil != "D":
                            print("Digite um valor valido")
                            break
                        else:
                            print("O usuario: {}, idade: {}, salario: {}, sexo: {}, Estado Civil: {}, foi cadastrado com sucesso!".format(nome,idade,salario,sexo,estadocivil))






