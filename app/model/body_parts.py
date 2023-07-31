from typing import Any
from dataclasses import dataclass
import json

class JsonImageEncoder(json.JSONEncoder):
    def default(self, obj):
        return json.dumps(obj, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
@dataclass
class ImageSize:
    WIDTH: int
    HEIGHT: int

@dataclass
class Keypoint:
    id: int
    x: int
    y: int

@dataclass
class ImageData():
    image_id: str
    image_size: ImageSize
    keypoints: dict[str, Keypoint]
    filename: str
    @staticmethod
    def from_json(json_data: Any) -> 'ImageData':
        return ImageData(**json_data)