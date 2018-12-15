from collections import Counter
from sports.test_sports.vital_capacity import VitalCapacity


class Student:
    def __init__(self, name, gender, grade, height, weight, **kwargs):
        """

        :param name:
        :param gender:
        :param grade:
        :param height:
        :param weight:
        :param kwargs: test sport name and its test result, e.g. vital_capacity=1000
        """
        self.name = name
        self.gender = gender
        self.grade = grade
        self.height = height
        self.weight = weight
        self.test_sports = kwargs

    # retrieve five dimension indexes from all available test sports of this student,
    # then compute average as the final five dimension indexes
    def get_five_dimension_index(self):
        five_dimension_indexes = []
        for name, result in self.test_sports.items():
            try:
                constructor = globals()[Student.underscore_to_camelcase(name)]
                test_sport = constructor()
                score = test_sport.get_score(self.gender, self.grade, result)
                score = 70
                assessment = test_sport.get_assessment(score)
                five_dimension_index = test_sport.get_five_dimension_index(assessment)
                five_dimension_indexes.append(five_dimension_index)
            except KeyError:
                print "{} is invalid test sport name!".format(name)

        if five_dimension_indexes:
            sums = Counter()
            counters = Counter()
            for five_dimension_index in five_dimension_indexes:
                sums.update(five_dimension_index)
                counters.update(five_dimension_index.keys())
            return {x: float(sums[x]) / counters[x] for x in sums.keys()}

    def get_bmi(self):
        return self.weight / (self.height**2)

    @staticmethod
    def underscore_to_camelcase(word):
        return ''.join(x.capitalize() for x in word.split('_'))
