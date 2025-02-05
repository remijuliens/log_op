"""Application visuelle servant à créer rapidement
des expressions logiques, sans avoir à toujours chercher
dans les caractères spéciaux. """

from tkinter import *
from tkinter import ttk
import unicodedata



class App:
    def __init__(self, liste_operateur):
        self.root = Tk()
        self.root.focus_force()
        self.mainframe = ttk.Frame(self.root, height=500, width=1000)
        self.liste_operateur = liste_operateur
        
        self.mainframe.grid(sticky = NSEW)
        self.dict_button = {}

    def init_button(self):
        for i, j in enumerate(self.liste_operateur, start=1):
            
            nom = f'b{i}'  #nom dynamique
            self.dict_button[nom] = ttk.Button(self.mainframe, text = chr(int(j, 16)) , command =(lambda c=j: self.click(c)))
            self.dict_button[nom].grid(pady=10)

    def click(self, c):
        print("Yes")

#TODO A CONTINUER
#TODO : comment passer un argument à une commande (boutton de tkinter)
#TODO : comment utiliser le unicode avec une variable. (ce qui s'affiche sur le boutton)


def get_unicode():
    l = []
    with open('/Users/remi-juliensavard/Documents/ProjetsPython/carac_logique/liste_carac.txt', 'r') as liste:
        for line in liste:
            ligne = line.strip().split(", ")
            l.append(ligne[1])
    return l

def main():
    
    liste_operateur = get_unicode()
    app = App(liste_operateur)
    app.init_button()
    
    for key, value in app.dict_button.items():
        print(f'clé :{key} ---> {value}')
    
    app.root.mainloop()
    



if __name__ == "__main__":
    main()
