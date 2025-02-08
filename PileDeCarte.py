import random

class PileDeCarte:
  # Classe permettant de créer la pile de carte originelle.
  def __init__(self, Paquet, milieu = False):
    # Cette fonction prend en argument une liste de cartes et un booléen. Elle permet d’initialiser une pile de cartes.
    self.pile_carte = Paquet
    self.milieu = milieu

  def __str__(self):
    # Cette fonction ne prend pas d’argument. Elle permet d’afficher la pile de carte
    if self.milieu == True:
      return f"voici le paquet du milieu:\n{self.pile_carte[-1]}\n"
    a = ''
    for i in range(len(self.pile_carte)):
      a += (f"{self.pile_carte[i]}\n")
    return f"{a}"

  def __len__(self):
    # Cette fonction ne prend pas d’argument. Elle renvoie la longueur de la pile de cartes
    return len(self.pile_carte)

  def indice_carte(self, i):
    # Cette fonction prend en argument un integer i.  Cela renvoie la carte numéro i du paquet.
    if not self.est_vide():
      return self.pile_carte[i]

  def est_vide(self):
    # Cette fonction ne prend pas d’argument. Elle renvoie True si la pile de cartes est vide et False si elle est remplie
    return len(self.pile_carte) == 0

  def nb_carte(self):
    # Cette fonction ne prend pas d’argument. Elle renvoie le nombre de cartes présentes dans la pile de cartes.
    return len(self.pile_carte)

  def nouvelle_partie(self):
    # Cette fonction ne prend pas d’argument. Elle vide la pile de cartes.
    self.pile_carte = []

  def ajout_carte(self, nv_carte):
    # Cette fonction prend en argument une liste composé de 8 integer qui n’a pas plusieurs fois le même élément.
    # Elle permet d’ajouter une carte (nv_carte) à la pile de cartes
    if type(nv_carte) != list:
      raise TypeError("La nouvelle carte doit être une liste")
    if len(nv_carte) != 8:
      raise ValueError("La nouvelle carte doit être composé de 8 symboles")
    if len(nv_carte) != len(set(nv_carte)):
      raise ValueError("La nouvelle carte ne dois pas avoir 2 fois le même élément")
    self.pile_carte.append(nv_carte)

  def retrait_carte(self, i):
    # Cette fonction prend en argument un intéger i. Elle permet de supprimer la carte à l’indice i .
    del self.pile_carte[i]

  def melange_pile(self):
    # Cette fonction ne prend pas d’arguments. Elle permet de mélanger la pile de cartes.
    random.shuffle(self.pile_carte)
  def distribuer(self):
    # Cette fonction ne prend pas d’arguments. Elle distribue toutes les cartes de la pile aux deux joueurs et au milieu
    random.shuffle(self.pile_carte)
    x = 41
    paquet_joueur1 = PileDeCarte([])
    paquet_joueur2 = PileDeCarte([])
    paquet_milieu = PileDeCarte([], True)
    for j in range(x // 2):
      paquet_joueur1.ajout_carte(self.pile_carte[0])
      del self.pile_carte[0]

    for k in range(x // 2):
      paquet_joueur2.ajout_carte(self.pile_carte[0])
      del self.pile_carte[0]

    paquet_milieu.ajout_carte(self.pile_carte[0])
    del self.pile_carte[0]
    

    return (paquet_joueur1, paquet_joueur2, paquet_milieu)

  def ajout_piles(self, other):
    # Cette fonction prend en argument une autre pile de carte other. Met à jour la pile de carte en l'additionant à
    # l'autre pile de carte other
    self.pile_carte += other.pile_carte