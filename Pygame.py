from Joueur import Joueur
from PileDeCarte import PileDeCarte
from Chono_IA import Chrono_IA
from pygame import *
from random import *

class Pygame:

  def __init__(self, joueur1:Joueur, joueur2:Joueur, pioche:PileDeCarte):
    '''Initialise les principaux composants du jeu,
      la fenêtre, les joueurs, toutes les images et les sons.
      Ainsi que les variables que nous aurons besoin dans tout le programme.'''

    display.set_caption("Dobble")  # titre de la page
    self.screen = display.set_mode((800, 730))  # hauteur et largeur de la page
    self.screen_size = self.screen.get_size()
    size_x = self.screen.get_width()

    self.joueur1 = joueur1
    self.joueur2 = joueur2
    self.pioche = pioche

    self.windows_list = ("accueil", "help", "modif", "login", "game", "result_score")
    self.current_window = "accueil"
    self.font = font.Font("komika_text/KOMTXTB_.ttf", 30) # on initie une police d'écriture
    self.font_login = font.Font('komika_text/KOMTXT__.ttf', 40)

    self.taille_carte = (200, 200)
    self.taille_symbole = (self.taille_carte[0]/4.16, self.taille_carte[1]/4.16)

    self.is_modif_screen = False
    self.pause = False
    self.started = False
    self.finit = False
    self.dragging_j1 = False
    self.dragging_j2 = False
    self.dragging_pioche = False
    self.offset = 0

    self.name_player = ''
    self.entry_name_selected = False

    self.dif_dict = {"easy":(5, 7), "normal":(3, 6), "hard":(1, 4)}
    self.ia_time = self.dif_dict["normal"]
    self.ia_set = Chrono_IA(self.ia_time)
    
    #sons
    self.correct_click = mixer.Sound("sons/click_win.wav")
    self.incorrect_click = mixer.Sound("sons/click_error.wav")
    self.place_card_sound = mixer.Sound("sons/card_flip.mp3")

    #toutes les images

    self.carte = {
      "front":image.load("cartes/carte_front.png").convert_alpha(),
      "behind":image.load("cartes/carte_behind.png").convert_alpha(),
      "pos_j1" :(size_x/2-self.taille_carte[0]/2, 520),
      "pos_j2" :(size_x/2-self.taille_carte[0]/2, 20),
      "pos_pioche" :(size_x/2-self.taille_carte[0]/2, 270)}
    
    self.fond_de_base = image.load("fonds/Fond_Dobble.png").convert()  #image de fond du accueil
    self.fond_jeu = image.load("fonds/Fond_jeu.png").convert()
    self.help_img = image.load("fonds/help_img.png").convert()
    self.fond_result = image.load("fonds/results_fond.png").convert()

    #boutons
    self.help_button = {
    "bouton": image.load("boutons/help.png").convert_alpha(),
    "bouton_h": image.load("boutons/help_h.png").convert_alpha(),
    "pos": (630, 15),
    "clicked" : False}

    self.modif_button = {
        "bouton": image.load("boutons/modifier.png").convert_alpha(),
        "bouton_h": image.load("boutons/modifier_h.png").convert_alpha(),
        "pos": (630, 650),
    "clicked" : False}

    self.retour_button = {
        "bouton": image.load("boutons/retour.png").convert_alpha(),
        "bouton_h": image.load("boutons/retour_h.png").convert_alpha(),
        "pos": (20, 20),
    "clicked" : False}

    self.reprendre_button = {
        "bouton": image.load("boutons/reprendre.png").convert_alpha(),
        "bouton_h": image.load("boutons/reprendre_h.png").convert_alpha(),
        "pos": (size_x/2-80.5, 280),
    "clicked" : False}

    self.quitter_button = {
        "bouton": image.load("boutons/quitter.png").convert_alpha(),
        "bouton_h": image.load("boutons/quitter_h.png").convert_alpha(),
        "pos": (size_x/2-80.5, 650),
    "clicked" : False}

    self.commencer_button = {
        "bouton": image.load("boutons/commencer.png").convert_alpha(),
        "bouton_h": image.load("boutons/commencer_h.png").convert_alpha(),
        "pos": (300, 575),
    "clicked" : False}

    self.accueil_button = {
        "bouton": image.load("boutons/accueil.png").convert_alpha(),
        "bouton_h": image.load("boutons/accueil_h.png").convert_alpha(),
        "pos": (size_x/2-80.5, 375),
    "clicked" : False}

    self.easy_button = {
        "bouton": image.load("boutons/easy.png").convert_alpha(),
        "bouton_h": image.load("boutons/easy_h.png").convert_alpha(),
        "pos": (50, 425),
    "clicked" : False}

    self.normal_button = {
        "bouton": image.load("boutons/normal.png").convert_alpha(),
        "bouton_h": image.load("boutons/normal_h.png").convert_alpha(),
        "pos": (280, 425),
    "clicked" : False}

    self.hard_button = {
        "bouton": image.load("boutons/hard.png").convert_alpha(),
        "bouton_h": image.load("boutons/hard_h.png").convert_alpha(),
        "pos": (510, 425),
    "clicked" : False}

    self.jouer_button = {
        "bouton": image.load("boutons/jouer.png").convert_alpha(),
        "bouton_h": image.load("boutons/jouer_h.png").convert_alpha(),
        "pos": (300, 600),
    "clicked" : False}

    self.name_entry_button = {
        "bouton": image.load("boutons/name_entry.png").convert_alpha(),
        "bouton_h": image.load("boutons/name_entry_h.png").convert_alpha(),
        "pos": (270, 290),
    "clicked" : False}

    self.recommencer_button = {
        "bouton": image.load("boutons/recommencer.png").convert_alpha(),
        "bouton_h": image.load("boutons/recommencer_h.png").convert_alpha(),
        "pos": (300, 200),
    "clicked" : False}

    self.ecran_titre_button = {
        "bouton": image.load("boutons/ecran_titre.png").convert_alpha(),
        "bouton_h": image.load("boutons/ecran_titre_h.png").convert_alpha(),
        "pos": (300, 300),
    "clicked" : False}

    self.plus_bouton = {"bouton": image.load("boutons/plus.png"),
                        "bouton_h": image.load("boutons/plus_h.png"),
                        "pos": (500, 20),
                        "clicked": False}
    
    self.moins_bouton = {"bouton": image.load("boutons/moins.png"),
                         "bouton_h": image.load("boutons/moins_h.png"),
                        "pos": (600, 20), "clicked": False}
    
    self.reinitialiser_bouton = {"bouton": image.load("boutons/reinitialiser.png"),
                            "bouton_h": image.load("boutons/reinitialiser_h.png"),
                        "pos": (700, 20), "clicked": False}

    #images symboles :
    self.intel_img = image.load("symboles/intel.png").convert_alpha()
    self.internet_img = image.load("symboles/internet.png").convert_alpha()
    self.nvidia_img = image.load("symboles/nvidia.png").convert_alpha()
    self.computer_img = image.load("symboles/computer.png").convert_alpha()
    self.keyboard_img = image.load("symboles/keyboard.png").convert_alpha()
    self.phone_img = image.load("symboles/phone.png").convert_alpha()
    self.mail_img = image.load("symboles/mail.png").convert_alpha()
    self.windows_img = image.load("symboles/windows.png").convert_alpha()
    self.amazon_img = image.load("symboles/amazon.png").convert_alpha()
    self.bitcoin_img = image.load("symboles/bitcoin.png").convert_alpha()
    self.brawl_star_img = image.load("symboles/brawl_star.png").convert_alpha()
    self.c_sharp_img = image.load("symboles/c_sharp.png").convert_alpha()
    self.discord_img = image.load("symboles/discord.png").convert_alpha()
    self.google_translate_img = image.load("symboles/google_translate.png").convert_alpha()
    self.ios_img = image.load("symboles/ios.png").convert_alpha()
    self.js_img = image.load("symboles/js.png").convert_alpha()
    self.lol_img = image.load("symboles/lol.png").convert_alpha()
    self.micro_img = image.load("symboles/micro.png").convert_alpha()
    self.minecraft_img = image.load("symboles/minecraft.png").convert_alpha()
    self.netflix_img = image.load("symboles/netflix.png").convert_alpha()
    self.pinterest_img = image.load("symboles/pinterest.png").convert_alpha()
    self.pronote_img = image.load("symboles/pronote.png").convert_alpha()
    self.pycharm_img = image.load("symboles/pycharm.png").convert_alpha()
    self.riot_img = image.load("symboles/riot.png").convert_alpha()
    self.samsung_img = image.load("symboles/samsung.png").convert_alpha()
    self.skype_img = image.load("symboles/skype.png").convert_alpha()
    self.snapchat_img = image.load("symboles/snapchat.png").convert_alpha()
    self.souris_img = image.load("symboles/souris.png").convert_alpha()
    self.speaker_img = image.load("symboles/speaker.png").convert_alpha()
    self.spotify_img = image.load("symboles/spotify.png").convert_alpha()
    self.steam_img = image.load("symboles/steam.png").convert_alpha()
    self.tiktok_img = image.load("symboles/tiktok.png").convert_alpha()
    self.twitch_img = image.load("symboles/twitch.png").convert_alpha()
    self.uber_img = image.load("symboles/uber.png").convert_alpha()
    self.usb_img = image.load("symboles/usb.png").convert_alpha()
    self.vlc_img = image.load("symboles/vlc.png").convert_alpha()
    self.vpn_img = image.load("symboles/vpn.png").convert_alpha()
    self.windows_img = image.load("symboles/windows.png").convert_alpha()
    self.wifi_img = image.load("symboles/wifi.png").convert_alpha()
    self.X_img = image.load("symboles/X.png").convert_alpha()
    self.youtube_img = image.load("symboles/youtube.png").convert_alpha()
    self.sword_img = image.load("symboles/sword.png").convert_alpha()
    self.trash_img = image.load("symboles/trash.png").convert_alpha()
    self.xbox_img = image.load("symboles/xbox.png").convert_alpha()
    self.playstation_img = image.load("symboles/playstation.png").convert_alpha()
    self.python_img = image.load("symboles/python.png").convert_alpha()
    self.microsoft_img = image.load("symboles/microsoft.png").convert_alpha()
    self.logitech_img = image.load("symboles/logitech.png").convert_alpha()
    self.hp_img = image.load("symboles/hp.png").convert_alpha()
    self.dell_img = image.load("symboles/dell.png").convert_alpha()
    self.headphone_img = image.load("symboles/headphone.png").convert_alpha()
    self.controller_img = image.load("symboles/controller.png").convert_alpha()
    self.android_img = image.load("symboles/android.png").convert_alpha()
    self.airpod_img = image.load("symboles/airpod.png").convert_alpha()
    self.robot_img = image.load("symboles/robot.png").convert_alpha()
    self.deezer_img = image.load("symboles/deezer.png").convert_alpha()
    self.switch_img = image.load("symboles/switch.png").convert_alpha()
    self.laptop_img = image.load("symboles/laptop.png").convert_alpha()




    self.symboles = {1: self.computer_img,2:self.amazon_img, 3:self.bitcoin_img, 4:self.brawl_star_img, 5:self.c_sharp_img,
                     6:self.discord_img,7:self.google_translate_img,8:self.deezer_img,9:self.ios_img,10:self.js_img,11:self.switch_img,
                     12:self.lol_img,13:self.micro_img, 14: self.intel_img,15:self.minecraft_img,16:self.netflix_img,17:self.pinterest_img,
                     18:self.pronote_img,19: self.internet_img,20:self.pycharm_img,21:self.riot_img,22:self.samsung_img,23:self.skype_img,
                     24:self.snapchat_img,25: self.nvidia_img,26:self.souris_img,27:self.speaker_img,28: self.keyboard_img,29:self.spotify_img,
                     30:self.steam_img,31:self.tiktok_img,32:self.twitch_img,33:self.uber_img,34:self.usb_img,35:self.vlc_img, 36: self.phone_img,
                     37:self.vpn_img,38:self.wifi_img,39: self.mail_img, 40:self.windows_img, 41:self.X_img, 42:self.youtube_img, 43:self.sword_img,
                    44:self.trash_img, 45:self.xbox_img, 46:self.playstation_img, 47:self.python_img, 48:self.microsoft_img, 49:self.logitech_img,
                    50: self.laptop_img, 51:self.hp_img,52:self.dell_img,53:self.headphone_img,54:self.controller_img,55:self.android_img,
                    56:self.airpod_img,57:self.robot_img}


