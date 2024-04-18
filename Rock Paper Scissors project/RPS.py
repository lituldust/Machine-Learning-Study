# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play, opponent_history=[], play_order={}):
    if prev_play == "":
        return random.choice(["R", "P", "S"])
    
    opponent_history.append(prev_play)
    prediction = 'P'

    # Save / remember the 5 last play by the opponent
    if len(opponent_history) > 4:
        last_five = "".join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1

    # Predict potential RPS that will be chose by the opponent
    potential_plays = [
        "".join([*opponent_history[-4:], v]) 
        for v in ['R', 'P', 'S']
    ]

    # How often a specific sequence of plays (last 4 plays + 1 guess) has occurred in the opponent's history
    sub_order = {
        k: play_order[k]
        for k in potential_plays if k in play_order
    }

    if sub_order:
        prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    guess = ideal_response[prediction]

    return guess
