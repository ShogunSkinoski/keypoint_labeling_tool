from app.model.keypoint_repo_i import KeypointRepository
from app.model.bll_i import BussinesLogicLayer
from app.const.app_const import KeypointConst
from app.model.body_parts import Keypoint

class LabelingBussinesModel(BussinesLogicLayer):
    
    def __init__(self, dal: KeypointRepository):
        self.dal = dal
    
    def get_positions(self, params) -> list:
        positions = []
        for keypoint in params.keypoints.values():
            positions.append([keypoint.x, keypoint.y, keypoint.id])
        return positions
    
    def list_to_dict(self, positions: list) -> dict:
        keypoint_dict = {}
        for index, keypoint_name in enumerate(KeypointConst.KEYPOINTS_FRONT):
            keypoint_dict[keypoint_name] = Keypoint(index, positions[index][0], positions[index][1])
        return keypoint_dict
    
    def insert_one_image_data(self, image_data):
        self.dal.insert_one_image_data(image_data)