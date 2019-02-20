def draw_board(spots):
    print("   " + spots[0] + "  |  " + spots[1] + "  |  " + spots[2] + "  \n")
    print("----------------\n")
    print("   " + spots[3] + "  |  " + spots[4] + "  |  " + spots[5] + "  \n")
    print("----------------\n")
    print("   " + spots[6] + "  |  " + spots[7] + "  |  " + spots[8] + "  \n")


def get_character():

    x_or_o = input("Are you an X or an O?")
    if x_or_o == 'x' or x_or_o == 'X':
        return True
    elif x_or_o == 'o' or x_or_o == 'O':
        return False
    else:
        print("Wrong answer, you're an X now.\n")
        return True


def turn(player):
    if player:
        return int(input("Player 1 turn. Choose a number on the board: "))
    else:
        return int(input("Player 2 turn. Choose a number on the board: "))


def check_win(positions):
    win = False

    positions.sort()
    # if they won, they have to have 2 wall values
    if 1 in positions:
        if 2 in positions and 3 in positions:
            win = True
        elif 4 in positions and 7 in positions:
            win = True
        elif 5 in positions and 9 in positions:
            win = True

    if 2 in positions:
        if 5 in positions and 8 in positions:
            win = True

    if 3 in positions:
        if 6 in positions and 9 in positions:
            win = True
        elif 5 in positions and 7 in positions:
            win = True

    if 4 in positions:
        if 5 in positions and 6 in positions:
            win = True

    if 7 in positions:
        if 8 in positions and 9 in positions:
            win = True

    return win


game = True
store_positions = ['', '', '', '', '', '', '', '', '']
position_history_p1 = []
position_history_p2 = []
draw_board(store_positions)
answer = get_character()
if answer:
    marker1 = 'X'
    marker2 = 'O'
else:
    marker1 = 'O'
    marker2 = 'X'

player_turn = True

while game is not False:
    if player_turn:
        position = turn(player_turn)
        if position not in position_history_p1 and position not in position_history_p2:
            position_history_p1.append(position)
            state = check_win(position_history_p1)
            store_positions[position - 1] = marker1
            draw_board(store_positions)

            if state:
                print("Player 1 wins!")
                break
            elif len(position_history_p1) == 5:
                print("Draw. Game over.")
                break
            else:
                player_turn = False
        else:
            print("Position not available.\n")

    if not player_turn:
        position = turn(player_turn)
        if position not in position_history_p2 and position not in position_history_p1:
            position_history_p2.append(position)
            state = check_win(position_history_p2)
            store_positions[position - 1] = marker2
            draw_board(store_positions)
            if state:
                print("Player 2 wins!")
                break
            else:
                player_turn = True
        else:
            print("Position not available.\n")



