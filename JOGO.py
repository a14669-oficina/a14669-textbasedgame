# RETORNO A CASA
introducao = input("Desejas jogar este jogo? Sim (S) / Não (N): ").lower()

if introducao in ["s", "sim"]:
    nome = input("Que nome queres chamar ao teu personagem? ")
    print(f"\n==================== BEM-VINDO AO JOGO RETORNO A CASA! ====================")
    print(f"\nOlá {nome}! Acordaste numa floresta à noite, perdido, com uma mochila nas costas. Dentro dela, tens um machado, uma lanterna, água e comida. A tua missão é voltar para casa em segurança. Vamos a isso!")

    escolha = input("\nÀ tua frente há dois caminhos. Um para a direita e outro para a esquerda. Qual escolhes? ").lower()

    if escolha == "direita":
        print("\nEscolheste o caminho da direita. Enquanto avanças, aparece de repente uma cobra!")
        luta = input("Vais lutar com a cobra? Sim (S) / Não (N): ").lower()

        if luta in ["s", "sim"]:
            print("\nLutaste contra a cobra e conseguiste derrotá-la! Continua a tua jornada.")
            entrar_caverna = input("Encontras uma caverna misteriosa. Vais entrar? Sim (S) / Não (N): ").lower()

            if entrar_caverna in ["s", "sim"]:
                print("\nDentro da caverna, encontras tesouros, mas também perigos! Vais tentar pegar no tesouro? Sim (S) / Não (N): ")
                desafio = input().lower()
                if desafio in ["s", "sim"]:
                    print("\nAtivaste uma armadilha e ficaste preso! Infelizmente, morreste. Volta ao início!")
                else:
                    print("\nDecidiste não pegar no tesouro e saíste da caverna em segurança. À frente, encontras um caminho para uma estrada familiar!")
                    print(f"\nParabéns, {nome}! Conseguiste voltar para casa em segurança!")
            else:
                print("\nDecidiste não entrar na caverna e continuaste o caminho. Mais à frente, encontras uma ponte.")
                atravessar_ponte = input("Vais atravessar a ponte? Sim (S) / Não (N): ").lower()

                if atravessar_ponte in ["s", "sim"]:
                    print("\nAtravessaste a ponte com sucesso e chegaste a uma vila. Parabéns, voltaste para casa!")
                else:
                    print("\nFicaste na floresta e, com a noite, crocodilos apareceram. Morreste.")

        else:
            print("\nA cobra atacou-te enquanto hesitavas. Infelizmente, morreste.")

    elif escolha == "esquerda":
        print("\nEscolheste o caminho da esquerda e chegaste a um lago com crocodilos.")
        atravessar = input("Vais tentar atravessar o lago? Sim (S) / Não (N): ").lower()

        if atravessar in ["s", "sim"]:
            print("\nOs crocodilos estavam distraídos e conseguiste atravessar o lago com sucesso, mais à frente encontraste um grupo de viajantes.")
            ajudar_viajantes = input("Vais ajudar os viajantes com o que tens na mochila? Sim (S) / Não (N): ").lower()

            if ajudar_viajantes in ["s", "sim"]:
                print("\nOs viajantes ficaram gratos e ofereceram-te um mapa que mostra um caminho seguro de volta para casa. Parabéns, voltaste para casa!")
            else:
                print("\nDecidiste continuar sozinho e acabaste por te perder na floresta. Morreste.")
        else:
            print("\nDecidiste não atravessar e os crocodilos se aproximaram. Morreste.")

    else:
        print("Escolha um caminho válido!")

elif introducao in ["n", "não"]:
    print("\nOh não! Volta outro dia!")
else:
    print("Insira uma opção válida!")
