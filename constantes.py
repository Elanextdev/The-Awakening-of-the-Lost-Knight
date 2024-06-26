import pygame

FPS = 60

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

# Dimensions de la fenetre
LARGEUR = 800
HAUTEUR = 600

# Création de la fenetre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
surface_pause = pygame.Surface((LARGEUR, HAUTEUR), pygame.SRCALPHA)

game_state = ""

game_frames = []

image_pause = pygame.Surface((0,0))

score = 0

zoom_carte = 2

volume = 30

# Bouton menu
bouton_background = "assets/images/bouton_background.png"

# Fond du menu
fond = pygame.image.load("assets/images/fond_menu.png").convert_alpha()

# Chargement du personnage du lobby
personnage_dos = pygame.image.load("assets/images/personnage/Vu_dos.png").convert_alpha()
personnage_dos = pygame.transform.scale(personnage_dos, (personnage_dos.get_width() * 3, personnage_dos.get_height() * 3))

personnage_dos_marche1 = pygame.image.load("assets/images/personnage/Pied_gauche_bas.png").convert_alpha()
personnage_dos_marche1 = pygame.transform.scale(personnage_dos_marche1, (personnage_dos_marche1.get_width() * 3, personnage_dos_marche1.get_height() * 3))

personnage_dos_marche2 = pygame.image.load("assets/images/personnage/Pied_droit_bas.png").convert_alpha()
personnage_dos_marche2 = pygame.transform.scale(personnage_dos_marche2, (personnage_dos_marche2.get_width() * 3, personnage_dos_marche2.get_height() * 3))

personnage_face = pygame.image.load("assets/images/personnage/Vu_face.png").convert_alpha()
personnage_face = pygame.transform.scale(personnage_face, (personnage_face.get_width() * 3, personnage_face.get_height() * 3))

personnage_face_marche1 = pygame.image.load("assets/images/personnage/Vu_face_-_Pied_droit_bas.png").convert_alpha()
personnage_face_marche1 = pygame.transform.scale(personnage_face_marche1, (personnage_face_marche1.get_width() * 3, personnage_face_marche1.get_height() * 3))

personnage_face_marche2 = pygame.image.load("assets/images/personnage/Vu_face_-_Pied_gauche_bas.png").convert_alpha()
personnage_face_marche2 = pygame.transform.scale(personnage_face_marche2, (personnage_face_marche2.get_width() * 3, personnage_face_marche2.get_height() * 3))

personnage_droite = pygame.image.load("assets/images/personnage/Vu_cote_droite.png").convert_alpha()
personnage_droite = pygame.transform.scale(personnage_droite, (personnage_droite.get_width() * 3, personnage_droite.get_height() * 3))

personnage_droite_marche1 = pygame.image.load("assets/images/personnage/Vu_cote_droite_-_pied_droit_arriere.png").convert_alpha()
personnage_droite_marche1 = pygame.transform.scale(personnage_droite_marche1, (personnage_droite_marche1.get_width() * 3, personnage_droite_marche1.get_height() * 3))

personnage_droite_marche2 = pygame.image.load("assets/images/personnage/Vu_cote_droite_-_pied_gauche_arriere.png").convert_alpha()
personnage_droite_marche2 = pygame.transform.scale(personnage_droite_marche2, (personnage_droite_marche2.get_width() * 3, personnage_droite_marche2.get_height() * 3))


personnage_gauche = pygame.image.load("assets/images/personnage/Vu_cote_gauche.png").convert_alpha()
personnage_gauche = pygame.transform.scale(personnage_gauche, (personnage_gauche.get_width() * 3, personnage_gauche.get_height() * 3))

personnage_gauche_marche1 = pygame.image.load("assets/images/personnage/Vu_cote_gauche_-_pied_droite_arriere.png").convert_alpha()
personnage_gauche_marche1 = pygame.transform.scale(personnage_gauche_marche1, (personnage_gauche_marche1.get_width() * 3, personnage_gauche_marche1.get_height() * 3))

personnage_gauche_marche2 = pygame.image.load("assets/images/personnage/Vu_cote_gauche_-_pied_gauche_arriere_.png").convert_alpha()
personnage_gauche_marche2 = pygame.transform.scale(personnage_gauche_marche2, (personnage_gauche_marche2.get_width() * 3, personnage_gauche_marche2.get_height() * 3))

pos_personnage = (LARGEUR // 2, HAUTEUR // 2)

# Elements de la map
carte = pygame.image.load("assets/images/map.png").convert_alpha()  # Chargement de la map

eau_1 = pygame.image.load("assets/images/eau/frame_0_delay-0.3s.png").convert_alpha()
eau_1 = pygame.transform.scale(eau_1, (eau_1.get_width() * 3, eau_1.get_height() * 3))

eau_2 = pygame.image.load("assets/images/eau/frame_1_delay-0.3s.png").convert_alpha()
eau_2 = pygame.transform.scale(eau_2, (eau_2.get_width() * 3, eau_2.get_height() * 3))

eau_3 = pygame.image.load("assets/images/eau/frame_2_delay-0.3s.png").convert_alpha()
eau_3 = pygame.transform.scale(eau_3, (eau_3.get_width() * 3, eau_3.get_height() * 3))

eau_4 = pygame.image.load("assets/images/eau/frame_3_delay-0.3s.png").convert_alpha()
eau_4 = pygame.transform.scale(eau_4, (eau_4.get_width() * 3, eau_4.get_height() * 3))

chateau_sable = pygame.image.load("assets/images/chateau-sable.png").convert_alpha()
chateau_sable = pygame.transform.scale(chateau_sable, (chateau_sable.get_width() * 2, chateau_sable.get_height() * 2))

caisse = pygame.image.load("assets/images/caisse.png").convert_alpha()
caisse = pygame.transform.scale(caisse, (caisse.get_width() * 2, caisse.get_height() * 2))

palmier = pygame.image.load("assets/images/palmier.png").convert_alpha()
palmier = pygame.transform.scale(palmier, (palmier.get_width() * 5, palmier.get_height() * 5))

arbre = pygame.image.load("assets/images/arbre.png").convert_alpha()
arbre = pygame.transform.scale(arbre, (arbre.get_width() * 3, arbre.get_height() * 3))

arbre_haut = pygame.image.load("assets/images/arbre_haut.png").convert_alpha()
arbre_haut = pygame.transform.scale(arbre_haut, (arbre_haut.get_width() * 3, arbre_haut.get_height() * 3))

# Options menu
pause = False

unpause_game = False

est_menu = False

musique = True

venu_de = ""

last_keys = ""

running = True

debug_mod = False

def animation(sens):
    if sens == "haut":
        fenetre.blit(personnage_dos, personnage_dos.get_rect(center=(pos_personnage)))
    elif sens == "bas":
        fenetre.blit(personnage_face, personnage_face.get_rect(center=(pos_personnage)))














