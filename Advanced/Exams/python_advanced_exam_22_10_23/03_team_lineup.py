def team_lineup(*args):

    teams = {}

    for arg in args:
        if arg[1] not in teams:
            teams[arg[1]] = []
        teams[arg[1]].append(arg[0])

    result = []

    sorted_teams = sorted(teams.items(), key=lambda t: (-len(t[1]), t[0]))
    for team in sorted_teams:
        result.append(f"{team[0]}:")
        for player in team[1]:
            result.append(f"  -{player}")

    return '\n'.join(result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
