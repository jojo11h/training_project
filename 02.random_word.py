import requests as req
import random as r


def choose_word():
    url = "https://raw.githubusercontent.com/lorenbrichter/Words/master/Words/fr.txt"
    res = req.get(url)
    return r.choice(list(res.text.split()))


def play_game(word):
    bool = False
    remaining_attemps = 6
    letters_used = list()
    hide_word = ["_"] * len(word)

    print("Bienvenue au jeu du Pendu!")

    while remaining_attemps > 0 and not bool:
        letter = input("Entrez une lettre : \n => ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("veuillez rentrez UNE SEULE lettre valide [A-Z,a-z]")

        elif letter in letters_used:
            print("Vous avez déjà utilisé cette lettre")

        elif letter in word:
            print("ca match !")

            for index, element in enumerate(word):
                if element == letter:
                    hide_word[index] = element
        else:
            print("ca ne match pas !")
            remaining_attemps -= 1
            print(f"(il te reste {remaining_attemps} tentatives)")
            letters_used.append(letter)
            print(f"les lettres utilisées : {letters_used}")

        if hide_word == list(word):
            print("Bravos tu a gagné !!!!!")
            bool = True

        if remaining_attemps <= 0:
            print("Tu a perdu !")
            print()
            print(f"le mot caché était : {word}")

        print()
        print(" ".join(hide_word))
        print()


word = choose_word()
play_game(word)
