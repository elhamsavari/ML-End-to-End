from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Paths:
    root: Path = Path(__file__).resolve().parents[1]
    data_raw: Path = root / "data" / "raw"
    data_processed: Path = root / "data" / "processed"
    models: Path = root / "models"

@dataclass(frozen=True)
class TrainConfig:
    target_col: str = "TARGET"  # TODO: اسم ستون هدف را بگذار
    test_size: float = 0.2
    random_state: int = 42
    model_name: str = "baseline"  # TODO: baseline / xgb / ...
