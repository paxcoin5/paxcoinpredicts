import requests

def get_public_bets(game_id):
    # Placeholder for DraftKings percentages
    try:
        url = f"https://sportsbook.draftkings.com//site-api/odds/future/{game_id}"
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = resp.json()
        home_percent = float(data['home_team_percent']) / 100
        away_percent = float(data['away_team_percent']) / 100
        return {'home': home_percent, 'away': away_percent}
    except:
        return {'home': 0.5, 'away': 0.5}
