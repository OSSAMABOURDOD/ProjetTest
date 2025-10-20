# Afficher le tableau de multiplication de 1 à 10

for i in range(1, 11):          # Boucle pour le multiplicande (1 à 10)
    print(f"\nTable de {i} :")  # Titre de chaque table
    for j in range(1, 11):      # Boucle pour le multiplicateur (1 à 10)
        resultat = i * j
        print(f"{i} x {j} = {resultat}")