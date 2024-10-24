introducao = input("Deseja jogar este jogo? Sim (S)/ Não (N): ").lower()

if introducao == "s" or introducao == "sim":
    nome = input("Como é que queres que o teu personagem se chame? ")
    print("\n==================== BEM-VINDO AO JOGO RETORNO A CASA! ====================")
    print(f"\n Olá {nome}! Você acordou numa floresta a meio da noite e está perdido sem nada nos bolsos, apenas com uma mochila nas costas e a sua missão é voltar para casa em segurança. Dê o seu melhor e vamos a isto!")
elif introducao == "n" or introducao == "não":
    print("\nOh nãoo. Volta outro dia!")
else:
    print("Insira uma opção válida!")
