
def calculate(first_number, second_number, operator):
    match operator:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '/':
            if second_number == 0:
                return 'Division par 0 impossible'
            return first_number / second_number
        case _:
            return "Opérateur invalide"


while True:
    number_1 = input('Entrez le premier chiffre (ou q pour quitter):')

    if number_1 == 'q':
        break

    number_2 = input("Entrez le deuxième chiffre : ")
    operator = input(
        "Quelle opération souhaitez-vous effectuer ? (+, -, *, /): ")

    if not number_1.isdigit() and not number_2.isdigit():
        print('Veuillez rentrez des chiffres !')

    else:
        result = calculate(int(number_1), int(number_2), operator)
        print('Résultat : ', result)