#Fonctions qui servent à l'affichage des différentes fenêtres. (fond, boutons, cartes, symboles...)
  def fonds(self, fond_name):
    '''Affiche les fonds du jeu en entrant le nom de sa variable,
    on s'en sert dans toutes les méthodes qui serviront à afficher une fenêtre différente.'''
    self.screen.blit(fond_name, (0, 0)) 

  def accueil_screen(self):
    '''L'écran d'accueil, affichage de tous les boutons qui sont présents sur l'accueil.'''
    self.fonds(self.fond_de_base)
    self.boutons_draw(self.help_button)
    self.boutons_draw(self.modif_button)
    self.boutons_draw(self.commencer_button)
    self.boutons_draw(self.quitter_button)
    
  def help_screen(self):
    '''affiche l'image et le bouton retour'''
    self.fonds(self.help_img)
    self.boutons_draw(self.retour_button)
         
  def modif_screen(self):
    '''affiche les 3 cartes de dos et les différents boutons'''
    self.fonds(self.fond_jeu)
    self.cartes_draw()
    self.boutons_draw(self.retour_button)
    self.boutons_draw(self.plus_bouton)
    self.boutons_draw(self.moins_bouton)
    self.boutons_draw(self.reinitialiser_bouton)

  def login_screen(self):
    '''Affiche l'entrée pour écrire son pseudo, les boutons de choix de difficultés, le bouton retour et jouer.'''
    self.fonds(self.fond_jeu)
    self.name_player_entry()
    self.dif_draw()
    self.boutons_draw(self.retour_button)
    self.boutons_draw(self.jouer_button)

  def name_player_entry(self):
    '''Affiche une case d'entée sous forme de bouton, le texte à l'intérieur est la variable self.name_player.'''
    self.boutons_draw(self.name_entry_button)
    entry_surface = self.font_login.render(self.name_player, True, (0, 0, 0))
    self.screen.blit(entry_surface, (self.boutons_rect(self.name_entry_button)))

  def dif_draw(self):
    '''Affiche les 3 boutons de choix de difficultés'''
    self.boutons_draw(self.easy_button)
    self.boutons_draw(self.normal_button)
    self.boutons_draw(self.hard_button)

  def game_screen(self):
    '''Affiche l'écran de jeu.'''
    self.fonds(self.fond_jeu)
    self.cartes_draw()
    self.name_players_draw()
    self.running = True

    if self.started:
      self.ia_play()
      self.nb_cartes_draw()

  def name_players_draw(self):
    '''Affiche le texte du nom des joueurs.
    celui du joueur 1 étant écrit en bas à gauche et celui du joueur 2 en haut à gauche.'''
    texte_j1 = self.font.render(self.name_player, True, (0, 0, 0))
    texte_j2 = self.font.render(self.joueur2.nom, True, (0, 0, 0))
    self.screen.blit(texte_j1, (5, 650))
    self.screen.blit(texte_j2, (5, 40))

  def nb_cartes_draw(self):
    '''Affiche le nombre de cartes restantes des joueurs. Sachant que les joueurs ont 20 cartes chacun
    les textes sont collés au texte du nom du joueur.'''
    nb_carte_j1 = self.font.render(f"Cartes restantes: {self.joueur1.paquet.nb_carte()}/20", True, (0, 0, 0))
    nb_carte_j2 = self.font.render(f"Cartes restantes: {self.joueur2.paquet.nb_carte()}/20", True, (0, 0, 0))
    self.screen.blit(nb_carte_j1, (0, 690))
    self.screen.blit(nb_carte_j2, (0, 5))
    
  def pause_screen(self):
    '''affiche l'écran de pause.'''
    draw.rect(self.screen, (255, 255, 0), (self.reprendre_button["pos"][0]-20, self.reprendre_button["pos"][1]-20, 200, 210), border_radius=15)
    draw.rect(self.screen, (238,130,238), (self.reprendre_button["pos"][0]-20, self.reprendre_button["pos"][1]-20, 200, 210), 7, border_radius=15)
    self.boutons_draw(self.reprendre_button)
    self.boutons_draw(self.accueil_button)

  def result_score_draw(self):
    '''Affiche l'écran de fin avec les resultats des points et du gagnant.'''
    self.fonds(self.fond_result)
    joueur1 = self.font.render(f"Vous: {self.joueur1.points}", True, (255, 255, 255))
    joueur2 = self.font.render(f"{self.joueur2.nom}: {self.joueur2.points}", True, (255, 255, 255))
    self.screen.blit(joueur1, (200, 50))
    self.screen.blit(joueur2, (200, 90))
    self.boutons_draw(self.recommencer_button)
    self.boutons_draw(self.ecran_titre_button)

    if self.joueur1.points > self.joueur2.points:
        gagne = self.font.render(f"Vous avez gagné!", True, (255, 255, 255))
    elif self.joueur1.points < self.joueur2.points:
        gagne = self.font.render(f"{self.joueur2.nom} a gagné!", True, (255, 255, 255))
    else:
        gagne = self.font.render("Match nul!", True, (255, 255, 255))
    self.screen.blit(gagne, (200, 130))
  
