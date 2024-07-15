def afficher_menu():
    print("Menu des options :")
    print("1. Ajouter un article")
    print("2. Supprimer un article")
    print("3. Afficher la liste")
    print("4. Quitter")

def ajouter_article(shopping_list, max_items):
    if len(shopping_list) < max_items:
        article = input("Entrez l'article à ajouter : ")
        shopping_list.append(article)
        print(f"'{article}' a été ajouté à la liste.")
    else:
        print("La liste est pleine. Vous ne pouvez pas ajouter plus d'articles.")

def supprimer_article(shopping_list):
    article = input("Entrez l'article à supprimer : ")
    if article in shopping_list:
        shopping_list.remove(article)
        print(f"'{article}' a été supprimé de la liste.")
    else:
        print(f"L'article '{article}' n'est pas dans la liste.")

def afficher_liste(shopping_list):
    if shopping_list:
        print("Liste des articles :")
        for i, article in enumerate(shopping_list, 1):
            print(f"{i}. {article}")
    else:
        print("La liste est vide.")

def main():
    shopping_list = []
    max_items = 10 

    while True:
        afficher_menu()
        choix = input("Faites une sélection (1-4) : ")

        if choix == '1':
            ajouter_article(shopping_list, max_items)
        elif choix == '2':
            supprimer_article(shopping_list)
        elif choix == '3':
            afficher_liste(shopping_list)
        elif choix == '4':
            print("Au revoir!")
            break
        else:
            print("Sélection invalide. Veuillez choisir une option entre 1 et 4.")

if _name_ == "_main_":
    main()
