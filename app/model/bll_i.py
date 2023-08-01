import abc
from app.model.body_parts import ImageData

class BussinesLogicLayer(abc.ABC):
    def __init__(self, dal):
        self.dal = dal
        
    @abc.abstractmethod
    def get_positions(self, params: ImageData) -> list:
        """
        return the position of the keypoints as list
        """
        pass