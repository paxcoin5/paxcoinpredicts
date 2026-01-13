def get_upcoming_games(sport):
    if sport == "NFL":
        return {
            "1": {"home_team": "Bills", "away_team": "Dolphins", "game_id": "1"},
            "2": {"home_team": "Packers", "away_team": "Vikings", "game_id": "2"}
        }
    return {}
