from done.py 


def menu_principal():
    while True:
        print("Menu Principal:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Quitter")

        choix = input("Sélectionnez une option : ")

        if choix == "1":
          print(done) 
        elif choix == "2":
            option2()
        elif choix == "3":
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")

def option1():
    print(done)
    # Ajoutez ici le code pour l'Option 1

def option2():
    print("Vous avez sélectionné l'Option 2.")
    # Ajoutez ici le code pour l'Option 2

if __name__ == "__main__":
    menu_principal()
