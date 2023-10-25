print("E-TECH.COM")

bisiness = {
    "nom_entreprise": "E-TECH.COM",
    "activite_entreprise": "Vente de matériel i-tech en ligne",
    "adresse_entreprise": "18 rue de la tech 94301 Palo Alto USA ",
    "date_create_entreprise": "18/06/1995",
}

salarie_tab = [
    [1, "Marrant", "Solange", "01/04/1985", "19/05/2014", "35000.00"],
    [2, "Durant", "Christophe", "19/11/1991", "02/09/2019", "25000.00"],
    [3, "Salambre", "Marine", "21/01/1982", "31/10/2016", "30000.00"],
]

produit_tab = [
    [1, "Iphone 14", 999.00, 10],
    [2, "Ipad 10", 699.00, 5],
    [3, "MacBook Pro 5", 1999.00, 5],
]


def show_business(name, activity, localisation, date):
    print(name)
    print(f"est une entreprise de {activity} ")
    print(f"elle a etait créé en {date}")
    print(f"sont addresse est actuellement : {localisation} ")


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

    match user_prompt:
        case "1":
            info = bisiness.values()
            print(info[0])
            # show_business(info[0], info[1], info[2], info[3])
        case "4":
            break
