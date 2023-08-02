from app.model.body_parts import ImageData, ImageSize, Keypoint
class AppConst:
    UI_PATH = 'app/resources/aivisiontech_gu_v2.ui'
    BASE_C_PATH = 'c:\\'

class KeypointConst:
    EDGES = [
            [6, 4, 2, 16, 0, 19, 1, 17, 3, 5, 7],
            [1, 11, 9],
            [0, 10, 8],
            [12, 14, 18, 15, 13]
        ]
    IMAGE_SIZE = ImageSize(640, 480)
    KEYPOINTS_FRONT = {
        "ac_joint_right": Keypoint(0,200, 102),
        "ac_joint_left": Keypoint(1, 383, 95),
        "iliac_spin_right": Keypoint(2, 246, 202),
        "iliac_spin_left": Keypoint(3, 366, 165),
        "knee_right": Keypoint(4, 238, 331),
        "knee_left": Keypoint(5, 383, 317),
        "ankle_right": Keypoint(6, 232, 425),
        "ankle_left": Keypoint(7, 403, 417),
        "wrist_right": Keypoint(8, 149, 31),
        "wrist_left": Keypoint(9, 457, 36),
        "elbow_right": Keypoint(10, 74, 85),
        "elbow_left": Keypoint(11, 548, 87),
        "tragus_right": Keypoint(12, 274, 55),
        "tragus_left": Keypoint(13, 327, 56),
        "eye_right": Keypoint(14, 296,47),
        "eye_left": Keypoint(15, 336, 47),
        "lateral_thoracic_right": Keypoint(16, 235, 150),
        "latral_thoracic_left": Keypoint(17, 366, 165),
        "lips": Keypoint(18, 317, 57),
        "suprasternal_notch": Keypoint(19, 318, 100)
    }
    IMAGE_DATA_FRONT = ImageData('test', IMAGE_SIZE, KEYPOINTS_FRONT, 'test.jpg')
    
    KEYPOINTS_BACK = {
        "ac_joint_right": Keypoint(0,383, 95),
        "ac_joint_left": Keypoint(1, 200, 102),
        "iliac_spin_right": Keypoint(2, 366, 165),
        "iliac_spin_left": Keypoint(3, 246, 202),
        "knee_right": Keypoint(4, 383, 317),
        "knee_left": Keypoint(5, 238, 331),
        "ankle_right": Keypoint(6, 403, 417),
        "ankle_left": Keypoint(7, 232, 425),
        "wrist_right": Keypoint(8, 457, 36),
        "wrist_left": Keypoint(9, 149, 31),
        "elbow_right": Keypoint(10, 548, 87),
        "elbow_left": Keypoint(11, 74, 85),
        "tragus_right": Keypoint(12, 358, 56),
        "tragus_left": Keypoint(13, 274, 55),
        "eye_right": Keypoint(14, 336,44),
        "eye_left": Keypoint(15, 296, 47),
        "lateral_thoracic_right": Keypoint(16, 366, 165),
        "latral_thoracic_left": Keypoint(17, 235, 150),
        "lips": Keypoint(18, 317, 57),
        "suprasternal_notch": Keypoint(19, 318, 100)
    }
    IMAGE_DATA_BACK = ImageData('test', IMAGE_SIZE, KEYPOINTS_BACK, 'test.jpg')
        