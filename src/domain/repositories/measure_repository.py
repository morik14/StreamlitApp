from abc import ABC, abstractmethod
from domain.entities import MeasureEntity


class IMeasureRepository(ABC):

    @abstractmethod
    def save(self, measure: MeasureEntity):
        pass

    @abstractmethod
    def get(self):
        pass


class MeasureRepository(IMeasureRepository):

    def save(self, measure: MeasureEntity):
        pass

    def get(self):
        pass
