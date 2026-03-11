import json
from typing import List, Dict


class ContextJsonDataSource:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def fetch_all(self) -> List[Dict]:
        with open(self.file_path, "r") as f:
            return json.load(f)