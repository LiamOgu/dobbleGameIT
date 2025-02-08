from PileDeCarte import PileDeCarte

class Joueur:

  def __init__(self, nom, paquet:PileDeCarte, difficulte="moyen"):
    self.nom = nom
    self.paquet = paquet
    self.difficulte = difficulte
    self.points = 0

  def __str__(self):
    return f"la carte qu'on voit, du joueur {self.nom} est:\n{self.paquet.indice_carte(-1)}\n"
  
  """def console_game(self):
    x = int(input("le symbole en commun: "))"""

  def afficher_tout_le_paquet(self):  #juste pour voir, c un brouillon
    return f"voici tous le paquet de {self.nom}:\n{str(self.paquet)}"

  def ajout_point(self):
    self.points += 1

  def retrait_point(self):
    self.points -= 1

  def a_gagne(self):
    return f"Gagné!"

  def nom(self):
    return self.nom
  
  def carte(self):
    return self.paquet.indice_carte(-1)
