# Message de bienvenue
print("Bienvenue dans Python Pizza Delivery")

# Demander la taille de la pizza
taille = input("Quelle taille de pizza voulez-vous ? Petite, Moyenne ou Grande: ").lower()

# Demander si le client veut du pepperoni
add_pepperoni = input("Voulez-vous ajouter du pepperoni ? (Y/N): ").lower()

# Demander si le client veut du fromage supplémentaire
extra_cheese = input("Voulez-vous du fromage supplémentaire ? (Y/N): ").lower()

# Initialiser le prix
prix = 0

# Définir les prix en fonction de la taille de la pizza
if taille == "petite":
    prix = 15
elif taille == "moyenne":
    prix = 20
elif taille == "grande":
    prix = 25

# Ajouter le prix du pepperoni si demandé
if add_pepperoni == "y":
    if taille == "petite":
        prix += 2
    else:
        prix += 3

# Ajouter le prix du fromage supplémentaire si demandé
if extra_cheese == "y":
    prix += 1

# Afficher la facture finale
print(f"Votre facture finale est de : {prix} $")
