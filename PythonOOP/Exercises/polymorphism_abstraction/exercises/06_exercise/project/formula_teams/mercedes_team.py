from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def sponsors(self):
        sponsors_info = {
            "Petronas": {
                1: 1_000_000,
                3: 500_000,
            },
            "TeamViewer": {
                5: 100_000,
                7: 50_000,
            },
        }

        return sponsors_info

    @property
    def expenses_for_one_race(self) -> int:
        return 200_000
