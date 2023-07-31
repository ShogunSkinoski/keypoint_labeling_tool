from app.model.keypoint_repo_i import KeypointRepository
from app.model.body_parts import ImageData, JsonImageEncoder
import json

class JsonRepo(KeypointRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        
    def get_image_data(self, id: str) -> ImageData:
        raise NotImplementedError
    
    def get_all_image_data(self) -> list[ImageData]:
        try:
            list_of_image_data = []
            with open(self.file_path, 'r') as file:
                image_data_list = json.load(file)
                for data in image_data_list:
                    list_of_image_data.append(ImageData.from_json(json.loads(data)))
            return list_of_image_data
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.file_path} not found')
        except json.JSONDecodeError:
            return []
        
    def insert_one_image_data(self, image_data: ImageData) -> bool:
        all_image_data = self.get_all_image_data()
        all_image_data.append(image_data)
        try:
            with open(self.file_path, 'w') as file:
                json.dump(all_image_data, file, cls=JsonImageEncoder)
            return True
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.file_path} not found')
        except json.JSONDecodeError:
            return False