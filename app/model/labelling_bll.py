from app.model.keypoint_repo_i import KeypointRepository
from app.model.bll_i import BussinesLogicLayer

class LabelingBussinesModel(BussinesLogicLayer):
    def __init__(self, dal: KeypointRepository):
        self.dal = dal
    
    def get_positions(self, params) -> list:
        positions = []
        for keypoint in params.keypoints.values():
            positions.append([keypoint.x, keypoint.y, keypoint.id])
        return positions

