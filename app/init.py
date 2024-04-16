import utils.func_network as bot_network

def start_bot():
    print("Initialisation du bot")
    print("Sélection du mode du bot : 1 - Farm, 2 - Combat, 3 - Trade")

    mode = -1
    modes = [1,2,3]
    job = -1
    jobs = [1,2,3,4,5]

    while mode not in modes:
        mode = int(input("Entrez mode : "))

    if mode == 1:
        print("Quel métier veux-tu travailler ? 1 - Alchimiste, 2 - Bûcheron, 3 - Paysan, 4 - Pêcheur, 5 - Mineur")

        while job not in jobs:
            job = int(input("Entrez métier : "))

        if job == 1:
            ressource_offset = 35

            print("Combien de ressources veux-tu farmer ? (entre 1 et 4)")
            
            nb_ressources = -1
            while nb_ressources not in list(range(1,5)):
                nb_ressources = int(input("Entrez nombre de ressources : "))

            print("Quelle ressource veux-tu farmer ? 1 - Ortie, 2 - Sauge, 3 - Trèfle à 5 feuilles, 4 - Menthe sauvage")

            selected_ressources = []
            ressources = [1,2,3,4]
            ressource = -1
            for i in range(nb_ressources):
                print("Ressource numéro " + str(i+1) + ":")
                while ressource not in ressources:
                    ressource = int(input("Entrez ressource sélectionnée : "))
                    if ressource in selected_ressources:
                        ressource = -1
                        print("Ressource déjà sélectionnée")
                    selected_ressources.append(ressource)
                ressource = -1

            for i in selected_ressources:
                print(bot_network.make_request_dofus_map(ressource_offset + i, 0))

        else :
            print("Métier non implémenté, au travail !")

        return
    else :
        print("Mode non implémenté, au travail !")

        return


