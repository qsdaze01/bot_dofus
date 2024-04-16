def start_bot():
    print("Initialisation du bot")
    print("Sélection du mode du bot : 1 - Farm, 2 - Combat, 3 - Trade")

    mode = -1
    modes = [1,2,3]

    while mode not in modes:
        mode = int(input("Entrez mode"))

    if mode == 1:
        print("Quel métier veux-tu travailler ?")
    else :
        print("Mode non implémenté, au travail !")


