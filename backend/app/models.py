import numpy as np

def predict_nfl_score(game, vegas_total=None, vegas_spread=None):
    team_stats = {
        'home_offense': 27,
        'home_defense': 23,
        'away_offense': 24,
        'away_defense': 25,
        'home_advantage': 3
    }

    home_exp = (team_stats['home_offense'] + team_stats['away_defense']) / 2 + team_stats['home_advantage']
    away_exp = (team_stats['away_offense'] + team_stats['home_defense']) / 2

    sims_home = np.random.normal(home_exp, 7, 10000)
    sims_away = np.random.normal(away_exp, 7, 10000)

    home_win_prob = float(np.mean(sims_home > sims_away))
    away_win_prob = 1 - home_win_prob

    return {
        'predicted_score': {
            'home': int(round(np.mean(sims_home))),
            'away': int(round(np.mean(sims_away)))
        },
        'win_probability': {
            'home': round(home_win_prob, 2),
            'away': round(away_win_prob, 2)
        },
        'cover_probability': {
            'home': round(np.mean((sims_home - sims_away) > 0), 2),
            'away': round(np.mean((sims_away - sims_home) > 0), 2)
        }
    }
