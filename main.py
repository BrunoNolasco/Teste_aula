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
    
def ouvir_historia():
    print("Qual tipo de história você gostaria de ouvir?")
    escolha_historia = input("cavaleiro, princesa ou mágico?").strip().lower()
    
    if escolha_historia == "cavaleiro":
        print("Era uma vez um cavaleiro chamado Hugo. Ele era corajoso, mas nunca tinha enfrentado um dragão. "
            "Um dia, o rei pediu sua ajuda. Um dragão está dormindo no meio da estrada principal! Ninguém consegue passar! "
            "Hugo foi até lá montado em seu cavalo. Quando chegou, viu o dragão roncando alto. Em vez de usar a espada, "
            "Hugo teve uma ideia. Ele assobiou uma música bem calma. O dragão abriu os olhos devagar… e começou a chorar. "
            "— Eu só queria um lugar quieto pra dormir... Hugo levou o dragão até uma caverna bem longe da cidade. "
            "O dragão dormiu feliz, e Hugo virou herói — sem lutar. Moral: Nem todo problema precisa de força. Às vezes, basta escutar.")



estado()
qual_nome()
ouvir_historia()


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