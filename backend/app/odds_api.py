import requests
import os

ODDS_API_KEY = os.environ.get("ODDS_API_KEY")

def get_odds(game_id):
    try:
        url = f"https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey={ODDS_API_KEY}&regions=us&markets=spreads,totals"
        resp = requests.get(url)
        data = resp.json()
        game_odds = data[0]['bookmakers'][0]['markets'][0]
        return {
            'home': game_odds['outcomes'][0]['price'],
            'away': game_odds['outcomes'][1]['price'],
            'spread': game_odds['outcomes'][0]['point'],
            'total': data[0]['bookmakers'][0]['markets'][1]['outcomes'][0]['point']
        }
    except:
        return {'home': -110, 'away': -110, 'spread': -3, 'total': 49.5}
