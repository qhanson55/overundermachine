import requests
from bs4 import BeautifulSoup

class Game:
    def __init__(self, winner, loser, total_score):
        self.winner = winner
        self.loser = loser
        self.total_score = total_score

def run_scraper(year, week):
    URL = 'https://www.pro-football-reference.com/years/'+ year + '/week_' + week + '.htm'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='game_summaries')

    games_soup = results.find_all('table', class_='teams')
    games_objs = []

    for game_soup in games_soup:
        winner = game_soup.find('tr', class_='winner')
        loser = game_soup.find('tr', class_='loser')
        if (winner is None) or (loser is None):
            continue

        winner_score = winner.find(class_='right').text
        loser_score = loser.find(class_='right').text
        if (winner_score is None) or (loser_score is None):
            continue
        total_score = int(winner_score) + int(loser_score)

        winner = winner.find('a').text
        loser = loser.find('a').text
        if (winner is None) or (loser is None):
            continue

        game_obj = Game(winner, loser, total_score)
        games_objs.append(game_obj)

    return games_objs