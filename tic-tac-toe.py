# Viel Spaß!

def display_board(board):
    print("\n")
    print("\t " + board[6] + " | " + board[7] + " | " + board[8])
    print("\t---+---+---")
    print("\t " + board[3] + " | " + board[4] + " | " + board[5])
    print("\t---+---+---")
    print("\t " + board[0] + " | " + board[1] + " | " + board[2])

def check_winner(board):
    gewinnkombinationen = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for kombination in gewinnkombinationen:
        if board[kombination[0]] == board[kombination[1]] == board[kombination[2]] != ' ':
            return board[kombination[0]]

    if ' ' not in board:
        return 'Unentschieden!'

    return None

def play_game():
    board = [' '] * 9
    spieler = ['X', 'O']
    aktueller_spieler = spieler[0]
    gewinner = None
    weiterspielen = True

    while weiterspielen:
        while not gewinner:
            display_board(board)
            print("\nSpieler " + aktueller_spieler + " ist an der Reihe.")
            position = input("Wähle eine Position (1-9): ")

            if position.isdigit():
                position = int(position) - 1

                if 0 <= position <= 8 and board[position] == ' ':
                    board[position] = aktueller_spieler
                    gewinner = check_winner(board)
                    aktueller_spieler = spieler[1] if aktueller_spieler == spieler[0] else spieler[0]
                else:
                    print("\n +++++ Falsche Position! Bitte wähle eine leere Position (1-9). +++++ ")
            else:
                print("\n +++++ Falsche Eingabe! Bitte gib eine ganze Zahl ein (1-9). +++++ ")

        display_board(board)

        if gewinner == 'Unentschieden!':
            print("\nUnentschieden!")
        else:
            print("\nSpieler " + gewinner + " hat gewonnen!")

        fortsetzung = input("\nLust auf noch eine Runde? (j oder n): ")
        while fortsetzung.lower() not in ['j', 'n']:
            print("\n +++++ Falsche Eingabe! Bitte antworte mit 'j' oder 'n'. +++++ ")
            fortsetzung = input("\nLust auf noch eine Runde? (j oder n): ")

        if fortsetzung.lower() == 'n':
            weiterspielen = False
        else:
            board = [' '] * 9
            gewinner = None

    print("\n _____ Bis zum nächsten Mal :) _____ \n")

play_game()