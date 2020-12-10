import requests
from bs4 import BeautifulSoup

class Game:
    def __init__(self, winner, score_for, score_against, total_score):
        self.winner = winner
        self.score_for = score_for
        self.score_against = score_against
        self.total_score = total_score

def run_scraper(team, year):
    URL = 'https://www.pro-football-reference.com/teams/'+ team + '/' + year + '.htm'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('table', id='games')

    games_soup = results.find('tbody')
    games_soup = games_soup.find_all('tr')
    games_objs = []

    for game_soup in games_soup:
        # print(game_soup, end='\n')
        winner = game_soup.find('td', {'data-stat':'game_outcome'}).text
        # loser = game_soup.find('tr', class_='loser')
        # draw = game_soup.find('tr', class_='draw')

        if (winner is None):
            continue

        team_score = game_soup.find('td', {'data-stat':'pts_off'}).text
        opp_score = game_soup.find('td', {'data-stat':'pts_def'}).text
        if (team_score is None) or (opp_score is None) or (team_score == ''):
            continue
        total_score = int(team_score) + int(opp_score)

        # winner = winner.find('a').text
        # loser = loser.find('a').text
        # if (winner is None) or (loser is None):
        #     continue

        game_obj = Game((winner == 'W'), int(team_score), int(opp_score), total_score)
        games_objs.append(game_obj)

    return games_objs