# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

my_plays = ['S']
answer = {
    '' : 'S',
    'R': 'P',
    'P': 'S',
    'S': 'R'
}

guess = [
    ['', 'S'],
    ['', 'S'],
    ['', 'S'],
    ['', 'S']
]

weight = [0,0,0,0]
play_order = {
    "RR": 0,
    "RP": 0,
    "RS": 0,
    "PR": 0,
    "PP": 0,
    "PS": 0,
    "SR": 0,
    "SP": 0,
    "SS": 0
}

def predict():
    predictions = [my_plays[-1] + 'R', my_plays[-1] + 'P', my_plays[-1] + 'S']
    final_answers = {}
    for i in play_order.keys():
        if i in predictions:
            final_answers[i] = play_order[i]
    return max(final_answers, key=final_answers.get)[-1:] if final_answers != {} else 'R'
def update(opponent_history):
    global guess
    guess = [
        [opponent_history[-6], answer[opponent_history[-5]]],
        [answer[max(set(my_plays[-10:]), key=my_plays[-10:].count)], answer[answer[max(set(my_plays[-10:]), key=my_plays[-10:].count)]]],
        [answer[my_plays[-1]], answer[answer[my_plays[-1]]]],
        [answer[predict()], answer[answer[predict()]]]
    ]
def reset_order():
    global weight, play_order
    weight = [0,0,0,0]
    play_order = {
        "RR": 0,
        "RP": 0,
        "RS": 0,
        "PR": 0,
        "PP": 0,
        "PS": 0,
        "SR": 0,
        "SP": 0,
        "SS": 0
    }
def player(prev_play, opponent_history=[]):   
    if prev_play == '':
        reset_order()
    else:
        opponent_history.append(prev_play)
        for i in range(4):
            if prev_play == guess[i][0]:
                weight[i] += 1
    prev2 = "".join(my_plays[-2:])
    
    if len(prev2) == 2:
        play_order[prev2] += 1
    if len(opponent_history) > 5:
        update(opponent_history)
    
    ans = guess[weight.index(max(weight))][1]
    my_plays.append(ans)
    return ans