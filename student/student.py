from utils.enums.test_sports import TestSports
from utils.enums.gender import Gender
from utils.enums.grade import Grade
from utils.constants import Constants


class Student:
    def __init__(self, _id, gender, grade, fy_score):
        """

        :param _id: unique identifier
        :param gender:
        :param grade:
        :param fy_score: current for_young score, an instance of class for_young_score.Score
        """
        self._id = _id
        self.gender = gender
        self.grade = grade
        self.fy_score = fy_score

    def update_fy_score(self, test_name, test_result):
        pass

    @staticmethod
    def get_score_from_test(gender, grade, test_name, test_result):
        """
        get score ranging from [0, 100] from gender, grate, test_name
        and test_result.

        :param gender:
        :param grade:
        :param test_name:
        :param test_result:
        :return:
        """
        score_map = TestSports[test_name.upper()] \
            .value \
            [Constants.SCORE_MAP] \
            [Gender[gender.upper()]] \
            [Grade[grade.upper()]]
        print(score_map)

        score = Student.get_score(score_map, test_result)
        print(score)

    @staticmethod
    def get_score(score_map, test_result):
        """
        TODO add implementation for tests that the larger the result the better.
        :param score_map:
        :param test_result:
        :return:
        """
        if test_result < score_map[20]:
            return int((test_result / score_map[20]) * 20)
        elif test_result < score_map[40]:
            return int(20 + (test_result - score_map[20]) / (score_map[40] - score_map[20]) * 20)
        elif test_result < score_map[60]:
            return int(40 + (test_result - score_map[40]) / (score_map[60] - score_map[40]) * 20)
        elif test_result < score_map[85]:
            return int(60 + (test_result - score_map[60]) / (score_map[85] - score_map[60]) * 20)
        elif test_result < score_map[100]:
            return int(85 + (test_result - score_map[85]) / (score_map[100] - score_map[85]) * 20)
        else:
            return 100


Student.get_score_from_test('male', 'one', 'standing_long_jump', 1.1)
