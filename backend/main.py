from fastapi import FastAPI
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, NBA Analytics App"}

@app.get("/teams")
def get_teams():
    nba_teams = teams.get_teams()
    return nba_teams

@app.get("/team-gamelog/{team_id}")
def get_team_gamelog(team_id: int):
    gamelog = teamgamelog.TeamGameLog(team_id=team_id)
    games = gamelog.get_normalized_dict()
    return games
