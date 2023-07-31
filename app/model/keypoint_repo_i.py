import abc
import json
class KeypointRepository(abc.ABC):
    @abc.abstractmethod
    def get_image_data(self,id: str)-> dict:
        """Returns a dictionary of image data for the given id"""
        pass
    @abc.abstractmethod
    def get_all_image_data(self)-> list:
        """Returns a list of all image data"""
        pass
    @abc.abstractmethod
    def insert_one_image_data(self, parameters: str)-> bool:
        """Inserts one image data into the database"""
        pass