from Server.Networking import *
from Server.Games.PileFace import play_pile_face
from Server.Games.PFC import play_p_f_s


game_name_list = ['pile_ou_face', 'p_f_c']

# Code pour commencer à jouer
def begin_party(conn1, conn2):

    chosen_game_name = choose_game(conn1, conn2)

    # play !
    if chosen_game_name == 'pile_ou_face':
        play_pile_face(conn1, conn2)
    elif chosen_game_name == 'p_f_c':
        play_p_f_c(conn1, conn2)

    send_message_to_all(conn1, conn2, "Bye !", False)


def choose_game(conn1, conn2):
    found_agreement = False
    while not found_agreement:
        (game_name_1, game_name_2) = ask_game(conn1, conn2)
        if game_name_1 == game_name_2:
            found_agreement = True
            send_message_to_all(conn1, conn2, 'You chose the same ! We gonna play ' + game_name_1 + '.')
        else:
            send_message_to_all(conn1, conn2, 'You did not choose the same... Player 1 chose ' + game_name_1 +
                                ' and Player 2 chose ' + game_name_2 + '.')
    return game_name_1


def ask_game(conn1, conn2):
    # Ask games
    ask_game = "Which game do you want to play ? [pile_ou_face/p_f_c]"
    send_message_to_all(conn1, conn2, ask_game, True)

    # Receive the name of the games they want to play
    (game_name_1, game_name_2) = receive_message_from_all(conn1, conn2)
    return game_name_1, game_name_2