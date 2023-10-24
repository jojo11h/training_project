import os

os.system("cls")
cwd = os.getcwd()

files = ["01.juste_prix.py", "02.random_word.py", "03.calculatrice.py"]
print(cwd)

while True:
    print("_" * 50)
    print("A quoi tu veux jouer ?")
    print("-> 1. Juste prix")
    print("-> 2. Jeu du pendu")
    print("-> 3. Calculatrice")
    print(' -> "q pour quitter ')
    user_choice = input("=> ")

    if user_choice == "q":
        break

    if user_choice not in ["1", "2", "3"]:
        print("Veuillez choisir une donnée valide !")

    else:
        match user_choice:
            case "1":
                os.system(
                    f"py C:/Users/LocaBox/Desktop/algo/training_project/{files[int(user_choice)-1]}"
                )
            case "2":
                os.system(
                    f"py C:/Users/LocaBox/Desktop/algo/training_project/{files[int(user_choice)-1]}"
                )
            case "3":
                os.system(
                    f"py C:/Users/LocaBox/Desktop/algo/training_project/{files[int(user_choice)-1]}"
                )
            case _:
                print("essais")
