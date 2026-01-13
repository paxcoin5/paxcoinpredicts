from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import predict_nfl_score
from data_loader import get_upcoming_games
from draftkings_api import get_public_bets
from odds_api import get_odds

app = FastAPI(title="PaxCoinPredicts API")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/games")
def games(sport: str = "NFL"):
    return get_upcoming_games(sport)

@app.get("/prediction/{game_id}")
def prediction(game_id: str):
    games = get_upcoming_games("NFL")
    if game_id not in games:
        return {"error": "Game not found"}
    game = games[game_id]
    odds = get_odds(game_id)
    pred = predict_nfl_score(game, vegas_total=odds['total'], vegas_spread=odds['spread'])
    return pred

@app.get("/public-bets/{game_id}")
def public_bets(game_id: str):
    return get_public_bets(game_id)

@app.get("/odds/{game_id}")
def odds(game_id: str):
    return get_odds(game_id)
