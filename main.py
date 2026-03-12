import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, data in players.items():
        data_race = data["race"]
        race, _ = Race.objects.get_or_create(
            name=data_race["name"],
            defaults={"description": data_race["description"]}
        )

        data_skill = data_race["skills"]
        for skill in data_skill:
            skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race}
            )

        data_guild = data.get("guild")
        data_guild = data["guild"]
        if data_guild is not None:
            guild, _ = Guild.objects.get_or_create(
                name=data_guild["name"],
                defaults={"description": data_guild["description"]}
            )

        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild if data_guild is not None else None
            }
        )


if __name__ == "__main__":
    main()
