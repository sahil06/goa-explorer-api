from enum import Enum


class RouteDifficulty(str, Enum):
    easy = "easy"
    moderate = "moderate"
    hard = "hard"
    extreme = "extreme"