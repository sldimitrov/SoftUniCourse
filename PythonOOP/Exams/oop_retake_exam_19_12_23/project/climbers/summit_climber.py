from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    STRENGTH = 150
    MINIMUM_STRENGTH_TO_CLIMB = 75

    def __init__(self, name: str):
        super().__init__(name, strength=self.STRENGTH)

    def can_climb(self):
        return self.strength >= self.MINIMUM_STRENGTH_TO_CLIMB

    def climb(self, peak: BasePeak):
        difficulty_multiplier = 1.3 if peak.difficulty_level == "Advanced" else 2.5
        self.strength -= 30.0 * difficulty_multiplier
        self.conquered_peaks.append(peak.name)