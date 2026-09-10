import json
from typing import Protocol
from pathlib import Path
from datetime import datetime, timezone


class CheckpointProtocol(Protocol):
    def load(self) -> set[str]:
        ...

    def save(self, completed_ids: set[str]) -> None:
        ...

    def is_exists(self, item_ids: str) -> bool:
        ...

    def mark_completed(self, item_ids: str) -> None:
        ...

    def is_completed(self, status: bool = False) -> None:
        ...

class Checkpoint:
    def __init__(self, checkpoint_path: Path):
        self.checkpoint_path = checkpoint_path
        self.completed_ids: set[list[any]] = set()

    def load(self) -> set[str]:

        if not self.checkpoint_path.exists():
            return set()

        with open(self.checkpoint_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.completed_ids = set(
            data.get("completed_ids", [])
        )

        return self.completed_ids

    def save(self, completed_ids: set[str]) -> None:

        self.checkpoint_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        data = {
            "completed_ids": sorted(completed_ids),
            "last_checkpoint": datetime.now(
                timezone.utc
            ).isoformat(),
        }

        with open(self.checkpoint_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def is_exist(self, item_ids: str) -> bool:
        return any(item_ids in item[0] for item in self.completed_ids)

    def mark_completed(self, item_ids: list) -> None:
        self.completed_ids.add(item_ids)
        self.save(self.completed_ids)

    def is_completed(self, status: bool = False) -> bool:
        return status