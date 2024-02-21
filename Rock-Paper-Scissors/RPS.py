def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)
    prediction = 'P'

    if len(opponent_history) > 3:
        six = "".join(opponent_history[-4:])
        play_order[six] = play_order.get(six, 0) + 1
        
        probs = [
            "".join([*opponent_history[-3:], v]) 
            for v in ['R', 'P', 'S']
        ]

        sub_order = {
            k: play_order[k]
            for k in probs if k in play_order
        }

        if sub_order:
            pred = max(sub_order, key=sub_order.get)[-1:]
        else:
            pred = prediction  # Default prediction if sub_order is empty

    else:
        pred = prediction  # Default prediction if opponent history is not long enough

    guess = {'P': 'S', 'R': 'P', 'S': 'R'}

    return guess.get(pred, 'R')  # Return 'R' as default if pred is not found in guess
