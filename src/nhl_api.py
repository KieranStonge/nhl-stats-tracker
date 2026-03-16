import requests

def get_player_stats(player_id):
    """Fetch Player stats from the NHL API."""
    url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"

    response = requests.get(url)

    data = response.json()

    first_name = data['firstName']['default']
    last_name = data['lastName']['default']
    position = data['position']
    stats = data['featuredStats']['regularSeason']['subSeason']

    print(f"Player: {first_name} {last_name}")
    print(f"Position: {position}")
    print(f"Games Played: {stats['gamesPlayed']}")
    print(f"Goals: {stats['goals']}")
    print(f"Assists: {stats['assists']}")
    print(f"Points: {stats['points']}")
    print(f"Plus/Minus: {stats['plusMinus']}")

player_id = input("Enter a player ID: ")
get_player_stats(player_id)