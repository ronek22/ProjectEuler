from collections import Counter
hand = (line.split() for line in open('p054_poker.txt'))  # generator
values = {r: i for i, r in enumerate('23456789TJQKA', 2)}
ranks = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1),
         (3, 1, 1), (), (), (3, 2), (4, 1)]


def is_straight(cards):
    for x in range(len(cards) - 1):
        if int(cards[x + 1]) != int(cards[x]) - 1:
            return 0
    return 4


def is_flush(cards):
    test = list(x[1] for x in cards)
    return test[1:] == test[:-1]


# Counter calculate number of repetions
# Need to carry out Straight(consecutive) & Flush(all cards the same suit)
win = 0
for line in hand:

    p1_hand = line[:5]
    p2_hand = line[5:]

    p1 = Counter(x[0] for x in p1_hand).items()
    p2 = Counter(x[0] for x in p2_hand).items()

    p1 = zip(*(sorted([(v, values[k]) for k, v in p1])[::-1]))
    p2 = zip(*(sorted([(v, values[k]) for k, v in p2])[::-1]))
    p1_score = ranks.index(p1[0])
    p2_score = ranks.index(p2[0])

    # Maybe it's a straight
    if p1_score == 0:
        p1_score = is_straight(p1[1])

    if p2_score == 0:
        p2_score = is_straight(p2[1])

    if p1_score < 5:
        p1_score = 5 if is_flush(p1_hand) else p1_score

    if p2_score < 5:
        p2_score = 5 if is_flush(p2_hand) else p2_score

    if p1_score == p2_score:
        if p1[1][0] > p2[1][0]:
            win += 1
    elif p1_score > p2_score:
        win += 1

print win
