from enum import Enum
from utils.enums.five_dimension import Dimension
from utils.enums.gender import Gender
from utils.enums.grade import Grade
from utils.constants import Constants


class TestSports(Enum):
    STANDING_LONG_JUMP = {
        Constants.DIMENSION_MAP: {
            Dimension.STRENGTH: 4,
            Dimension.SPEED: 3,
            Dimension.STAMINA: 2,
            Dimension.COORDINATION: 2,
            Dimension.FLEXIBILITY: 1
        },
        Constants.SCORE_MAP: {
            Gender.MALE: {
                Grade.ONE: {
                    # just put some test numbers here
                    20: 1.0,
                    40: 1.2,
                    60: 1.4,
                    85: 1.6,
                    100: 2
                }
            }
        }
    }
