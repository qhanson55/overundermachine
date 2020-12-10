import overunder_scraper
import sys

total_games = 0
over_games = 0
under_games = 0
even_games = 0
# wins = 0
# losses = 0

# parse arguments
for i in range(len(sys.argv)):
    if (i == 0):
        continue
    elif (i == 1):
        year = sys.argv[i]
    elif (i == 2):
        week = int(sys.argv[i])
    elif (i == 3):
        score = float(sys.argv[i])    
    elif (i == 4):
        team = sys.argv[i].lower()
    elif (i > 4):
        team = team + ' ' + sys.argv[i].lower()    

for i in range(week - 1):
    games = overunder_scraper.run_scraper(str(year), str(week - 1 - i))

    for game in games:
        game_winner = game.winner.lower()
        game_loser = game.loser.lower()
        game_score = float(game.total_score)

        if (game_winner == team or game_loser == team):
            total_games += 1
            if (game_score > score):
                over_games += 1
            elif (game_score < score):
                under_games += 1
            elif (game_score == score):
                even_games += 1
            # elif (game_loser == team):
            #     losses += 1
            # else:
            #     wins += 1



print(team.upper() + ':')
print('Has ' + str(over_games) + ' out of ' + str(total_games) + ' over a score of ' + str(score) + '.')
print('Has ' + str(under_games) + ' out of ' + str(total_games) + ' under a score of ' + str(score) + '.')
print('Has ' + str(even_games) + ' out of ' + str(total_games) + ' even with a score of ' + str(score) + '.')
# print('Was winner of ' + str(wins) + ' games')
# print('Was loser of ' + str(losses) + ' games')
