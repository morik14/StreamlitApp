from domain.entities import MeasureEntity
from domain.services import MeasureService


class HomePageService:

    @classmethod
    def save_measure(cls, area_id: int, measure_value: float):
        measure = MeasureEntity(area_id=area_id, measure_value=measure_value)
        MeasureService.calc(measure=measure)

    @staticmethod
    def get_latest():
        pass
