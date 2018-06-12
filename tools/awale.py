def awale_play(pos, board, round):
    score = 0
    distribute = board[pos]
    current_pos = pos
    board[pos] = 0
    for i in range(1, distribute + 1):
        # Apply point
        current_pos = (pos + i) % len(board)
        board[current_pos] += 1

    scoring = True
    while scoring:
        if check_enemy_zone(current_pos, round, len(board)) and 2 <= board[current_pos] <= 3:
            score += board[current_pos]
            board[current_pos] = 0
            current_pos -= 1
        else:
            scoring = False
    return score


def check_enemy_zone(pos, game_round, size=12):
    if game_round % 2 == 0:
        # Player 1 - selecting enemies range
        return size // 2 <= pos < size
    else:
        # Player 2 - selecting enemies range
        return 0 <= pos < size // 2
