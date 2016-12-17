from Server.Networking import *


def play_p_f_c(c1, c2):
    rej1 = 'oui'
    rej2 = 'oui'
    while rej1 == 'oui' and rej2 == 'oui':
        # Envoyer drmande choix
        send_message_to_all(c1, c2, "[Pierre/Feuille/Ciseaux]", True)
        choix1, choix2 = receive_message_from_all(c1, c2)

        # tests chaque combinaison
        gagnant = trouver_gagnant(choix1, choix2)

        # Envoyer resultat
        send_message_to_all(c1, c2, "Le gagnant est : " + gagnant + " car Joueur 1 a choisi " + choix1 + " et Joueur 2 a "
                                                                                                        "choisi " + choix2)

        # Rejouer ?
        send_message_to_all(c1, c2, 'Rejouer ? [oui/non]', True)
        rej1, rej2 = receive_message_from_all(c1, c2)


def trouver_gagnant(choix1, choix2):
    if choix1=="Pierre" and choix2 == "Feuille":
        gagnant = "Joueur 2"
    elif choix1=="Pierre" and choix2 == "Pierre":
        gagnant = "Personne"
    elif choix1=="Pierre" and choix2 == "Ciseaux":
        gagnant = "Joueur 1"

    elif choix1=="Feuille" and choix2 == "Feuille":
        gagnant = "Personne"
    elif choix1=="Feuille" and choix2 == "Pierre":
        gagnant = "Joueur 1"
    elif choix1=="Feuille" and choix2 == "Ciseaux":
        gagnant = "Joueur 2"

    elif choix1=="Ciseaux" and choix2 == "Feuille":
        gagnant = "Joueur 1"
    elif choix1=="Ciseaux" and choix2 == "Ciseaux":
        gagnant = "Personne"
    elif choix1 == "Ciseaux" and choix2 == "Pierre":
        gagnant = "Joueur 2"
    else
        gagnant = "Retapez, gogoles"
    return gagnant