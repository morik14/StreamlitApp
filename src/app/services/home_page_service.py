from domain.entities import MeasureEntity
from domain.repositories import MeasureRepository, IMeasureRepository


class HomePageService:

    _measure_repository: IMeasureRepository = MeasureRepository()

    @classmethod
    def save_measure(cls, area_id: int, measure_value: float):
        measure = MeasureEntity(area_id=area_id, measure_value=measure_value)
        cls._measure_repository.save(measure=measure)

    @staticmethod
    def get_latest():
        pass
