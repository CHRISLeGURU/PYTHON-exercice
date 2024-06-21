import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon application")
fenetre.configure(background='black')

# Ajout d'un label (texte)
label = tk.Label(fenetre, text="Hello, world!")
label.pack()  # Positionnement du label dans la fenêtre

# Ajout d'un bouton
def click_bouton():
  print("Bouton pressé !")

bouton = tk.Button(fenetre, text="Cliquez-moi", command=click_bouton)
bouton.pack()

# Lancement de la boucle principale qui gère l'affichage et les interactions
fenetre.mainloop()