import overunder_scraper
import sys

total_games = 0
total_points_for = 0
total_points_against = 0
over_games = 0
under_games = 0
even_games = 0
wins_over = 0
losses_over = 0
wins_under = 0
losses_under = 0

team_abrevs = {
    'arizona cardinals': 'crd',
    'atlanta falcons': 'atl',
    'baltimore ravens': 'rav',
    'buffalo bills': 'buf',
    'carolina panthers': 'car',
    'chicago bears': 'chi',
    'cincinnati bengals': 'cin',
    'cleveland browns': 'cle',
    'dallas cowboys': 'dal',
    'denver broncos': 'den',
    'detroit lions': 'det',
    'green bay packers': 'gnb',
    'houston texans': 'htx',
    'indianapolis colts': 'clt',
    'jacksonville jaguars': 'jax',
    'kansas city chiefs': 'kan',
    'las vegas raiders': 'rai',
    'los angeles chargers': 'sdg',
    'los angeles rams': 'ram',
    'miami dolphins': 'mia',
    'minnesota vikings': 'min',
    'new england patriots': 'nwe',
    'new orleans saints': 'nor',
    'new york giants': 'nyg',
    'new york jets': 'nyj',
    'philadelphia eagles': 'phi',
    'pittsburgh steelers': 'pit',
    'san francisco 49ers': 'sfo',
    'seattle seahawks': 'sea',
    'tampa bay buccaneers': 'tam',
    'tennesse titans': 'oti',
    'washington football team': 'was'
}

# parse arguments
for i in range(len(sys.argv)):
    if (i == 0):
        continue
    elif (i == 1):
        year = sys.argv[i]
    # elif (i == 2):
    #     week = int(sys.argv[i])
    elif (i == 2):
        score = float(sys.argv[i])    
    elif (i == 3):
        team = sys.argv[i].lower()
    elif (i > 3):
        team = team + ' ' + sys.argv[i].lower()       

team = team_abrevs[team]

# for i in range(week - 1):
games = overunder_scraper.run_scraper(team, year)

total_games = len(games)

for game in games:
    # game_winner = game.winner.lower()
    # game_loser = game.loser.lower()
    total_points_for = total_points_for + game.score_for
    total_points_against = total_points_against + game.score_against
    game_score = float(game.total_score)
    if (game_score > score):
        over_games += 1
        if (game.winner):
            wins_over += 1
        else:
            losses_over += 1
    elif (game_score < score):
        under_games += 1
        if (game.winner):
            wins_under += 1
        else:
            losses_under += 1
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
print('Was winner of ' + str(wins_over) + ' over games')
print('Was loser of ' + str(losses_over) + ' over games')
print('Was winner of ' + str(wins_under) + ' under games')
print('Was loser of ' + str(losses_under) + ' under games')
print("Average points scored = " + str(total_points_for / total_games))
print("Average points against = " + str(total_points_against / total_games))
