from nba_api.stats.endpoints import playergamelog, commonplayerinfo, leaguegamelog
import pandas as pd
import time

def save_player_gamelog_to_csv(player_id: int, season: str, file_name: str):
    """
    Fetches and saves a player's game log for the given season to a CSV file.
    """
    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    games = gamelog.get_normalized_dict()["PlayerGameLog"]
    df = pd.DataFrame(games)
    df.to_csv(file_name, index=False)
    print(f"Player data saved to {file_name}")

def save_all_players_current_season():
    """
    Fetch all player data for the current season.
    """
    # Fetch all games for the current season to get player context
    league_log = leaguegamelog.LeagueGameLog(season="2024-25")  # Adjust for current season
    all_games = league_log.get_normalized_dict()["LeagueGameLog"]
    df_games = pd.DataFrame(all_games)
    df_games.to_csv("all_games_2024_25.csv", index=False)
    print("All games data saved.")

# Example usage
if __name__ == "__main__":
    player_id = 201939  # Example: Stephen Curry
    season = "2024-25"
    save_player_gamelog_to_csv(player_id, season, "steph_curry_gamelog.csv")
    save_all_players_current_season()
