import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for nickname, data in players.items():
            
            




if __name__ == "__main__":
    main()
