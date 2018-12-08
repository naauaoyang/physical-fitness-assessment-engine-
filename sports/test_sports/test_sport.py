from abc import abstractmethod
from utils.enums.assessment import Assessment


class TestSport:

    def __init__(self, name):
        self.name = name
        self.map = {}  # map assessment to five dimension index

    @abstractmethod
    def get_score(self, gender, grade, result):
        pass

    @staticmethod
    def get_assessment(score):
        if score < 60:
            return Assessment.FAIL
        elif 60 <= score < 80:
            return Assessment.PASS
        elif 80 <= score < 90:
            return Assessment.GOOD
        else:
            return Assessment.EXCELLENCE

    @abstractmethod
    def get_five_dimension_index(self, assessment):
        pass
