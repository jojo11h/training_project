import time
import csv
print("E-TECH.COM")


def read_file(file_to_read):
    with open(file_to_read, 'r', encoding='utf-8') as file:
        read_data = csv.reader(file, delimiter=';')
        data = list(read_data)
        return data


def show_business(name, activity, localisation, date):
    print(name)
    print(f"- Est une entreprise de {activity} ")
    print(f"- Elle a etait créé en {date}")
    print(f"- Sont addresse est actuellement : {localisation} ")


def show_employee(employee):
    print(
        "  ID  |  First Name  |  Last Name  |  Birthdate  |  Start Job  |  Salary (€)")
    for data in employee:
        print("-" * 70)
        print(
            f"{data[0]:3} | {data[1]:12} | {data[2]:11} | {data[3]:10} | {data[4]:10} | {data[5]:9}€")

# Affichage des paramètres donnés sous forme de tableau


def show_product(produits):
    print(
        "  ID  |  Name  |  Quantity  |  Value (€)")
    for data in produits:
        print("-"*40)
        print(f'{data[0]:3} | {data[1]:13} | {data[3]:5} | {data[2]:8}€')


# fonction qui supprime les doublons et additionne les quantités
def update_product_csv(file):
    product_totals = {}

    for item in file:
        product_id, product_name, price, quantity = item
    # Vérifier si le nom du produit est déjà présent dans le dictionnaire
        if product_name in product_totals:
            # ajouter la quantité actuelle à la quantité existante
            product_totals[product_name][3] = str(
                int(product_totals[product_name][3]) + int(quantity))
        else:
            # Sinon, ajouter une nouvelle entrée dans le dictionnaire
            product_totals[product_name] = item
    # Convertir le dictionnaire en une liste de listes
    result = list(product_totals.values())
    return result


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
            file = 'entreprise.csv'
            print()
            # notion unpacking https://www.pythoniste.fr/python/packing-et-unpacking-d-arguments-de-fonctions-en-python/
            _, name, activity, localisation, date = list(read_file(file))[0]
            show_business(name, activity, localisation, date)
            time.sleep(2.5)

        case '2':
            file = 'salarie.csv'
            show_employee(read_file(file))
            # stop un temp donné avant l'affichage du menu
            time.sleep(2.5)

        case '3':
            file = 'stock.csv'
            show_product(update_product_csv(read_file(file)))
            # show_product(read_file(file))
            # stop un temp donné avant l'affichage du menu
            time.sleep(2.5)
        case "4":
            break
