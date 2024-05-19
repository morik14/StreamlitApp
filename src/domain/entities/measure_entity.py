import datetime
from dataclasses import dataclass


@dataclass
class MeasureEntity:
    area_id: int = None
    measure_date: str = None
    measure_value: int = None

    def __post_init__(self):
        self.measure_date = datetime.datetime.now().strftime("%H%M%S")
