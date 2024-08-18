def manage_scoreboard(rounds: list[tuple[int, int]]) -> dict:
    scoreboard = {}
    
    for player, score in rounds:
        if player not in scoreboard:
            scoreboard[player] = score
        else:
            scoreboard[player] += score
    return scoreboard

rounds = [(1, 10), (2, 15), (3, -5), (1, 20), (2, -10)]
final_scores = manage_scoreboard(rounds)
print(final_scores)
