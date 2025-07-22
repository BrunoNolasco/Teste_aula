def estado():
    tudo_bem = input("Olá! Tudo bem? (sim ou não): ").strip().lower()

    if tudo_bem == "sim":
        print("Que legal, então vamos deixá-lo ainda melhor!")
    elif tudo_bem == "não":
        print("Que pena, mas não se preocupe, vamos melhorá-lo!")
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
        
def qual_nome():
    nome = input("Qual o seu nome?").strip().lower()
    print(f"Eu adoro o seu nome, {nome}!")

estado()
qual_nome()


#
#
#
#
#
#print("Olá pessoal!")
#
#
#
#
#
#
#nome: str = input("Qual é o seu nome? ")
#print(f"Olá, {nome}!")
#
#
#print("Tudo bem?")