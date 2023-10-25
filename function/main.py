import time
print("E-TECH.COM")

business = {
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
    print(f"- Est une entreprise de {activity} ")
    print(f"- Elle a etait créé en {date}")
    print(f"- Sont addresse est actuellement : {localisation} ")


def show_employee(employee):
    print(
        "  ID  |  First Name  |  Last Name  |  Birthdate  |  Start Job  |  Salary (€)")
    for id, first_name, last_name, birthdate, start_job, salary in employee:
        print("-" * 70)  # Ligne de séparation
        print(
            f"{id:3} | {first_name:12} | {last_name:11} | {birthdate:10} | {start_job:10} | {salary:9}€")


def show_product(produits):
    print(
        "  ID  |  Name  |  Quantity  |  Value (€)")
    for id, name, price, qte in produits:
        print("-"*40)
        print(f'{id:3} | {name:13} | {qte:5} | {price:8}€')


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
            show_business(business["nom_entreprise"], business["activite_entreprise"],
                          business["adresse_entreprise"], business["date_create_entreprise"])
            time.sleep(2.5)

        case '2':
            show_employee(salarie_tab)
            time.sleep(2.5)

        case '3':
            show_product(produit_tab)
            time.sleep(2.5)
        case "4":
            break
