from Server.Networking import *
import random


def play_pile_face(c1, c2):

    play_again = True
    while play_again == True:
        # Ask bets
        send_message_to_all(c1, c2, "Pile ou face ? [pile/face]", True)
        choix_p1, choix_p2 = receive_message_from_all(c1, c2)

        # Throw coin
        piece = lancer_piece()

        # Results
        if choix_p1 == piece and choix_p2 != piece:
            send_message_to_all(c1, c2, 'La pièce est tombée sur ' + piece + '. Et... le joueur 1 gagne !')
        elif choix_p2 == piece and choix_p1 != piece:
            send_message_to_all(c1, c2, 'La pièce est tombée sur ' + piece + '. Et... le joueur 2 gagne !')
        else:
            send_message_to_all(c1, c2, 'La pièce est tombée sur ' + piece + '. Mais vous avez fait le même choix !')

        # Rejouer ?
        send_message_to_all(c1, c2, 'Rejouer ? [oui/non]', True)
        rej1, rej2 = receive_message_from_all(c1, c2)
        if rej1 == 'non' or rej2 == 'non':
            play_again = False


def lancer_piece():
    r = random.randint(0, 1)
    return 'pile' if r == 0 else 'face'
