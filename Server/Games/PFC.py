from Server.Networking import *


def play_p_f_c(c1, c2):

    # Envoyer drmande choix
    send_message_to_all(c1, c2, "[Pierre/Feuille/Ciseaux]", True)
    choix1, choix2 = receive_message_from_all(c1, c2)

    # tests chaque combinaison
    gagnant = trouver_gagnant(choix1, choix2)

    # Envoyer resultat

def trouver_gagnant(choix1, choix2):
    if choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"
    elif choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"
    elif choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"
    elif choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"
    elif choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"
    elif choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"
    elif choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"
    elif choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"
    else choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"