print("E-TECH.COM")

while True:
    print("\n Que voulez-vous faire :")
    print("1 - Informations sur l'entrepise")
    print("2 - Information sur les salariés")
    print("3 - Liste des produits ainsi que ces stoks")
    print("4 - Quitter")
    print()
    user_prompt = input(" ==> ")

    if not user_prompt.isdigit() and user_prompt not in ["1", "2", "3", "4"]:
        print(f"La saisie {user_prompt} n'est pas reconnu ! ")
