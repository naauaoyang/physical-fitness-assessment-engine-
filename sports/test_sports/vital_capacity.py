from sports.test_sports.test_sport import TestSport
from utils.enums.assessment import Assessment
from utils.enums.five_dimension import Dimension


class VitalCapacity(TestSport):

    def __init__(self):
        TestSport.__init__(self,
                           name='vital capacity')
        # TODO this is just a example, need change the value later
        self.map = {Assessment.EXCELLENCE: {Dimension.COORDINATION: 5,
                                            Dimension.STAMINA: 5,
                                            Dimension.FLEXIBILITY: 5,
                                            Dimension.SPEED: 5,
                                            Dimension.STRENGTH: 5},
                    Assessment.GOOD: {Dimension.COORDINATION: 4,
                                      Dimension.STAMINA: 4,
                                      Dimension.FLEXIBILITY: 4,
                                      Dimension.SPEED: 4,
                                      Dimension.STRENGTH: 4},
                    Assessment.PASS: {Dimension.COORDINATION: 3,
                                      Dimension.STAMINA: 3,
                                      Dimension.FLEXIBILITY: 3,
                                      Dimension.SPEED: 3,
                                      Dimension.STRENGTH: 3},
                    Assessment.FAIL: {Dimension.COORDINATION: 1,
                                      Dimension.STAMINA: 1,
                                      Dimension.FLEXIBILITY: 1,
                                      Dimension.SPEED: 1,
                                      Dimension.STRENGTH: 1}}

    def get_score(self, gender, grade, capacity):
        pass

    def get_five_dimension_index(self, assessment):
        return self.map[assessment]

