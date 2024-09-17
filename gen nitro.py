import random
import string
import requests
import time
from colorama import Fore, Style, init

# Initialisation de colorama avec autorestart pour éviter de réinitialiser manuellement les couleurs
init(autoreset=True)

def generate_nitro_code():
    """Génère un code Discord Nitro aléatoire de 16 ou 24 caractères."""
    length = random.choice([16, 24])  # Discord Nitro peut avoir 16 ou 24 caractères
    nitro_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return nitro_code

def check_nitro_code_api(nitro_code):
    """Vérifie le code Discord Nitro en utilisant l'API Discord."""
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True  # Le code est valide
        else:
            return False  # Le code est invalide ou l'API a échoué
    except requests.RequestException as e:
        print(Fore.RED + f"Erreur lors de la vérification du code : {e}")
        return False

def save_valid_codes(valid_codes):
    """Sauvegarde les codes valides dans le fichier valid_nitro.txt."""
    with open("valid_nitro.txt", "w") as file:
        for code in valid_codes:
            file.write(f"https://discord.gift/{code}\n")

def homepage():
    """Affiche la page d'accueil et gère l'entrée de l'utilisateur."""
    while True:
        print(Fore.RED + r" ______                             __    __  __    __                                _______                    ______   __                  ________                                        ")
        print(Fore.RED + r" /      \                           |  \  |  \|  \  |  \                              |       \                  /      \ |  \                |        \                                        ")
        print(Fore.RED + r"|  $$$$$$\  ______   _______        | $$\ | $$ \$$ _| $$_     ______    ______        | $$$$$$$\ __    __       |  $$$$$$\| $$   __  __    __  \$$$$$$$$ ______    ______    ______   _______  ")
        print(Fore.RED + r"| $$ __\$$ /      \ |       \       | $$$\| $$|  \|   $$ \   /      \  /      \       | $$__/ $$|  \  |  \      | $$___\$$| $$  /  \|  \  |  \    /  $$ /      \  /      \  /      \ |       \ ")
        print(Fore.RED + r"| $$|    \|  $$$$$$\| $$$$$$$\      | $$$$\ $$| $$ \$$$$$$  |  $$$$$$\|  $$$$$$\      | $$    $$| $$  | $$       \$$    \ | $$_/  $$| $$  | $$   /  $$ |  $$$$$$\|  $$$$$$\|  $$$$$$\| $$$$$$$\ ")
        print(Fore.RED + r"| $$ \$$$$| $$    $$| $$  | $$      | $$\$$ $$| $$  | $$ __ | $$   \$$| $$  | $$      | $$$$$$$\| $$  | $$       _\$$$$$$\| $$   $$ | $$  | $$  /  $$  | $$    $$| $$    $$| $$    $$| $$  | $$")
        print(Fore.RED + r"| $$__| $$| $$$$$$$$| $$  | $$      | $$ \$$$$| $$  | $$|  \| $$      | $$__/ $$      | $$__/ $$| $$__/ $$      |  \__| $$| $$$$$$\ | $$__/ $$ /  $$___| $$$$$$$$| $$$$$$$$| $$$$$$$$| $$  | $$")
        print(Fore.RED + r" \$$    $$ \$$     \| $$  | $$      | $$  \$$$| $$   \$$  $$| $$       \$$    $$      | $$    $$ \$$    $$       \$$    $$| $$  \$$\ \$$    $$|  $$    \\$$     \ \$$     \ \$$     \| $$  | $$")
        print(Fore.RED + r"  \$$$$$$   \$$$$$$$ \$$   \$$       \$$   \$$ \$$    \$$$$  \$$        \$$$$$$        \$$$$$$$  _\$$$$$$$        \$$$$$$  \$$   \$$ _\$$$$$$$ \$$$$$$$$ \$$$$$$$  \$$$$$$$  \$$$$$$$ \$$   \$$")
        print(Fore.RED + r"                                                                                                |  \__| $$                          |  \__| $$                                                  ")
        print(Fore.RED + r"                                                                                                 \$$    $$                           \$$    $$                                                  ")
        print(Fore.RED + r"                                                                                                  \$$$$$$                             \$$$$$$                                                   ")

        print(Fore.RED + "Bienvenue dans le Générateur de Codes Discord Nitro !")
        print(Fore.RED + " Discord : https://discord.gg/bbSqHcpFUD")
        
        try:
            num_codes = int(input(Fore.RED + "Entrez le nombre de codes Nitro à générer : "))
            if num_codes <= 0:
                raise ValueError("Le nombre de codes doit être un entier positif.")
        except ValueError as e:
            print(Fore.RED + f"Entrée invalide : {e}")
            continue

        print(Fore.RED + f"\nGénération de {num_codes} codes Discord Nitro :")

        valid_codes = []
        valid_count = 0
        invalid_count = 0

        for _ in range(num_codes):
            nitro_code = generate_nitro_code()
            
            # Vérification du code avec un délai entre les requêtes
            valid = "Valide" if check_nitro_code_api(nitro_code) else "Invalide"
            if valid == "Valide":
                valid_count += 1
                valid_codes.append(nitro_code)
            else:
                invalid_count += 1
            
            print(f"Lien Discord Nitro : https://discord.gift/{nitro_code} ({Fore.RED}{valid})")

            # Attendre 1 seconde avant la prochaine vérification pour éviter d'être banni
            time.sleep(1)

        # Sauvegarde les codes valides dans le fichier
        save_valid_codes(valid_codes)

        print(Fore.RED + "\nRécapitulatif :")
        print(Fore.RED + f"Codes Valides : {valid_count}")
        print(Fore.RED + f"Codes Invalides : {invalid_count}")

        # Demander si l'utilisateur souhaite retourner à l'accueil ou quitter
        again = input(Fore.RED + "\nSouhaitez-vous générer d'autres codes Nitro ? (oui/non) : ").strip().lower()
        if again != 'oui':
            break

    # Message final et attente de l'entrée de l'utilisateur avant de fermer
    print(Fore.RED + "\nMerci d'avoir utilisé le Générateur de Codes Discord Nitro !")
    input(Fore.RED + "Appuyez sur Entrée pour quitter...")

# Appelle la fonction d'accueil pour commencer
homepage()