#Fonctions pour l'IA
  def ia_play(self):
    '''si le temps de l'IA est écoulé, la carte du joueur 2 est jouée'''
    if self.ia_set.IA_play() and not self.pause:
      self.place_card(self.joueur2)

  def reset_ia_time(self):
      '''Réinitialisation à 0 du temps de l'IA'''
      self.ia_set = Chrono_IA(randint(self.ia_time[0], self.ia_time[1]))

  def place_card(self, joueur:Joueur):
    '''Place la carte du joueur tout en jouant le son, en ajoutant un point au joueur et en réinitialisant le temps de l'IA.'''
    self.pioche.ajout_carte(joueur.paquet.indice_carte(-1))
    joueur.paquet.retrait_carte(-1)
    self.correct_click.play()
    joueur.ajout_point()
    self.reset_ia_time()

  def cartes_draw(self):
    '''Méthode qui va afficher les cartes.''' 
    self.carte["front"] = transform.scale(self.carte["front"], self.taille_carte)
    self.carte["behind"] = transform.scale(self.carte["behind"], self.taille_carte)
    if not self.pause and not self.started: #si on a pas start et que on est pas en pause, on affiche...
      self.screen.blit(self.carte["front"], self.carte["pos_j1"])
      self.screen.blit(self.carte["front"], self.carte["pos_j2"])
      self.screen.blit(self.carte["behind"], self.carte["pos_pioche"])
      self.images_symboles(self.cartes_rect('j1'),self.joueur1.paquet.indice_carte(-1))
      self.images_symboles(self.cartes_rect('j2'),self.joueur2.paquet.indice_carte(-1))
    if self.started and not self.pause:
      self.screen.blit(self.carte["front"], self.carte["pos_j1"])
      self.screen.blit(self.carte["front"], self.carte["pos_j2"])
      self.screen.blit(self.carte["front"], self.carte["pos_pioche"])
      self.images_symboles(self.cartes_rect('j1'),self.joueur1.paquet.indice_carte(-1))
      self.images_symboles(self.cartes_rect('j2'),self.joueur2.paquet.indice_carte(-1))
      self.images_symboles(self.cartes_rect('pioche'), self.pioche.indice_carte(-1))
    if self.pause or self.is_modif_screen:
      self.screen.blit(self.carte["behind"], self.carte["pos_j1"])
      self.screen.blit(self.carte["behind"], self.carte["pos_j2"])
      self.screen.blit(self.carte["behind"], self.carte["pos_pioche"])

  def cartes_rect(self, carte) -> Rect:
    '''carte : "j1", "j2", "pioche"
    Renvoie la collision des de la carte choisie'''
    image_rect = self.carte["front"].get_rect()
    image_rect.x, image_rect.y = (self.carte["pos_"+carte])
    return image_rect     
   
  def boutons_draw(self, image):
    ''''''
    clicked = image["clicked"]
    if clicked:
      self.screen.blit(image["bouton_h"], image["pos"])
    else:
      self.screen.blit(image["bouton"], image["pos"])
      
  def boutons_rect(self, image: Surface)-> Rect:
    '''Retourne le rect (la collision) d'un bouton suivant sa position'''
    rect_button = image["bouton"].get_rect()
    rect_button.x, rect_button.y = image["pos"]
    return rect_button

  def boutons_anim(self, image, clicked = False):
    if clicked == False:
      image["clicked"] = False
    else:
      image["clicked"] = True


  
  def images_symboles(self, cartes_rect, carte:list):
    '''Affiche tous les symboles de la carte sur la carte'''
    case = 1
    for i in carte:
      self.taille_symbole = (self.taille_carte[0]/4.16, self.taille_carte[1]/4.16)
      self.symboles[i] = transform.scale(self.symboles[i], (self.taille_symbole))
      self.screen.blit(self.symboles[i], self.rect_symbole(case, cartes_rect))
      case += 1  

  def rect_symbole(self, case, cartes_rect:cartes_rect):
    if case == 1:
      return Rect((cartes_rect.x + self.taille_carte[0]/2.5, cartes_rect.y), self.taille_symbole)
    if case == 2:
      return Rect((cartes_rect.x + self.taille_carte[0]/7.14, cartes_rect.y+self.taille_carte[0]/6.66), self.taille_symbole)
    if case == 3:
      return Rect((cartes_rect.x +self.taille_carte[0]/2.56, cartes_rect.y + self.taille_carte[0]/4.2), self.taille_symbole)
    if case == 4:
      return Rect((cartes_rect.x + self.taille_carte[0]/1.6, cartes_rect.y + self.taille_carte[0]/6.66), self.taille_symbole)
    if case == 5:
      return Rect((cartes_rect.x + self.taille_carte[0]/8, cartes_rect.y + self.taille_carte[0]/2.5), self.taille_symbole)
    if case == 6:
      return Rect((cartes_rect.x+ self.taille_carte[0]/2.66, cartes_rect.y + self.taille_carte[0]/2.1), self.taille_symbole)
    if case == 7:
      return Rect((cartes_rect.x + self.taille_carte[0]/1.6, cartes_rect.y + self.taille_carte[0]/2.5), self.taille_symbole)
    if case == 8:
      return Rect((cartes_rect.x + self.taille_carte[0]/2.22, cartes_rect.y + self.taille_carte[0]/1.46), self.taille_symbole)

  def redistribuer(self):
    self.pause = False
    self.started = False
    pile_temp = PileDeCarte([])
    pile_temp.ajout_piles(self.pioche)
    pile_temp.ajout_piles(self.joueur1.paquet)
    pile_temp.ajout_piles(self.joueur2.paquet)
    paquet_distribues = pile_temp.distribuer()
    self.joueur1.paquet = paquet_distribues[0]
    self.joueur2.paquet = paquet_distribues[1]
    self.pioche = paquet_distribues[2]
    
  def events(self, window):
    
    #tous les évènements (click souris, etc...)
    for events in event.get():
      # Quitter le jeu
      if events.type == QUIT:
        self.running = False
        exit()
      if window == "accueil":
        menu_boutons = [self.commencer_button, self.help_button, self.modif_button, self.quitter_button]
        if events.type == MOUSEBUTTONDOWN:
          for bouton in menu_boutons:
            if self.boutons_rect(bouton).collidepoint(mouse.get_pos()):
              self.boutons_anim(bouton, True)          

        if events.type == MOUSEBUTTONUP:
          for bouton in menu_boutons:
            if self.boutons_rect(bouton).collidepoint(mouse.get_pos()):
              self.boutons_anim(bouton)
              if bouton == self.help_button:
                self.current_window = "help"
              if bouton == self.modif_button:
                self.current_window = "modif"
              if bouton == self.commencer_button:
                self.current_window = "login"
              if bouton == self.quitter_button:
                exit()

      if window == "login":
        login_boutons = [self.retour_button, self.jouer_button, self.name_entry_button, self.easy_button, self.normal_button, self.hard_button]
        if events.type == MOUSEBUTTONDOWN:
          if not self.boutons_rect(self.name_entry_button).collidepoint(mouse.get_pos()):
            self.boutons_anim(self.name_entry_button)
            self.entry_name_selected = False

          for bouton in login_boutons:
            if self.boutons_rect(bouton).collidepoint(mouse.get_pos()):
              self.boutons_anim(bouton, True)
              if bouton == self.easy_button:
                self.ia_time = self.dif_dict["easy"]
                print(self.ia_time)
                self.boutons_anim(self.normal_button)
                self.boutons_anim(self.hard_button)
              if bouton == self.normal_button:
                self.ia_time = self.dif_dict["normal"]
                print(self.ia_time)
                self.boutons_anim(self.easy_button)
                self.boutons_anim(self.hard_button)
              if bouton == self.hard_button:
                self.ia_time = self.dif_dict["hard"]
                print(self.ia_time)
                self.boutons_anim(self.normal_button)
                self.boutons_anim(self.easy_button)
              if bouton == self.name_entry_button:
                self.entry_name_selected = True

        if events.type == MOUSEBUTTONUP:
          for bouton in range(0, 2):
            if self.boutons_rect(login_boutons[bouton]).collidepoint(mouse.get_pos()):
              self.boutons_anim(login_boutons[bouton])
              if login_boutons[bouton] == self.retour_button:
                self.current_window = "accueil"
              if login_boutons[bouton] == self.jouer_button:
                self.current_window = "game"
                self.reset_ia_time()

        if self.entry_name_selected:
          if events.type == KEYDOWN:
            if events.key == K_BACKSPACE:
              self.name_player = self.name_player[:-1]
            else:
              self.name_player += events.unicode

      if window == "game":
        if events.type == KEYDOWN:
          if events.key == K_ESCAPE:
            if self.pause:
              self.pause = False
            else:
              self.pause = True
        if self.pause:
          pause_boutons = [self.reprendre_button, self.accueil_button]
          if events.type == MOUSEBUTTONDOWN:
            for bouton in pause_boutons:
              if self.boutons_rect(bouton).collidepoint(mouse.get_pos()):
                self.boutons_anim(bouton, True)
          if events.type == MOUSEBUTTONUP:
            for bouton in pause_boutons:
              if self.boutons_rect(bouton).collidepoint(mouse.get_pos()):
                self.boutons_anim(bouton)
                if bouton == self.reprendre_button:
                  self.pause = False
                if bouton == self.accueil_button:
                  self.current_window = "accueil"
                  self.redistribuer()

        if events.type == MOUSEBUTTONDOWN and not self.pause:
          if self.cartes_rect('j2').collidepoint(mouse.get_pos()):
            pass
          if self.cartes_rect('j1').collidepoint(mouse.get_pos()):
            pass
          if self.cartes_rect('pioche').collidepoint(mouse.get_pos()) and self.started == False: #quand on touche le dos de la carte du milieu, ca commence le je
            self.started = True
            self.place_card_sound.play()
            self.reset_ia_time()

          #action symboles
          for case in range(1, 9):
            if self.rect_symbole(case, self.cartes_rect('j1')).collidepoint(mouse.get_pos()):
              if self.joueur1.paquet.indice_carte(-1)[case-1] in self.pioche.indice_carte(-1):
                print('correct')
                self.place_card(self.joueur1)
              else:
                print('incorrect')
                self.incorrect_click.play()
                self.joueur1.retrait_point()

      if window == "help":
        if events.type == MOUSEBUTTONDOWN:
          if self.boutons_rect(self.retour_button).collidepoint(mouse.get_pos()):
            self.boutons_anim(self.retour_button, True)

        if events.type == MOUSEBUTTONUP:
          if self.boutons_rect(self.retour_button).collidepoint(mouse.get_pos()):
              self.boutons_anim(self.retour_button)
              self.current_window = "accueil"

      if window == "result_score":
        self.redistribuer()
        result_score_boutons = [self.recommencer_button, self.ecran_titre_button]
        if events.type == MOUSEBUTTONDOWN:
          for bouton in result_score_boutons:  
            if self.boutons_rect(bouton).collidepoint(mouse.get_pos()):
              self.boutons_anim(bouton, True)
        if events.type == MOUSEBUTTONUP:
          for bouton in result_score_boutons:  
            if self.boutons_rect(bouton).collidepoint(mouse.get_pos()):
              self.boutons_anim(bouton)

              if bouton == self.recommencer_button:
                self.current_window = "game"
                self.joueur1.points = 0
                self.joueur2.points = 0
              if bouton == self.ecran_titre_button:
                self.current_window = "accueil"
                self.joueur1.points = 0
                self.joueur2.points = 0
          
      if window == "modif":
        modif_boutons = [self.plus_bouton, self.moins_bouton, self.reinitialiser_bouton]
        if events.type == MOUSEBUTTONDOWN:
          for bouton in modif_boutons:
            if self.boutons_rect(bouton).collidepoint(mouse.get_pos()):
              self.boutons_anim(bouton, True)

          if self.boutons_rect(self.retour_button).collidepoint(mouse.get_pos()):
            self.current_window = "accueil"
          if self.cartes_rect("j2").collidepoint(mouse.get_pos()):
            self.dragging_j2 = True
            mouse_x, mouse_y = mouse.get_pos()
            self.offset = (self.carte["pos_j2"][0] - mouse_x, self.carte["pos_j2"][1] - mouse_y)

          if self.cartes_rect("j1").collidepoint(mouse.get_pos()):
            self.dragging_j1 = True
            mouse_x, mouse_y = mouse.get_pos()
            self.offset = (self.carte["pos_j1"][0] - mouse_x, self.carte["pos_j1"][1] - mouse_y)
          if self.cartes_rect("pioche").collidepoint(mouse.get_pos()):
            self.dragging_pioche = True
            mouse_x, mouse_y = mouse.get_pos()
            self.offset = (self.carte["pos_pioche"][0] - mouse_x, self.carte["pos_pioche"][1] - mouse_y)

        if events.type == MOUSEBUTTONUP:
          for bouton in modif_boutons:
            if self.boutons_rect(bouton).collidepoint(mouse.get_pos()):
              self.boutons_anim(bouton)
              if bouton == self.plus_bouton:
                self.taille_carte = (self.taille_carte[0]+20, self.taille_carte[1]+20)
              if bouton == self.moins_bouton:
                self.taille_carte = (self.taille_carte[0]-20, self.taille_carte[1]-20)
              if bouton == self.reinitialiser_bouton:
                self.taille_carte = (200, 200)
                self.carte["pos_j1"] = (self.screen.get_width()/2-self.taille_carte[0]/2, 520)
                self.carte["pos_j2"] = (self.screen.get_width()/2-self.taille_carte[0]/2, 20)
                self.carte["pos_pioche"] = (self.screen.get_width()/2-self.taille_carte[0]/2, 270)

          self.dragging_j2 = False
          self.dragging_j1 = False
          self.dragging_pioche = False

        if events.type == MOUSEMOTION:
          if self.dragging_j2:
            mouse_x, mouse_y = mouse.get_pos()
            self.carte["pos_j2"] = (self.offset[0]+mouse_x, self.offset[1]+mouse_y)
          if self.dragging_j1:
            mouse_x, mouse_y = mouse.get_pos()
            self.carte["pos_j1"] = (self.offset[0]+mouse_x, self.offset[1]+mouse_y)
          if self.dragging_pioche:
            mouse_x, mouse_y = mouse.get_pos()
            self.carte["pos_pioche"] = (self.offset[0]+mouse_x, self.offset[1]+mouse_y)

  def run(self):
    self.running = True

    while self.running:

      if self.joueur1.paquet.est_vide() or self.joueur2.paquet.est_vide():
          self.finit = True
          self.current_window = "result_score"

      if self.current_window == "accueil":
        self.accueil_screen()
        self.events("accueil")

      if self.current_window == "help":
        self.help_screen()
        self.events("help")

      if self.current_window == "modif":
        self.is_modif_screen = True
        self.modif_screen()
        self.events("modif")

      if self.current_window == "login":
        self.login_screen()
        self.events("login")

      if self.current_window == "game":
        self.game_screen()
        self.events("game")
        if self.pause:
          self.pause_screen()
      
      if self.current_window == "result_score":
        self.result_score_draw()
        self.events("result_score")
      
      self.is_modif_screen = False

      display.flip()