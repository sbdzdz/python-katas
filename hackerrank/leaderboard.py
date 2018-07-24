"""
Alice is playing an arcade game and wants to climb to the top of the leaderboard.

The game uses dense ranking, so its leaderboard works like this:
- The player with the highest score is ranked number  on the leaderboard.
- Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

You are given an array of monotonically decreasing leaderboard scores, and another array of Alice's scores in ascending order. For every Alice's score, print her rank on the leaderboard.
"""

def climbingleaderboard(scores, alice):
    results = []
    place = 1
    while alice and scores:
        current = scores[0]
        if alice[-1] >= current:
            results.append(place)
            alice.pop()
        else:
            place += 1
            while scores and scores[0] == current:
                scores.pop(0)
    if not scores:
        for a in alice:
            results.append(place)

    return list(reversed(results))
