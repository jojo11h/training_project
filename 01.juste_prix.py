import random as r

prix = r.randint(1, 10)

score = 100

tentatives = 0

bool = False

print("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 10 inclus.")

while bool == False:
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
