import random as r

print("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 10 inclus.")


def choose_difficulty():
    while True:
        difficult = input(
            'Choisissez la difficulté (1-facile, 2-moyen, 3-difficile) : ')
        if difficult == '1':
            return r.randint(1, 10)
        elif difficult == '2':
            return r.randint(1, 50)
        elif difficult == '3':
            return r.randint(1, 100)
        else:
            print('Veuillez entrer une difficulté valide (1, 2 ou 3)')


def game(prix):
    bool = False
    score = 100
    tentatives = 0

    while not bool:
        nombre = int(input('=> '))
        tentatives += 1
        if nombre < prix:
            print("Le just prix est plus haut")

        elif nombre > prix:
            print("Le juste prix est plus bas")

        else:
            print(
                f"Félicitations, vous avez trouvé le juste prix {prix} en {tentatives} essais, votre score est {int(score / tentatives)} !")

            bool = True


prix = choose_difficulty()
print(prix)
game(prix)
