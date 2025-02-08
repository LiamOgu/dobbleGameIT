
import time

class Chrono_IA:
    def __init__(self, temps: int):
        '''c'est la méthode qui permet d'initialiser la classe Chrono_IA. Elle initialise le temps .'''
        self.temps = temps
        self.temps_depart = time.time()
    
    def IA_play(self) -> bool:
        '''Cette méthode ne prend pas d'argument. Elle retourne True quand le temps(en secondes) entré dans l'init est atteint.'''
        temps_actuel = time.time()
        if temps_actuel - self.temps_depart >= self.temps:
            self.temps_depart = temps_actuel
            return True