# RETORNO A CASA
introducao = input("Desejas jogar este jogo? Sim (S)/ Não (N): ").lower()

if introducao == "s" or introducao == "sim":
    nome = input("Que nome queres chamar ao teu personagem? ")
    print("\n==================== BEM-VINDO AO JOGO RETORNO A CASA! ====================")
    print(f"\nOlá {nome}! Acordaste numa floresta a meio da noite e está perdido sem nada nos bolsos, apenas com uma mochila nas costas. Na mochila tens um machado, uma lanterna, água e comida. A tua missão é voltar para casa em segurança. Dá o teu melhor e vamos a isto!")

    print("\nÀ tua frente há dois caminhos. Um para a direita e outro para a esquerda.")
    escolha = input("Qual deseja escolher? (Direita ou Esquerda): ").lower()

    if escolha == "direita":
        print("\nEscolheste o caminho da direita.")
        print("Enquanto avanças aparece derrepente uma cobra!")
        luta = input("Vais lutar com a cobra? Sim (S) / Não (N): ").lower()

        if luta == "s" or luta == "sim":
            print("\nLutas contra a cobra e consegues derrotá-la!")
            print("Como derrotas-te a cobra agora podes continuar a tua jornada.")
            print("Continuando, encontras uma caverna misteriosa.")
            entrar_caverna = input("Vais entrar na caverna? Sim (S) / Não (N): ").lower()

            if entrar_caverna == "s" or entrar_caverna == "sim":
                print("\nDentro da caverna, encontras tesouros, mas também muitos perigos!")
                desafio = input("Vais tentar pegar no tesouro? Sim (S) / Não (N): ").lower()
                if desafio == "s" or desafio == "sim":
                    print("\nEnquanto tentas pegar no tesouro, uma armadilha é ativada e ficaste preso!")
                    print("Infelizmente, não conseguiste escapar. Morreste.")
                    print("Volta ao início!")
                elif desafio == "n" or desafio == "não":
                    print("\nDecidiste não pegar no tesouro e sair da caverna em segurança.")
                    print("À frente, encontras um caminho que leva a uma estrada familiar!")
                    print(f"\nParabéns, {nome}! Conseguiste voltar para casa em segurança!")
                else:
                    print("Insira uma opção válida!")

            elif entrar_caverna == "n" or entrar_caverna == "não":
                print("\nDecidiste não entrar na caverna e continuaste o teu caminho.")
                print("Mais à frente encontras uma ponte.")
                atravessar_ponte = input("Vais atravessar a ponte? Sim (S) / Não (N): ").lower()

                if atravessar_ponte == "s" or atravessar_ponte == "sim":
                    print("\nAtravessaste a ponte com sucesso!")
                    print("Do outro lado, vês uma vila e decidiste ir até lá.")
                    print(f"\nParabéns, {nome}! Conseguiste voltar para casa em segurança!")
                elif atravessar_ponte == "n" or atravessar_ponte == "não":
                    print("\nDecidiste não atravessar a ponte e ficaste na floresta.")
                    print("Infelizmente, a noite chegou e vários crocodilos aparecem. Morreste.")
                    print("Volta ao início!")
                else:
                    print("Insira uma opção válida!")

        elif luta == "n" or luta == "não":
            print("\nComo não fizeste nada, a cobra atacou-te e morreste!")
            print("Volta ao início!")
        else:
            print("Insira uma opção válida!")

    elif escolha == "esquerda":
        print("\nEscolheste o caminho da esquerda.")
        print("Chegaste a um lago, onde vês dois crocodilos.")
        atravessar = input("Vais tentar atravessar o lago? Sim (S) / Não (N): ").lower()

        if atravessar == "s" or atravessar == "sim":
            print("\nTentas atravessar o lago a nado.")
            print("Os crocodilos parecem distraídos e consegues passar com sucesso!")
            print("\nDepois de atravessares, encontras um grupo de viajantes.")
            ajudar_viajantes = input("Vais ajudar os viajantes com o que tens na mochila? Sim (S) / Não (N): ").lower()

            if ajudar_viajantes == "s" or ajudar_viajantes == "sim":
                print("\nOs viajantes ficam muito gratos e oferecem-te um mapa!")
                print("O mapa mostra um caminho seguro de volta para casa.")
                print(f"\nParabéns, {nome}! Conseguiste voltar para casa em segurança!")
            elif ajudar_viajantes == "n" or ajudar_viajantes == "não":
                print("\nDecidiste não ajudar os viajantes e continuaste sozinho.")
                print("Infelizmente, acabas por te perder na floresta e morres.")
                print("Volta ao início!")
            else:
                print("Insira uma opção válida!")

        elif atravessar == "n" or atravessar == "não":
            print("\nDecidiste não atravessar o lago e ficaste à margem.")
            print("Os crocodilos se aproximam e, infelizmente, morres.")
            print("Volta ao início!")
        else:
            print("Insira uma opção válida!")

    else:
        print("Escolha um caminho válido!")

elif introducao == "n" or introducao == "não":
    print("\nOh não! Volta outro dia!")
else:
    print("Insira uma opção válida!")
