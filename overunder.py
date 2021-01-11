import overunder_scraper
import sys

total_games1 = 0
total_points_for1 = 0
total_points_against1 = 0
average_for1 = 0
average_against1 = 0
over_games1 = 0
under_games1 = 0
even_games1 = 0
wins_over1 = 0
losses_over1 = 0
wins_under1 = 0
losses_under1 = 0
delta_team_score1 = 0

total_games2 = 0
total_points_for2 = 0
total_points_against2 = 0
average_for2 = 0
average_against2 = 0
over_games2 = 0
under_games2 = 0
even_games2 = 0
wins_over2 = 0
losses_over2 = 0
wins_under2 = 0
losses_under2 = 0
delta_team_score2 = 0

team_abrevs = {
    'crd': 'Arizona Cardinals',
    'atl': 'Atlanta Falcons',
    'rav': 'Baltimore Ravens',
    'buf': 'Buffalo Bills',
    'car': 'Carolina Panthers',
    'chi': 'Chicago Bears',
    'cin': 'Cincinnati Bengals',
    'cle': 'Cleveland Browns',
    'dal': 'Dallas Cowboys',
    'den': 'Denver Broncos',
    'det': 'Detroit Lions',
    'gnb': 'Green Bay Packers',
    'htx': 'Houston Texans',
    'clt': 'Indianapolis Colts',
    'jax': 'Jacksonville Jaguars',
    'kan': 'Kansas City Chiefs',
    'rai': 'Las Vegas Raiders',
    'sdg': 'Los Angeles Chargers',
    'ram': 'Los Angeles Rams',
    'mia': 'Miami Dolphins',
    'min': 'Minnesota Vikings',
    'nwe': 'New England Patriots',
    'nor': 'New Orleans Saints',
    'nyg': 'New York Giants',
    'nyj': 'New York Jets',
    'phi': 'Philadelphia Eagles',
    'pit': 'Pittsburgh Steelers',
    'sfo': 'San Francisco 49ers',
    'sea': 'Seattle Seahawks',
    'tam': 'Tampa Bay Buccaneers',
    'oti': 'Tennesse Titans',
    'was': 'Washington Football Team'
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
        team1 = sys.argv[i].lower()
    elif (i == 4):
        team2 = sys.argv[i].lower()       

# team = team_abrevs[team]

games1 = overunder_scraper.run_scraper(team1, year)
games2 = overunder_scraper.run_scraper(team2, year)

total_games1 = len(games1)
total_games2 = len(games2)

for game in games1:
    total_points_for1 = total_points_for1 + game.score_for
    total_points_against1 = total_points_against1 + game.score_against
    game_score = float(game.total_score)
    if (game_score > score):
        over_games1 += 1
        if (game.winner):
            wins_over1 += 1
        else:
            losses_over1 += 1
    elif (game_score < score):
        under_games1 += 1
        if (game.winner):
            wins_under1 += 1
        else:
            losses_under1 += 1
    elif (game_score == score):
        even_games1 += 1

for game in games2:
    total_points_for2 = total_points_for2 + game.score_for
    total_points_against2 = total_points_against2 + game.score_against
    game_score = float(game.total_score)
    if (game_score > score):
        over_games2 += 1
        if (game.winner):
            wins_over2 += 1
        else:
            losses_over2 += 1
    elif (game_score < score):
        under_games2 += 1
        if (game.winner):
            wins_under2 += 1
        else:
            losses_under2 += 1
    elif (game_score == score):
        even_games2 += 1

average_for1 = total_points_for1 / total_games1
average_against1 = total_points_against1 / total_games1

average_for2 = total_points_for2 / total_games2
average_against2 = total_points_against2 / total_games2

delta_team_score1 = (average_for1 + average_against2) / 2
delta_team_score2 = (average_for2 + average_against1) / 2


print("")
print(team_abrevs[team1] + ':')
print('Has ' + str(over_games1) + ' out of ' + str(total_games1) + ' over a score of ' + str(score) + '.')
print('Has ' + str(under_games1) + ' out of ' + str(total_games1) + ' under a score of ' + str(score) + '.')
print('Has ' + str(even_games1) + ' out of ' + str(total_games1) + ' even with a score of ' + str(score) + '.')
print('Was winner of ' + str(wins_over1) + ' over games')
print('Was loser of ' + str(losses_over1) + ' over games')
print('Was winner of ' + str(wins_under1) + ' under games')
print('Was loser of ' + str(losses_under1) + ' under games')
print("Average points scored = " + str(average_for1))
print("Average points against = " + str(average_against1))
print("")
print(team_abrevs[team2] + ':')
print('Has ' + str(over_games2) + ' out of ' + str(total_games2) + ' over a score of ' + str(score) + '.')
print('Has ' + str(under_games2) + ' out of ' + str(total_games2) + ' under a score of ' + str(score) + '.')
print('Has ' + str(even_games2) + ' out of ' + str(total_games2) + ' even with a score of ' + str(score) + '.')
print('Was winner of ' + str(wins_over2) + ' over games')
print('Was loser of ' + str(losses_over2) + ' over games')
print('Was winner of ' + str(wins_under2) + ' under games')
print('Was loser of ' + str(losses_under2) + ' under games')
print("Average points scored = " + str(average_for2))
print("Average points against = " + str(average_against2))
print("")
print(team_abrevs[team1] + " points scored vs " + team_abrevs[team2] + " points against: " + str(delta_team_score1))
print(team_abrevs[team2] + " points scored vs " + team_abrevs[team1] + " points against: " + str(delta_team_score2))
print("Potential Total: " + str(delta_team_score1 + delta_team_score2))
