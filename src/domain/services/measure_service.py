from domain.entities import MeasureEntity
from domain.repositories import MeasureRepository, IMeasureRepository


class MeasureService:

    _model_repository: IMeasureRepository = MeasureRepository()

    def __init__(self) -> None:
        pass

    def calc(self, measure: MeasureEntity):
        pass
