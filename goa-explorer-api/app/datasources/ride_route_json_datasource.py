import json
from pathlib import Path


class RideRouteJsonDatasource:

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> list[dict]:
        with open(self.file_path, "r") as f:
            return json.load(f)