import pandas as pd
from nba_api.stats.endpoints import teamgamelog

def save_team_gamelog_to_csv(team_id: int, file_name: str):
    gamelog = teamgamelog.TeamGameLog(team_id=team_id)
    games = gamelog.get_normalized_dict()["TeamGameLog"]
    df = pd.DataFrame(games)
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}")

# Example usage
if __name__ == "__main__":
    team_id = 1610612744  # Golden State Warriors
    save_team_gamelog_to_csv(team_id, "warriors_gamelog.csv")
