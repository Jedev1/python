cont=0
print("faça seu login e senha para se cadastrar na nossa agência de viagens blue tour")
print("obrigado pela preferência")
while True:
    login=str(input("Digite o login: "))
    senha=str(input("Digite a senha: "))
    if(login=="admin"and senha=="admin"):
        print("pode proseguir")
        break
    else:
        print("Login ou senha errado ")
        cont=cont+1
        if(cont==3):
            break



def cadeira():
    classe1 = ["livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre"]
    classe2 = ["livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre"]
    executiva = ["livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre","livre"]
    opcao = 0
    c = 0
    i=0
    opcao_poltrona=0
    disponivel = 0
    opcao_local=0
   
    # Criando menu
   

    while True:
        print("#"*37)
        print("\U0001F603""menu para planejamento de assentos""\U0001F603")
        print("$"*37)
        print("1 - Escolha o assento")
        print("2 - Vistoria geral dos assentos")
        print("3 - sair")
        op = int(input("o que deseja fazer?"))
    # Operação com as opções janela e corredor
        if op == 1:
            opcao_local = str(input("[c] para primeira classe ou [o] para segunda classe e [a] para classe executiva:"))
            if opcao_local == "c":
                opcao_poltrona = int(input("escolha a poltrona: "))
                classe1[opcao_poltrona-1] = "Ocupado"

            elif opcao_local == "o":
                opcao_poltrona = int(input("escolha a poltrona: "))
                classe2[opcao_poltrona-1] = "Ocupado"
            elif opcao_local == "a":
                 opcao_poltrona = int(input("escolha a poltrona: "))
                 executiva[opcao_poltrona-1] = "Ocupado"
           
   
   
    # Mostrar o mapa
        elif op == 2:
            print("-----------------------------------------------------------")
            print("\t1ºclasse\t executiva \t2ºclasse")
            print("-----------------------------------------------------------")
            for c in range(1, 16):
                print(f"\t{classe1[c-1]}\t\t{executiva[c-1]}\t\t{classe2[c-1]}")
        elif op == 3:
            break
def pagamento():
    print("--------------")
    print("menu pagamento")
    print("--------------")
    print("\n")
    print("1 - A vista(10% de desconto)")
    print("2 - Boleto")
    print("3 - cartão(até 12x sem juros)")
    op=int(input("digite a forma de pagamento desejada"))
    valor=float(input("digite o valor:"))
    if(op==1):
        print("1 - ecolheu primeira classe?")
        print("2 - escolheu segunda classe?")
        print("3 - escolheu 2°classe?")
        o1=int(input("digite a opção desejada"))
        if(o1==1):
            total=valor+(valor/0.5)*0.1
            print("valor a vista mais primeira classe foi de: {}".format(total))
        elif(o1==2):
            total=valor+(valor/0.3)*0.1
            print("o valor a vista mais classe executiva é: {}".format(total))
        elif(o1==3):
             total=valor*0.1
             print("o valor a vista é: {}".format(total))
    elif(op==2):
        print("1 - escolheu primeira classe?")
        print("2 - ecolheu classe executiva?")
        print("3 - escolheu segunda classe?")
        o2=int(input("digite a opção desejada:"))
        if(o2==1):
            nome=str(input("digite seu nome: "))
            c=str(input("digite o seu CPF: "))
            d=str(input("digite a data: "))
            total2=valor/0.5
            print("--------------------------------------------------------")
            print(" comprovante de boleto aviões blue tour")
            print("--------------------------------------------------------")
            print("nome: {}".format(nome))
            print("CPF: {}".format(c))
            print("data: {}".format(d))
            print("\n")
            print("\n")
            print("valor a pagar: {} com acrecimo de 50% da primeira classe".format(total2))
            print("você têm até dois dias uteis pra pagar viu")
            print("--------------------------------------------------------")
            print("\n\n\n")
        elif(o2==2):
            nome=str(input("digite seu nome: "))
            c=str(input("digite o seu CPF: "))
            d=str(input("digite a data: "))
            total3=valor/0.3
            print("-------------------------------------------------------")
            print(" comprovante de boleto aviões blue tour")
            print("-------------------------------------------------------")
            print("nome: {}".format(nome))
            print("CPF: {}".format(c))
            print("data: {}".format(d))
            print("\n")
            print("\n")
            print("valor a pagar: {} com acrecimo de 30% da primeira classe".format(total3))
            print("você têm até dois dias uteis pra pagar viu")
            print("---------------------------------------------------------")
            print("\n\n\n")
        elif(o2==3):
            nome=str(input("digite seu nome: "))
            c=str(input("digite o seu CPF: "))
            d=str(input("digite a data: "))
            print("------------------------------------------")
            print(" comprovante de boleto aviões blue tour")
            print("------------------------------------------")
            print("nome: {}".format(nome))
            print("CPF: {}".format(c))
            print("data: {}".format(d))
            print("\n")
            print("\n")
            print("valor a pagar: {}".format(valor))
            print("você têm até dois dias uteis pra pagar viu")
            print("------------------------------------------")
            print("\n\n\n")
    elif(op==3):
        print("1 - cartão debito")
        print("2 - cartão credito")
        o=int(input("digite a forma de pagamento"))
        if(o==1):
             print("1 - escolheu primeira classe?")
             print("2 - ecolheu classe executiva?")
             print("3 - escolheu segunda classe?")
             o3=int(input("digite a opção desejada:"))
             if(o3==1):
                print("seu pagamento via cartão do debito foi de: {}".format(valor))
        elif(o==2):
            total=valor/1
            print("o valor via credito em 1X é: {}".format(total))
            total2=valor/2
            print("o valor via credito em 2X é: {}".format(total2))
            total3=valor/3
            print("o valor via credito em 3X é: {}".format(total3))
            total4=valor/4
            print("o valor via credito em 4X é: {}".format(total4))
            total5=valor/5
            print("o valor via credito em 5X é: {}".format(total5))
            total6=valor/6
            print("o valor via credito em 6X é: {}".format(total6))
            total7=valor/7
            print("o valor via credito em 7X é: {}".format(total7))
            total8=valor/8
            print("o valor via credito em 8X é: {}".format(total8))
            total9=valor/9
            print("o valor via credito em 9X é: {}".format(total9))
            total10=valor/10
            print("o valor via credito em 10X é: {}".format(total10))
            total11=valor/11
            print("o valor via credito em 11X é: {}".format(total11))
            total12=valor/12
            print("o valor via credito em 12X é: {}".format(total12))


   
   
def menu():
    print("-"*31)
    print("\U0001F600""agência de viagens blue tour""\U0001F600")
    print("-"*31)
    print("1 - dados de assentos")
    print("2 - formas de pagamentos")
    print("3 - viagens disponiveis")
    print("4 - sair")

##Principal
while True:
    menu()
    op=int(input("Digite a opção:"))
    if(op==1):
        cadeira()
    elif(op==2):
        pagamento()
    elif(op==3):
        viagens()