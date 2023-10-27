import time
import csv


def read_file(file_to_read):
    with open(file_to_read, "r", encoding="utf-8") as file:
        read_data = csv.reader(file, delimiter=";")
        data = list(read_data)
        return data


print("-" * 20, "E-TECH.COM", "-" * 20)


def show_business(name, activity, localisation, date):
    print(name)
    print(f"- Est une entreprise de {activity} ")
    print(f"- Elle a etait créé en {date}")
    print(f"- Sont addresse est actuellement : {localisation} ")


# Affichage des paramètres donnés sous forme de tableau


def show_employee(employee):
    print(
        "  ID  |  First Name  |  Last Name  |  Birthdate  |  Start Job  |  Salary (€)"
    )
    for id, first_name, last_name, birthdate, start_job, salary in employee:
        print("-" * 70)
        print(
            f"{id:3} | {first_name:12} | {last_name:11} | {birthdate:10} | {start_job:10} | {salary:9}€"
        )
    print("-" * 70)


# Affichage des paramètres donnés sous forme de tableau


def show_product(produits):
    print("  ID  |  Name  |  Quantity  |  Value (€)")
    for id, name, price, qte in produits:
        print("-" * 40)
        print(f"{id:3} | {name:13} | {qte:5} | {price:8}€")
    print("-" * 40)


# Boucle jusqu'a la commande pour sortir
while True:
    # Affichage du menu
    print("\n Que voulez-vous faire :")
    print("1 - Informations sur l'entrepise")
    print("2 - Information sur les salariés")
    print("3 - Liste des produits ainsi que ces stoks")
    print("4 - Quitter")
    print()
    # Recupération donnée de l'utilisateur
    user_prompt = input(" ==> ")
    # Contrôle de la donnée de l'utilisateur
    if not user_prompt.isdigit() and user_prompt not in ["1", "2", "3", "4"]:
        print(f"La saisie {user_prompt} n'est pas reconnu ! ")
    # lanceLancement d'un programme en fontion de la donnée utilisateur
    match user_prompt:
        case "1":
            show_business(
                read_file("entreprise.csv")[0][1],
                read_file("entreprise.csv")[0][2],
                read_file("entreprise.csv")[0][3],
                read_file("entreprise.csv")[0][4],
            )
            # stop un temp donné avant l'affichage du menu
            time.sleep(2.5)

        case "2":
            data = read_file("salarie.csv")
            print(data[1])
            # for i, line in enumerate(data):
            #     data[i] = show_employee(*line)
            # print(read_file("salarie.csv"))
            # show_employee(salarie_tab)
            # stop un temp donné avant l'affichage du menu
            time.sleep(2.5)

        case "3":
            # show_product(produit_tab)
            # stop un temp donné avant l'affichage du menu
            time.sleep(2.5)
        case "4":
            break
